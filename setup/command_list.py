# Description: Returns a formatted list of the bot's commands and/or instructions to use them.
# Customize using f-strings.
def command_list(ctx, admin, bot_name):
    user_commands = f"\n\t🟢\t 🟡\t🔴\n\n" \
                    f"==STOPLIGHT-BOT COMMANDS ==\n" \
                    f"Most commands do not work in private messages.\n\n" \
                    f"Ping bots with `{bot_name} ping`\n" \
                    f"List commands with `{bot_name} commands`\n\n" \
                    f"**Conversational Triggers**:\n" \
                    f"The bot can respond to some natural speech. Here are some examples:\n\n" \
                    f"> \t\tHi / Hello / Hey {bot_name.capitalize()}.\n" \
                    f"> \t\tWhat's up, {bot_name.capitalize()}?\n" \
                    f"> \t\tHow\'s your day going, {bot_name.capitalize()}.\n" \
                    f"> \t\tThanks {bot_name.capitalize()}!\n" \
                    f"> \t\tSorry {bot_name.capitalize()}!\n\n" \
                    f"**Stoplight Commands**:\n\n" \
                    f"> \t\tLet someone know that you\'re good-to-go with `{bot_name} green`\n" \
                    f"> \t\tIf the conversation should proceed with caution, use `{bot_name} yellow`\n" \
                    f"> \t\tIf you need to stop the conversation and ping an admin, use `{bot_name} red`"
    admin_commands = f"\n\n**ADMIN Commands**:\n\n" \
                     f"> \t\tReboot bot with `{bot_name} reboot`\n\n"
    tail = f"🟢\t 🟡\t🔴\n"

    if admin:
        return user_commands + admin_commands + tail
    else:
        return user_commands + tail
