# Description: Based on the total count, converts q unit to its plural form.
def pluralizer(total_count, unit, plural_suffix):
    if total_count == 1:
        return f"{total_count} {unit}"
    else:
        return f"{total_count} {unit}{plural_suffix}"


# Description: Given an input string representing a color, returns the corresponding RGB integer.
# If a color cannot be detected, returns the Discord default color.
def colorizer(input_color):
    discord_default_colors = {
        "DEFAULT": 0,
        "AQUA": 1752220,
        "DARK_AQUA": 1146986,
        "GREEN": 3066993,
        "DARK_GREEN": 2067276,
        "BLUE": 3447003,
        "DARK_BLUE": 2123412,
        "PURPLE": 10181046,
        "DARK_PURPLE": 7419530,
        "LUMINOUS_VIVID_PINK": 15277667,
        "DARK_VIVID_PINK": 11342935,
        "GOLD": 15844367,
        "DARK_GOLD": 12745742,
        "ORANGE": 15105570,
        "DARK_ORANGE": 11027200,
        "RED": 15158332,
        "DARK_RED": 10038562,
        "GREY": 9807270,
        "DARK_GREY": 9936031,
        "DARKER_GREY": 8359053,
        "LIGHT_GREY": 12370112,
        "NAVY": 3426654,
        "DARK_NAVY": 2899536,
        "YELLOW": 16776960,
        "WHITE": 16777215,
        "BLURPLE": 7506394,
        "GREYPLE": 10070709,
        "DARK_BUT_NOT_BLACK": 2895667,
        "NOT_QUITE_BLACK": 2303786,
        "BLACK": 0
    }

    # Integer-formatted RGB color code?
    if input_color.isnumeric() and int(input_color, 10) >= 0:
        return int(input_color, 10)
    # Hex-formatted color code (# or 0x)?
    elif (input_color[0] == '#' and len(input_color) <= 7) or (input_color[0:1] == "0x" and len(input_color) <= 8):
        input_color = input_color.upper()
        input_color = input_color.replace('#', '0x')
        return int(input_color, 16)
    # One of the default discord colors?
    elif input_color.upper() in discord_default_colors.keys():
        return discord_default_colors[input_color.upper()]
    else:
        return discord_default_colors["DEFAULT"]
