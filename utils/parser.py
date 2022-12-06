# Helper functions are simple functions that abstract away various tasks.


# Description: Based on the total count, converts q unit to its plural form.
def pluralizer(total_count, unit, plural_suffix):
    if total_count == 1:
        return f"{total_count} {unit}"
    else:
        return f"{total_count} {unit}{plural_suffix}"


# Description: Retrieves and formats strings from the guild_config dictionary. Uses the following
# placeholders: "@USER", "#CHANNEL", "#ADMIN_CHANNEL", and "!MODERATOR_ROLE".
def get_config(ctx, guild_config, key, asset):
    if ctx.guild.id in guild_config.keys():
        user = f"<@!{ctx.message.author.id}>"
        channel = f"<#{ctx.message.channel.id}>"
        admin_channel = f"<#{guild_config[ctx.guild.id]['admin_channel']}>"
        moderator_role = f"<@&{guild_config[ctx.guild.id]['moderator_role']}>"
        asset = guild_config[ctx.guild.id][key][asset];
        if asset is not None:
            return asset.replace("@USER", user).replace("#CHANNEL", channel).replace(
                "#ADMIN_CHANNEL", admin_channel).replace("!MODERATOR_ROLE", moderator_role)
        else:
            return ""
    else:
        return guild_config["default"][key][asset]
