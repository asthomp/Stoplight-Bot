# Description:  The guild_config object contains information about each of the guilds using Stoplight-Bot.
#               If not configured, it uses the default settings.
# Access Keys:  Guilds added to this object should use the guild's Discord ID (no quotes) as a key.
# Identity:     You can customize non-Stoplight-related responses in "personalization.py".
# Placeholders: Phrases can be included in "message" and "admin_message" to link various Discord entities.
#               @USER will link to the message's original author.
#               #CHANNEL will link to the original message's channel.
#               #ADMIN_CHANNEL will link to the channel specified under "admin_channel".
#               !MODERATOR_ROLE will tag the role specified under "moderator_role".
# Emojis:       Non-animated custom emojis should be formatted as follows: <:EMOJI_NAME:EMOJI_ID>
#               To get a custom emoji's ID, right-click on the emoji, select "Copy Link", open it in your
#               browser. The ID is the long number between the  "/" and the image file extension (ex: .jpg, .gif).


guild_config = {  # Default Settings
    "default": {"green": {"emoji": f"🟢",
                          "alert": f"Good-to-go.",
                          "message": f"Someone in this channel just called :white_check_mark: green "
                                     f":white_check_mark: ; they are good to go.",
                          "admin_message": None},
                "yellow": {"emoji": f"🟡",
                           "alert": f"Be mindful!",
                           "message": f"Someone in the channel just called :yellow_square: yellow "
                                      f":yellow_square: ; slow down, take care to be kind and "
                                      f"conscientious, and take a break if you need one.",
                           "admin_message": None},
                "red": {"emoji": f"🔴",
                        "alert": f"Time out!",
                        "message": f"Someone in the channel just called :octagonal_sign: red "
                                   ":octagonal_sign: ;  stop this conversation and take a break. Someone "
                                   "will pop in shortly to help resolve the situation if necessary.",
                        "admin_message": None}
                },
    # Sample 1
    875820996047802398: {"id": 875820996047802398,
                         "name": f"Better Than Chuck",
                         "type": f"Guild",
                         "owner": 349005712623534080,
                         "admin_channel": 968663212436365322,
                         "moderator_role": 927092713428504606,
                         "green": {
                             "emoji": None,
                             "alert": None,
                             "message": f"Someone in this channel just called :white_check_mark: green "
                                        f":white_check_mark: ; they are good to go.",
                             "admin_message": f"@USER just called :white_check_mark: green "
                                              f":white_check_mark: in #CHANNEL; they are good to go."},
                         "yellow": {
                             "emoji": f"<:BTC_z_FunkyTown:893371139198439485>",
                             "alert": f"Funky Town!",
                             "message": f"Someone in the channel just called :yellow_square: yellow "
                                        f":yellow_square: ; slow down, take care to be kind and "
                                        f"conscientious, and take a break if you need one.",
                             "admin_message": f"@USER just called :yellow_square: yellow :yellow_square: "
                                              f"in #CHANNEL. Please check in on them, but only intervene "
                                              f"if the situation escalates."},
                         "red": {
                             "emoji": f"<:BTC_z_Poughkeepsie:893371139252944926>",
                             "alert": f"Poughkeepsie!",
                             "message": f"Someone in the channel just called :octagonal_sign: red "
                                        f":octagonal_sign: ;  stop this conversation and take a break. "
                                        f"!MODERATOR_ROLE will pop in shortly to help resolve the situation"
                                        f" if necessary.",
                             "admin_message": f"@USER just called :octagonal_sign: red :octagonal_sign: "
                                              f"in #CHANNEL. Please reply here in #ADMIN_CHANNEL to let "
                                              f"your fellow mods know you'll be the one checking it out, "
                                              f"then head over to #CHANNEL to ensure the code of conduct "
                                              f"is being followed and all members are being respected."}
                         },
    # Sample 2
    12345678910: {"id": 12345678910,
                  "name": f"My Cool Server",
                  "type": f"Guild",
                  "owner": 111111111,
                  "admin_channel": 222222222,
                  "moderator_role": 333333333,
                  "green": {
                      "emoji": None,
                      "alert": None,
                      "message": f"My green user message has multiple f-string lines! Wow!"
                                 f"Someone in this channel just called :white_check_mark: green "
                                 f":white_check_mark: ; they are good to go.",
                      "admin_message": f"My admin message has two f-string lines."
                                       f"@USER just called :white_check_mark: green in #CHANNEL."},
                  "yellow": {
                      "emoji": f"<:EMOJI_NAME:EMOJI_ID>",
                      "alert": f"A yellow alert!",
                      "message": f"My yellow user message has multiple f-string lines! Wow! "
                                 f"Someone in the channel just called :yellow_square: yellow "
                                 f":yellow_square: ; slow down, take care to be kind and "
                                 f"conscientious, and take a break if you need one.",
                      "admin_message": f"My yellow admin message has multiple f-string lines! Wow!"
                                       f"@USER just called :yellow_square: yellow :yellow_square: "
                                       f"in #CHANNEL. Please check in on them, but only intervene "
                                       f"if the situation escalates."},
                  "red": {
                      "emoji": f"<:EMOJI_NAME:EMOJI_ID>",
                      "alert": f"Red alert!",
                      "message": f"Someone in the channel just called :octagonal_sign: red "
                                 f":octagonal_sign: ;  stop this conversation and take a break. "
                                 f"!MODERATOR_ROLE will pop in shortly to help resolve the situation"
                                 f" if necessary.",
                      "admin_message": f"@USER just called :octagonal_sign: red :octagonal_sign: "
                                       f"in #CHANNEL. Please reply here in #ADMIN_CHANNEL to let "
                                       f"your fellow mods know you'll be the one checking it out, "
                                       f"then head over to #CHANNEL to ensure the code of conduct "
                                       f"is being followed and all members are being respected."}
                  }
}
