#!/usr/bin/env python3
from dotenv import load_dotenv

import discord
import discord.client
import discord.types.emoji
from discord.ext import commands, tasks
from discord.app_commands import MissingPermissions

from setup import personalization as phrases
from cogs.stoplight import Stoplight
from utils import command_list as c
from utils import *

# Variables
load_dotenv()
prefixes = phrases.prefixes + default_prefixes
bot_key = phrases.key


# == LOAD BOT ==
class Bot(commands.Bot):
    def __init__(self):
        # Privileged Intents
        intents = discord.Intents.all()
        intents.guilds = True
        intents.emojis = True
        intents.members = True
        intents.presences = True
        intents.messages = True
        intents.message_content = True

        super().__init__(command_prefix=prefixes, intents=intents, application_id=int(os.getenv('ID')))
        self.synced = False

    async def on_ready(self):
        # Check if the tree is synced.
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync()
            self.synced = True
            print(f"Synced slash commands for {self.user}.")

        # Start the activity cycle.
        try:
            change_status.start()
            print(f"Started activity cycle for {self.user}.")
        except RuntimeError as err:
            print(f"{self.user} has a running activity cycle.")

        await self.add_cog(Stoplight(self))

        print(f'{client.user} just woke up.')


client = Bot()



# == ADMINISTRATIVE FUNCTIONS ==
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


# == ACTIVITY HANDLER ==
# This loop randomly selects a status for the bot.
@tasks.loop(minutes=7)
async def change_status():
    await get_random_activity(discord, client, phrases.watching,
                              phrases.playing, phrases.listening)


# == ROLE-PLAY ACTIONS ==
@client.command(no_pm=True)
async def hug(ctx, *target):
    original_target = " ".join(target)
    target = original_target.rstrip(".,!?")
    target = target.lower()

    # Find a user to perform an RP action on.
    user_object = find_user(ctx, target)
    if user_object:
        await perform_action(ctx.message.channel, user_object.id, "hugs")



# == MESSAGE HANDLER ==
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


# == ERROR HANDLERS ==
# Error handler for invalid chat-commands.
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        print(f"{ctx.author} triggered the following error: [{error}]")
        return
    else:
        raise error


@client.tree.error
async def on_error(interaction, error):
    ctx = await build_context(discord, interaction)
    if isinstance(error, MissingPermissions):
        print(f"{ctx.author} triggered the following error: [{error}]")
        await ctx.send(str(error), ephemeral=True)
        return
    else:
        raise error


client.run(os.getenv('DEV_TEST_BOT_TOKEN'))
