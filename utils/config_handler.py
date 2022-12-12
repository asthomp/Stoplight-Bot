from setup.config import guild_config as c

default_prefixes = ["stop! ", "Stoplight ", "stoplight ", "STOPLIGHT "]
default_config = {"green": {"emoji": f"🟢",
                            "alert": f"Good-to-go.",
                            "message": f"Someone in this channel just called :white_check_mark: green "
                                       f":white_check_mark: ; they are good to go."},
                  "yellow": {"emoji": f"🟡",
                             "alert": f"Be mindful!",
                             "message": f"Someone in the channel just called :yellow_square: yellow "
                                        f":yellow_square: ; slow down, take care to be kind and "
                                        f"conscientious, and take a break if you need one."},
                  "red": {"emoji": f"🔴",
                          "alert": f"Time out!",
                          "message": f"Someone in the channel just called :octagonal_sign: red "
                                     ":octagonal_sign: ;  stop this conversation and take a break. Someone "
                                     "will pop in shortly to help resolve the situation if necessary."}
                  }


# Description: Returns a message from the guild's entry in the setup/config file.
# If there isn't one, returns the default message.
def get_message(ctx, color):
    if config_exists(ctx.guild.id, color, "message"):
        return replace_placeholders(ctx, c[ctx.guild.id][color]["message"])
    else:
        return default_config[color]["message"]


# Description: Returns an admin message from the guild's entry in the setup/config file.
# If there isn't one, returns an empty string.
def get_admin_message(ctx, color):
    if admin_channel(ctx.guild.id) and config_exists(ctx.guild.id, color, "admin_message"):
        return replace_placeholders(ctx, c[ctx.guild.id][color]["admin_message"])
    else:
        return ""


# Description: Returns a customized emoji from the guild's entry in the setup/config file.
# If there isn't one, returns the default emoji.
def get_emoji(guild_id, color):
    if guild_id in c.keys() and c[guild_id][color]["emoji"] is not None:
        return c[guild_id][color]["emoji"]
    else:
        return default_config[color]["emoji"]


# Description: Returns the customized alert from the guild's entry in the setup/config file.
# If there isn't one, returns the default alert.
def get_alert(guild_id, color):
    if guild_id in c.keys() and c[guild_id][color]["alert"] is not None:
        return c[guild_id][color]["alert"]
    else:
        return default_config[color]["alert"]


# Description: Given a guild ID, checks whether-or-not a guild has a preconfigured asset for a given color.
def config_exists(guild_id, color, asset):
    return guild_id in c.keys() and color in c[guild_id].keys() and asset in c[guild_id][color].keys() \
           and c[guild_id][color][asset] is not None


# Description: Given a guild ID, checks whether-or-not an admin channel is configured.
def admin_channel(guild_id):
    return guild_id in c.keys() and "admin_channel" in c[guild_id].keys() and c[guild_id]["admin_channel"] is not None


# Description: Given a guild ID, returns a preconfigured admin channel, if possible.
def get_admin_channel(guild_id):
    if admin_channel(guild_id):
        return c[guild_id]["admin_channel"]
    else:
        return None


# Description: Given a guild ID, checks whether-or-not moderators can be tagged in the preconfigured admin channel.
def moderator_role(guild_id):
    return guild_id in c.keys() and "admin_channel" in c[guild_id].keys() and c[guild_id]["admin_channel"] is not None \
           and "moderator_role" in c[guild_id].keys() and c[guild_id]["moderator_role"] is not None


# Given a context object and a message, replaces all placeholder keywords in that message as appropriate.
#               @USER will link to the message's original author.
#               #CHANNEL will link to the original message's channel.
#               #ADMIN_CHANNEL will link to the channel specified under "admin_channel".
#               !MODERATOR_ROLE will tag the role specified under "moderator_role".
def replace_placeholders(ctx, msg):
    if ctx.message.author.id:
        user = ctx.message.author.id
    else:
        user = "unknown-user"

    if ctx.message.channel.id:
        channel = ctx.message.channel.id
    else:
        channel = "unknown-channel"

    if admin_channel(ctx.guild.id):
        mod_channel = c[ctx.guild.id]['admin_channel']
    else:
        mod_channel = "unknown-admin-channel"

    if moderator_role(ctx.guild.id):
        mod_role = c[ctx.guild.id]['moderator_role']
    else:
        mod_role = "unknown-moderator-role"

    return msg.replace("@USER", f"<@!{user}>").replace("#CHANNEL", f"<#{channel}>") \
        .replace("#ADMIN_CHANNEL", f"<#{mod_channel}>").replace("!MODERATOR_ROLE", f"<@&{mod_role}>")
