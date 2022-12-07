# Stoplight-Bot

## Introduction

Stoplight-Bot is a Discord bot that uses the "stoplight system" to facilitate anonymously expressing
discomfort with a given discussion. "Green" means the user is good-to-go and wants to continue. "Yellow"
means the conversation should proceed with care. "Red" means that the conversation should end, full stop.

## Origins

The "stoplight system" has its origins in the BDSM, kink and leather communities. Used as "safewords," the system
allowed partners to quickly communicate their needs during intimacy. This helped improve the physical and
mental health of all involved parties. In adjacent online communities, the stoplight system has increasingly been used
to communicate one's boundaries during sensitive discussions - particularly those that might impact a user's mental
health.

The stoplight system allows users to deepen connections through a mutual respect of eachother's boundaries. Its
goal is not to prevent free-speech but, rather, to ensure that potentially harmful dialogue is tabled for another venue
or time. Essentially, it reminds us to be mindful of others around us so that everyone walks away feeling awesome.

## Features

When a stoplight command is used, the bot will post a message to the channel. To preserve anonymity, it will also delete
the user's original message. If configured, the bot can also simultaneously post a message in an administrative channel,
tagging moderators and alerting them to a potentially inflammatory discussion.

## Running Stoplight-Bot

### Prerequisite Knowledge
This guide assume that you have little-to-no programming experience. If you're familiar with setting up or programming 
Discord bots, skim for the details you need and discard the rest! Prior to running Stoplight-Bot, you'll need to 
familiarize yourself with the [Discord Developer Portal](https://discord.com/developers/docs/intro) and understand how to 
[create an app](https://discord.com/developers/docs/getting-started#creating-an-app). 

### Start the Terminal (Console)

An operating-system (OS) has a Terminal (sometimes called a 'Console') that runs a program called a Shell. Your OS
and Shell combination determine the syntax for various commands. While popular samples are included here, you may
need to do some research to confirm that the commands provided are appropriate for your particular setup.

Terminal
commands will sometimes be labelled like this: `(OS, Shell)`.

### Install Python3

From your computer's terminal, check to see whether-or-not [Python3](https://www.python.org) is installed. You can test
this by typing the command `which python3` (Mac/Linux, bash/zsh). If the response indicates that Python3
is not installed, follow the installation instructions [here](https://www.python.org).

### Download Repository

Secondly, download the project's GitHub repository. This contains all the code and files necessary to run the program.
Unzip the download. Then, drag the folder to your preferred location. Make sure that you're happy with where the
project is and remember this path.

### Setup Virtual Environment

Python3 uses "[virtual environments](https://docs.python.org/3/library/venv.html)" to keep dependencies associated
with a specific project, rather than the global installation of Python3. You can learn more about Python3 virtual
environments [here](https://docs.python.org/3/library/venv.html).

We need to create a virtual environment for Stoplight-Bot. So, open the command terminal and navigate to the folder
that contains the project. If you type `ls` (Mac/Linux, bash/zsh) or `dir`(Windows, cmd.exe) you should see a
file called `bot.py`. That means you're in the right spot.

Create the virtual environment by typing the command `python3 -m venv venv`. Next, activate the virtual
environment by typing the command `$ source venv/bin/activate` (Mac/Linux, bash/zsh) or
`C:\> venv\Scripts\activate.bat` (Windows, cmd.exe). It will automatically launch the virtual environment.

### Install Dependencies

The project needs several dependencies in order to run. Type `pip3 install -r requirements.txt` to install the
requirements listed in `requirements.txt`.

### Setup Bot Credentials

This step assumes that you've created a bot and know its ID and token, which can be found in
the [Discord Developer Portal](https://discord.com/developers/docs/intro). You can learn more
about setting up a bot by reading [this article](https://discord.com/developers/docs/getting-started#creating-an-app).



Feel free to use the following text for the bot's description:

```
Stoplight-Bot lets you anonymously share your comfort level. 
Use `stoplight green` if you're good-to-go, `stoplight yellow` 
to proceed with caution, or `stoplight red` if the conversation 
should stop. You can see a full list of commands with 
`stoplight commands`. 
```

Open the project up in your favorite file navigator. Then, create a brand-new file in your preferred Python IDE or text
editor. Name the file `.env` and save it in the same folder as `bot.py`. Add your bot's Discord credentials to this
file.
It might look something like this:

```
ID="12345"
TOKEN="12345abcd12345myreallylongsecretcode"
```

Save the `.env` file. Then, open it and confirm that your bot's credentials match those found in
the [Discord Developer Portal](https://discord.com/developers/docs/intro).

### Configuration

Next, open the project in your favorite file navigator. Navigate to the `setup` folder. You should see two files:
`config.py` and `personalization.py`. Open `config.py` in your favorite Python IDE or text editor.

This file stores data about your guild and customizes the posts that Stoplight-Bot makes. By default, it posts a
message in the same channel as the source command. It can also be configured to send an additional message to a
private channel used by moderators.

Do not change the "default" guild. Instead, customize the section below it labeled `Better Than Chuck` or add
a new entry. **Be mindful of the quotes!!** Discord resource IDs (ex: emoji ids, user ids, channel ids) should not
have quotes!

Let's walk through editing the configuration file.

```
}, 12345: {"id": 12345,
        "name": f"My Guild Name",
        "type": f"Guild",
        "owner": 1111,
        "admin_channel": None,
        "moderator_role": None,
        ....
```

First, let's add information about our guild. In the above example, `12345` is both the unique key for the guild
object and the actual ID of the guild. Make sure that they're the same number. After the Guild ID, you can add the
guild's name; make sure to put *that* between quotes. You can also add the guild's `owner`, which should be a
numeric ID.

Next, let's say we have a private channel named `#moderators` and, when a stoplight command is used, we want the bot to
post a message in that channel and ping moderators with the role `@Moderator Squad`. Under `admin_channel`, put the ID
for the private moderator channel. Under `moderator_role`, put the ID of the role you want tagged. Here's what our
sample would look like after putting in the IDs associated with `@Moderator Squad` and `#moderators`.

```
}, 12345: {"id": 12345,
        "name": f"My Guild Name",
        "type": f"Guild",
        "owner": 1111,
        "admin_channel": 4322109876543,
        "moderator_role": 6789101112131,
        ....

```

Now, let's build some custom messages for our bots.

```
...
"green": {"emoji": None,
          "alert": None,
          "message": f"Someone in this channel just called :white_check_mark: green "
                     f":white_check_mark: ; they are good to go.",
          "admin_message": f"@USER just called :white_check_mark: green "
                           f":white_check_mark: in #CHANNEL; they are good to go."},
"yellow": {"emoji": f"<:EMOJI_NAME:EMOJI_ID>",
           "alert": f"Slow down!",
           "message": f"Someone in the channel just called :yellow_square: yellow "
                      f":yellow_square: ; slow down, take care to be kind and "
                      f"conscientious, and take a break if you need one.",
           "admin_message": f"@USER just called :yellow_square: yellow :yellow_square: "
                            f"in #CHANNEL. Please check in on them, but only intervene "
                            f"if the situation escalates."},
"red": {"emoji": f"<:EMOJI_NAME:EMOJI_ID>",
        "alert": f"Time out!",
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
```

For each color, you can add a custom emoji, alert, user message, and admin message. Remember, admin messages get
posted to the channel specified in `admin_channel`. All messages should be formatted as
[Python f-strings](https://realpython.com/python-f-strings/). You can read more about them by reading
[this article](https://realpython.com/python-f-strings/).

You *can* use `None` in lieu of an alert, emoji, or admin message but the actual message must contain *at
least* one character.

You can also use the following placeholders other Discord resources:

```
    @USER will link to the message's original author.
    #CHANNEL will link to the original message's channel.
    #ADMIN_CHANNEL will link to the channel specified under "admin_channel".
    !MODERATOR_ROLE will tag the role specified under "moderator_role".
```

If you don't want to customize the messages, the bot will default to the messages set under `default`.

## Personalization

Next, open `personalization.py` and skim through its contents. This file lets you personalize the bot and turn them into
a "character" that matches the theme of your Discord Guild. This is a sample where the bot has been skinned to be
Rowena from the CW's Supernatural. You can also look at `personalization_SAMPLE.py`, which provides a more generic
version of the bot. Whichever one you choose, after editing it, the settings you want to use should be stored in
`personalization.py`.

### Review Setup

By this point, you should have downloaded the project, created a virtual environment, and installed the
project's dependencies. In addition, you should have stored your bot's credentials in `.env` and your guild
information in `configuration.py`. You may also have personalized the bot and given them some character using the
`personalization.py` file. Review the instructions one more time and make sure you're happy with these settings.

### Add Bot To Discord Guild

You'll need to add the bot you created in the [Discord Developer Portal](https://discord.com/developers/docs/intro)
to your Discord Guild. Ensure that the bot has all `TEXT PERMISSIONS` and the following `GENERAL PERMISSIONS`:
`Manage Roles`, `Manage Channels`, `Change Nickname`, `Manage Nicknames`, `Read Messages/View Channels`,
and `Moderate Members`. If you included a private administration channel in your configuration, you'll need to make
sure that the bot has permission to post in that channel.

### Run Bot

Open your terminal and navigate to the project's folder. Like before, we need to activate the virtual environment
using `$ source venv/bin/activate` (Mac/Linux, bash/zsh) or `C:\> venv\Scripts\activate.bat` (Windows, cmd.exe). Then,
type `python3 bot.py`. After a bit, an announcemnet should display on the terminal, letting you know that the bot 
is live. If you check your guild, the bot should now be online. Make sure all the commands work and, if they do, 
you're done.

Congratulations! You installed the Stoplight-Bot.

## Credits

Robbie of BTC came up with the idea for the Stoplight-Bot. The code was written by Aaron Thompson in 2022.

