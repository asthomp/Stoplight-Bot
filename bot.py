import discord.client
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
from dotenv import load_dotenv

from setup import personalization, config, command_list as c
from utils import *

# Privileged Intents
intents = discord.Intents.all()
intents.guilds = True
intents.emojis = True
intents.members = True
intents.presences = True
intents.messages = True

# Variables
load_dotenv()
phrases = personalization
bot_key = phrases.key

# Load client
client = commands.Bot(command_prefix=phrases.prefixes, intents=intents)


# Wake up bot!
@client.event
async def on_ready():
    print(f'{bot_key.capitalize()} just woke up.')
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


# This command sends a list of the bot's commands.
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


# == STOPLIGHT FEATURE ==

async def stoplight(ctx, guild_config, key):
    emoji = get_config(ctx, guild_config, key, "emoji")
    alert = get_config(ctx, guild_config, key, "alert")
    message = get_config(ctx, guild_config, key, "message")

    user_message = f"{emoji} {alert} {emoji} {message}"
    if len(user_message) > 0:
        await ctx.send(user_message)

    # If an admin channel is configured, duplicate the command, linking the user & channel involved.
    # This will throw an error if the bot doesn't have access to the admin channel.
    if ctx.guild.id in guild_config.keys() and guild_config[ctx.guild.id]["admin_channel"] is not None:
        admin_message = get_config(ctx, guild_config, key, "admin_message")
        if len(admin_message) > 0:
            try:
                await ctx.guild.get_channel(guild_config[ctx.guild.id]["admin_channel"]).send(admin_message)
            except Exception as err:
                print(err)
    # Deletes the message the user sent
    await ctx.message.delete()


@client.command(no_pm=True)
@has_permissions(send_messages=True)
async def green(ctx):
    await stoplight(ctx, config.guild_config, "green")


@client.command(no_pm=True)
@has_permissions(send_messages=True)
async def yellow(ctx):
    await stoplight(ctx, config.guild_config, "yellow")


@client.command(no_pm=True)
@has_permissions(send_messages=True)
async def red(ctx):
    await stoplight(ctx, config.guild_config, "red")


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
