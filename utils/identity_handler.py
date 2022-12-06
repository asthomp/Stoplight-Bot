# == IDENTITY HANDLER ==
# Descriptions: Functions that handle managing the bot's instance as well as identifying various types of users.
import os
import random
import sys


# == BOT MANAGEMENT ==
# Description: Reboots a given bot when prompted by an authorized user.
async def reboot_bots(ctx, bot):
    bot = bot.capitalize()
    if authorize_user(ctx.message.author):
        print(f"{ctx.message.author} rebooted {bot}.")
        await ctx.send(f" :computer:  {bot} is rebooting.")
        print("\t => git pull")
        os.system("git pull")
        print(f"\t =>python3 {sys.argv[0]}")
        os.system(f"python3 {sys.argv[0]}")
    else:
        await ctx.send(
            f" :computer:  Only admins can reboot {bot}!")


# == USER MANAGEMENT ==
# Description: Given a user object, returns true if the user is an administrator (or the developer).
def authorize_user(user):
    if user.id == int(os.getenv('DEV_ID')) or user.guild_permissions.administrator:
        return True
    else:
        return False


# Description: Given a context, returns the display_name of a random guild member.
def random_user(ctx):
    return random.choice([member.display_name for member in ctx.guild.members])


# Description: Given a context and a user's name (or <@ID>>), searches for a guild member object.
def find_user(ctx, target):
    # The target should always be compared as a string.
    target = str(target)
    # Look the user up by user ID.
    if target[0:2] == "<@":
        target = target[2:-1]
        user = [member for member in ctx.guild.members if
                str(member.id) == target]
    else:
        # Look the user up by name.
        user = [member for member in ctx.guild.members if
                member.display_name.lower() == target or member.name.lower() == target]

    if user:
        return user.pop()
    else:
        return False
