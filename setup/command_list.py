# Description: Returns a formatted list of the bot's commands and/or instructions to use them.
# Customize using f-strings.
def command_list(ctx, admin, bot_name):
    user_commands = f"\n\t🟢\t 🟡\t🔴\n\n" \
                    f"==STOPLIGHT-BOT COMMANDS ==\n" \
                    f"Most commands do not work in private messages.\n\n" \
                    f"> \t\tPing bots with `{bot_name} ping`\n" \
                    f"> \t\tList commands with `{bot_name} commands`\n\n" \
                    f"**Conversational Triggers**:\n" \
                    f"The bot can respond to some natural speech. Here are some examples:\n\n" \
                    f"> \t\tHi / Hello / Hey {bot_name.capitalize()}.\n" \
                    f"> \t\tWhat's up, {bot_name.capitalize()}?\n" \
                    f"> \t\tHow\'s your day going, {bot_name.capitalize()}.\n" \
                    f"> \t\tThanks {bot_name.capitalize()}!\n" \
                    f"> \t\tSorry {bot_name.capitalize()}!\n\n" \
                    f"**Stoplight Commands**:\n\n" \
                    f"> \t\tIf you\'re good-to-go, use `{bot_name} green`\n" \
                    f"> \t\tIf everyone should proceed with caution, use `{bot_name} yellow`\n" \
                    f"> \t\tIf the conversation should stop, use `{bot_name} red`"
    admin_commands = f"\n\n**ADMIN ONLY Commands**:\n\n" \
                     f"> \t\tReboot bot with `{bot_name} reboot`\n\n"
    tail = f"🟢\t 🟡\t🔴\n"

    if admin:
        return user_commands + admin_commands + tail
    else:
        return user_commands + tail
