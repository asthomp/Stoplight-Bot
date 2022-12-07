# Description: Returns a formatted list of the bot's commands and/or instructions to use them.
# Customize using f-strings.
def command_list(ctx, admin, bot_name):
    user_commands = f"\n\t🟢\t 🟡\t🔴\n" \
                    f"==STOPLIGHT-BOT COMMANDS ==\n\n" \
                    f"All bots respond to both chat messages and private messages.\n\n" \
                    f"Ping bots with `{bot_name} ping`\n" \
                    f"List commands with `{bot_name} commands`\n\n" \
                    f"**Conversation Triggers**:\n" \
                    f"Hi / Hello / Hey, {bot_name.capitalize()}.\n" \
                    f"What's up / What are you doing, {bot_name.capitalize()}.\n" \
                    f"How are you/How\'s your day going, {bot_name.capitalize()}.\n" \
                    f"Thanks / Thank you, {bot_name.capitalize()}.\n" \
                    f"Sorry / My bad {bot_name.capitalize()}. \n\n" \
                    f"**Stoplight Triggers**:\n" \
                    f"Let someone know that you\'re good-to-go with `{bot_name} green'\n" \
                    f"If the conversation should proceed with caution use `{bot_name} yellow'\n" \
                    f"To stop the conversation and ping an admin use `{bot_name} red'\n"
    admin_commands = f"\n\n**ADMIN Commands**:\n" \
                     f"Reboot bot with `{bot_name} reboot`\n"
    if admin:
        return user_commands + admin_commands + f"🟢\t 🟡\t🔴\n"
    else:
        return user_commands + f"🟢\t 🟡\t🔴\n"
