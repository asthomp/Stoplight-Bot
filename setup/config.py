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

guild_config = {  # Sample 1
    0: {"id": 0,
        "name": f"[YOUR GUILD NAME GOES HERE]]",
        "type": f"Guild",
        "owner": None,
        "admin_channel": None,
        "moderator_role": None,
        "green": {
            "emoji": f"<:EMOJI_NAME:EMOJI_ID>",
            "alert": f"[YOUR ALERT GOES HERE]",
            "message": f"[YOUR TEXT GOES HERE]",
            "admin_message": f"[YOUR ADMIN MESSAGE GOES HERE]"},
        "yellow": {
            "emoji": f"<:EMOJI_NAME:EMOJI_ID>",
            "alert": f"[YOUR ALERT GOES HERE]",
            "message": f"[YOUR TEXT GOES HERE]",
            "admin_message": f"[YOUR ADMIN MESSAGE GOES HERE]"},

        "red": {
            "emoji": f"<:EMOJI_NAME:EMOJI_ID>",
            "alert": f"[YOUR ALERT GOES HERE]",
            "message": f"[YOUR TEXT GOES HERE]",
            "admin_message": f"[YOUR ADMIN MESSAGE GOES HERE]"}
        },
    # Sample 2
    963899072622788700: {"id": 963899072622788700,
                         "name": "Sample Guild",
                         "type": f"Guild",
                         "owner": 403657716129857577,
                         "admin_channel": 1049215454650060834,
                         "moderator_role": 964382007251570688,
                         "green": {
                             "emoji": f"<:green_icon:1051733810800238673>",
                             "alert": "Green!",
                             "message": f"Someone in this channel just called :white_check_mark: green "
                                        f":white_check_mark: ; they are good to go.",
                             "admin_message": f"@USER just called :white_check_mark: green in #CHANNEL."},
                         "yellow": {
                             "emoji": f"<:yellow_icon:1051733853506646067>",
                             "alert": f"Yellow!",
                             "message": f"Someone in the channel just called :yellow_square: yellow "
                                        f":yellow_square: ; slow down, take care to be kind and "
                                        f"conscientious, and take a break if you need one.",
                             "admin_message": f"@USER just called :yellow_square: yellow :yellow_square: "
                                              f"in #CHANNEL. Please check in on them, but only intervene "
                                              f"if the situation escalates."},

                         "red": {
                             "emoji": f"<:red_icon:1051733888113836103>",
                             "alert": f"Red!",
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
