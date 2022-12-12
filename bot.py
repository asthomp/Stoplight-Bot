import discord.client
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from dotenv import load_dotenv

from setup import personalization as phrases
from utils import command_list as c
from utils import *

# Variables
load_dotenv()
prefixes = phrases.prefixes + default_prefixes
bot_key = phrases.key


# Load Bot
class Bot(commands.Bot):
    def __init__(self):
        # Privileged Intents
        intents = discord.Intents.default()
        intents.guilds = True
        intents.emojis = True
        intents.members = True
        intents.presences = True
        intents.messages = True
        intents.message_content = True

        intents = discord.Intents.default()
        intents.messages = True


        super().__init__(command_prefix=prefixes, intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}.")


client = Bot()


# Wake up bot!
@client.event
async def on_ready():
    print(f'{client.user} just woke up.')
    change_status.start()


# This error handler catches invalid commands.
@client.event
async def on_command_error(ctx, error):
    print(f"{ctx.author.display_name} triggered {error}.")
    if isinstance(error, discord.ext.commands.CommandNotFound):
        return
    else:
        raise error


# This command pings the bot to confirm that it's online.
@client.command(no_pm=True)
async def ping(ctx):
    await ctx.send(phrases.ping)


# This command reboots the bot - it can only be used by a guild admin or the developer.
@client.command(no_pm=True)
async def reboot(ctx):
    await reboot_bots(ctx, bot_key)


# This command sends a list of available commands to the channel.
@client.command()
async def commands(ctx):
    await ctx.send(c.command_list(ctx, authorize_user(ctx.message.author), bot_key))


# This loop randomly selects a status for the bot.
@tasks.loop(minutes=7)
async def change_status():
    await get_random_activity(client, phrases.watching,
                              phrases.playing, phrases.listening)


# == ROLE-PLAY ACTIONS
@client.command(no_pm=True)
async def hug(ctx, *target):
    original_target = " ".join(target)
    target = original_target.rstrip(".,!?")
    target = target.lower()

    # Find a user to perform an RP action on.
    user_object = find_user(ctx, target)
    if user_object:
        await perform_action(ctx.message.channel, user_object.id, "hugs")


# == STOPLIGHT FUNCTIONALITY ==
async def stoplight(ctx, color, flagged_message=None):
    # Post an announcement to the source channel.
    emoji = get_emoji(ctx.guild.id, color)
    alert = get_alert(ctx.guild.id, color)
    message = get_message(ctx, color)

    user_message = f"{emoji} {alert} {emoji} {message}"
    if len(user_message) > 0:
        await ctx.channel.send(user_message)

    # If configured, post a stoplight message to the admin channel.
    if admin_channel(ctx.guild.id):
        admin_message = get_admin_message(ctx, color)
        if len(admin_message) > 0:
            await ctx.guild.get_channel(get_admin_channel(ctx.guild.id)).send(admin_message)

    # If the user flags a message and an admin channel has been configured, embed the flagged message
    # in the admin channel.
    if admin_channel(ctx.guild.id) and flagged_message is not None and ctx.guild.id == flagged_message.guild.id:
        embed = discord.Embed(title=f"{emoji} Flagged Message")
        embed.description = flagged_message.content
        embed.set_author(name=flagged_message.author.display_name,
                         icon_url=flagged_message.author.display_avatar.url)
        embed.timestamp = flagged_message.created_at
        url_view = discord.ui.View()
        url_view.add_item(
            discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url,
                              url=flagged_message.jump_url))

        await ctx.guild.get_channel(get_admin_channel(ctx.guild.id)).send(embed=embed, view=url_view)


async def _text(ctx, color):
    await stoplight(ctx, color)
    await ctx.message.delete()


async def _slash(interaction, color):
    ctx = await discord.ext.commands.Context.from_interaction(interaction)
    await stoplight(ctx, color)
    await ctx.send(f"{default_config[color]['emoji']} A {color} stoplight was sent to <#{interaction.channel.id}>.",
                   ephemeral=True)


async def _message_context_menu(interaction, color, flagged_message):
    ctx = await discord.ext.commands.Context.from_interaction(interaction)
    await stoplight(ctx, color, flagged_message)
    await ctx.send(f"{default_config[color]['emoji']} A {color} stoplight was sent to <#{interaction.channel.id}>.",
                   ephemeral=True)


# == STOPLIGHT (PREFIXED CHAT-COMMANDS) ==
# Chat commands are sent directly to a channel using a preconfigured prefix, with the default being "stoplight".
# Once a chat command has been issued, the command message is deleted to preserve a user's anonymity.
# Note: While hybrid chat & application commands are available, each command is kept separate. If Discord removes
# support for them altogether, this simplifies removal.
@client.command(pass_context=True)
@has_permissions(send_messages=True)
async def green(ctx):
    await _text(ctx, "green")


@client.command(pass_context=True)
@has_permissions(send_messages=True)
async def yellow(ctx):
    await _text(ctx, "yellow")


@client.command(pass_context=True)
@has_permissions(send_messages=True)
async def red(ctx):
    await _text(ctx, "red")


# == STOPLIGHT (/SLASH APPLICATION COMMANDS) ==
# /Slash application commands are invoked by typing "/" in the message text-box of a given channel.
@client.tree.command(name='green', description="🟢 Green means you\'re good to continue the conversation.")
async def _green(interaction: discord.Interaction):
    await _slash(interaction, "green")


@client.tree.command(name='yellow', description="🟡 Yellow means the conversation should proceed with caution.")
async def _yellow(interaction: discord.Interaction):
    await _slash(interaction, "yellow")


@client.tree.command(name='red', description="🔴 Red means the conversation should stop.")
async def _red(interaction: discord.Interaction):
    await _slash(interaction, "red")


# == STOPLIGHT (CONTEXT-MENU APPLICATION COMMANDS) ==
# Context-menu application commands can be invoked by right-clicking on a given message.
@client.tree.context_menu(name='🟢 Green Stoplight')
async def __green(interaction: discord.Interaction, message: discord.Message):
    await _message_context_menu(interaction, "green", message)


@client.tree.context_menu(name='🟡 Yellow Stoplight')
async def __yellow(interaction: discord.Interaction, message: discord.Message):
    await _message_context_menu(interaction, "yellow", message)


@client.tree.context_menu(name='🔴 Red Stoplight')
async def __red(interaction: discord.Interaction, message: discord.Message):
    await _message_context_menu(interaction, "red", message)


# == MESSAGE HANDLING ==
@client.event
async def on_message(message):
    # Bot should not respond to itself.
    if message.author == client.user:
        return

    # Respond to direct commands
    await client.process_commands(message)

    # Respond to user (mimics natural-speech)
    if not message.author.bot:
        await respond_to_user(message)


# Bot responds to the user.
async def respond_to_user(message):
    # Check if message contains any trigger phrases.
    if check_if_message_contains_phrase(message, phrases.greetings_trigger):
        await send_message(message, random.choice(phrases.greetings_response))
    elif check_if_message_contains_phrase(message, phrases.what_trigger):
        await send_message(message, random.choice(phrases.what_response))
    elif check_if_message_contains_phrase(message, phrases.how_trigger):
        await send_message(message, random.choice(phrases.how_response))
    elif check_if_message_contains_phrase(message, phrases.welcome_trigger):
        await send_message(message, random.choice(phrases.welcome_response))
    elif check_if_message_contains_phrase(message, phrases.sorry_trigger):
        await send_message(message, random.choice(phrases.sorry_response))

    # Compliment functionality - 50/50 chance for a message response.
    if check_if_message_contains_phrase(message, phrases.variants) and \
            check_if_message_contains_phrase(message, phrases.compliment_trigger):
        await message.add_reaction('😈')
        toggle = random.randint(0, 1)
        if toggle == 0:
            await message.add_reaction('💋')
            await message.channel.send(
                random.choice(phrases.compliment_response))


client.run(os.getenv('TOKEN'))
