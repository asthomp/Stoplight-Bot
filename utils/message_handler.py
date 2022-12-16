# noinspection PyPackageRequirements
import copy


# Description: Given an interaction, returns a discord.py context object.
async def build_context(discord, interaction):
    context_object = await discord.ext.commands.Context.from_interaction(interaction)
    return context_object


# Description: Receives a message object and sends a response (after checking various parameters).
async def send_message(message, response, nsfw=False):
    if nsfw and not message.channel.is_nsfw():
        print("ERROR: NSFW content triggered in SFW channel.")
        return

    # Identify the user-tagging-sentinel and replace it appropriately.
    if "@USER" in response:
        response = response.replace("@USER", "<@!" + str(message.author.id) + ">")

    await message.channel.send(response)


# Description: Given a channel, a target user's ID, and an action, sends an "action" message.
async def perform_action(channel, target_id, action):
    response = "*" + str(action) + "*" + "  " + "<@!" + str(target_id) + ">"
    await channel.send(response)


# Description: Checks whether a given message is included in a list of trigger phrases; ignore it if quoted.
def check_if_message_contains_phrase(message, list_of_phrases):
    for phrase in list_of_phrases:
        if phrase in message.content.lower():
            previous_char_index = message.content.find(phrase) - 1
            # Check for captures or other invalid commands,
            if previous_char_index >= 0 and (
                    message.content[previous_char_index] == '\"' or message.content[previous_char_index] == '\''):
                return False
            return True
    return False


# Description: Replace a word in a message; function returns False if this cannot be done.
def replace_word(message, original, new):
    temp_message = copy.copy(message).lower()
    starting_index = temp_message.find(original.lower())
    ending_index = starting_index + len(original)

    if starting_index == -1:
        return False
    else:
        return message[0:starting_index] + new.capitalize() + message[ending_index:]
