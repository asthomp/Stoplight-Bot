# == IDENTITY HANDLER ==
# Descriptions: Functions that handle manage users, permissions and moderation.
import os
import random
import sys


# == BOT MANAGEMENT ==
# Description: Reboots a given bot when prompted by an authorized user.
async def reboot_bots(ctx, bot):
    bot = bot.capitalize()
    if authorize_user(ctx.message.author):
        await ctx.send(f" :computer:  {bot} is rebooting.")
        os.execv(sys.executable, ['git pull'])
        os.execv(sys.executable, ['python3'] + sys.argv)
    else:
        await ctx.send(
            f" :computer:  Only admins can reboot {bot}!")


# == USER MANAGEMENT ==
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


# == PERMISSIONS ==
# Description: Given a user object, returns true if the user is an administrator (or the developer).
def authorize_user(user):
    if user.id == int(os.getenv('DEV_ID')) or user.guild_permissions.administrator:
        return True
    else:
        return False


# Description: These functions check whether-or-not a user has various
# permissions by performing bitwise operations.
def can_kick(permissions):
    return bool(permissions.value & (1 << 1))


def can_ban(permissions):
    return bool(permissions.value & (1 << 2))


def is_admin(permissions):
    return bool(permissions.value & (1 << 3))


def can_manage_channels(permissions):
    return bool(permissions.value & (1 << 4))


def manage_guild(permissions):
    return bool(permissions.value & (1 << 5))


def add_reactions(permissions):
    return bool(permissions.value & (1 << 6))


def view_channel(permissions):
    return bool(permissions.value & (1 << 10))


def send_messages(permissions):
    return bool(permissions.value & (1 << 11))


def manage_messages(permissions):
    return bool(permissions.value & (1 << 13))


def manage_roles(permissions):
    return bool(permissions.value & (1 << 28))


def use_application_commands(permissions):
    return bool(permissions.value & (1 << 31))


def moderate_members(permissions):
    return bool(permissions.value & (1 << 40))
