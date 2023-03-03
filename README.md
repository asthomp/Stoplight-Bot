# Stoplight-Bot

## Introduction

Stoplight-Bot is a Discord bot that uses the "stoplight system" to facilitate anonymously expressing
discomfort with a given discussion. "Green" means the user is good-to-go and wants to continue. "Yellow"
means the conversation should proceed with care. "Red" means that the conversation should end, full stop.

## Origins

The "stoplight system" is familiar to a lot of people. As kids, we're taught through games that "Red means stop!" and
"Green means go!" It's a simple, familiar, and straightforward system to flag "stop-slow-go." In some online communities, 
the system has increasingly been used to communicate one's boundaries during sensitive discussions - particularly those 
that might impact a user's mental health.

The stoplight system helps users to deepen connections through a mutual respect of eachother's boundaries. Its
goal is not to prevent free-speech but, rather, to ensure that potentially harmful dialogue is tabled for another venue
or time. Essentially, it reminds us to be mindful of others around us so that everyone walks away feeling awesome.

## Features

Stoplight-Bot posts an anonymous announcement to the channel flagged by the command. If configured, it can
also simultaneously post a message to an administrative channel, tagging moderators and alerting them to potentially 
inflammatory discussions. There are three ways to issue a stoplight command: posting a text-based
chat command directly to the channel, using a `/` application command, or accessing a message's context menu.

### Chat Commands

> Users can issue stoplight commands by posting the command directly to a channel.
> The default prefix for stoplight chat commands is `stoplight`
>
> - `stoplight green` signals that a user is good-to-go
>
>
> - `stoplight yellow` signals that the discussion should proceed with care
>
>
> - `stoplight red` signals that the discussion should stop and may flag a moderator
>
> To preserve anonymity, the Stoplight-Bot deletes stoplight commands posted directly to a channel.

### Slash Commands

> If [application commands](https://discord.com/developers/docs/interactions/application-commands) are allowed in
> the channel, users can also type `/green`, `/yellow`, and `/red` to issue
> a stoplight command. Using slash commands helps better preserve anonymity because the command
> can only be seen by the flagging user.
>
> > If users cannot use slash commands, the channel is missing "Application Command" permissions.
> You can learn more about configuring your channels for application commands
> [here](https://support.discord.com/hc/en-us/articles/10543994968087-Channel-Permissions-Settings-101).

### Context Menu Commands

> If [application commands](https://discord.com/developers/docs/interactions/application-commands) are allowed in
> the channel, users can also issue stoplight commands that are targeted at a specific message.
> - Right-click on the target message
> - Select `App`
> - Select the Stoplight-Bot
> - Select a stoplight command
>   - `/green` signals that a user is good-to-go
>   - `/yellow` signals that the discussion should proceed with care
>   - `/red` signals that the discussion should stop and may flag a moderator
>
> > If users cannot see stoplight commands in the `App` context menu, the channel is missing "Application Command"
> > permissions.
> You can learn more about configuring your channels for application commands
> [here](https://support.discord.com/hc/en-us/articles/10543994968087-Channel-Permissions-Settings-101).
>
> If a moderator channel is configured for the bot, message-targeting context menu commands will include
> a direct link to the flagged post. This makes moderation quick and easy.

## Running Stoplight-Bot

### Prerequisite Knowledge

This guide assume that you have little-to-no programming experience. If you're familiar with programming
Discord bots, skim for the details you need and discard the rest! Prior to running Stoplight-Bot, you'll need to
familiarize yourself with the [Discord Developer Portal](https://discord.com/developers/docs/intro) and understand how
to
[create an app](https://discord.com/developers/docs/getting-started#creating-an-app).

### Start the Terminal (Console)

An operating-system (OS) has a Terminal (sometimes called a 'Console') that runs a program called a Shell. Your OS
and Shell combination determine the syntax for various commands. While popular samples are included here, you may
need to do some research to confirm that the commands provided are appropriate for your particular setup.

### Install Python3

From your computer's terminal, check to see whether-or-not [Python3](https://www.python.org) is installed. You can test
this by typing the command `which python3` (Mac/Linux, bash/zsh). If the response indicates that Python3
is not installed, follow the installation instructions [here](https://www.python.org).

You'll need to install Python 3.8 or higher.

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

The project needs several dependencies in order to run. Type `pip install -r requirements.txt` to install the
requirements listed in `requirements.txt`.

You'll need to be able to install [Discord.py version 2.1.0](https://pypi.org/project/discord.py/) for the project to run.

### Setup Bot Credentials

This step assumes that you've created a bot and know its ID and token, which can be found in
the [Discord Developer Portal](https://discord.com/developers/docs/intro). You can learn more
about setting up a bot by reading [this article](https://discord.com/developers/docs/getting-started#creating-an-app).

Feel free to use the following text for the bot's description:

```
Stoplight-Bot lets you anonymously share your comfort level.  
Use `/green` if you're good-to-go, `/yellow` to proceed with 
caution, or `/red` if the conversation should stop. You can see 
a full list of commands with `/`.
```

Open the project up in your favorite file navigator. Then, create a brand-new file in your preferred Python IDE or text
editor. Name the file `.env` and save it in the same folder as `bot.py`. Add your bot's Discord credentials to this
file.
It should look something like this (but with real credentials):

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

You can customize the samples or add a new entry. **Be mindful of the quotes!!** Discord
resource IDs (ex: emoji ids, user ids, channel ids) should not have quotes!

Let's walk through editing the configuration file.

```
    0: {"id": 0,
        "name": f"[YOUR GUILD NAME GOES HERE]]",
        "type": f"Guild",
        "owner": None,
        "admin_channel": None,
        "moderator_role": None,
        ....
```

First, let's add information about our guild. Note that, in the above example, `0` is both the unique key for the guild
object and the actual ID of the guild. Enter *your* Guild ID in as the key and "id". Then, add your guild's name and
put *that* between quotes. If you want, you can add the guild's `owner`, which should also be a numeric ID (no quotes).

Next, let's say we have a private channel named `#moderator_break_room` and, when a stoplight command is used,
we want the bot to post a message in that channel and ping moderators with the role `@Moderator Squad`.
Under `admin_channel`, put the numeric ID of the moderator channel. Under `moderator_role`, put the ID of the role
you want tagged. Here's what our sample would look like after putting in the IDs associated with `@Moderator Squad`
and `#moderator_break_room`.

```
}, 963899072622788700: {"id": 963899072622788700,
        "name": f"My Cool Guild",
        "type": f"Guild",
        "owner": 403657716129857577,
        "admin_channel": 1049215454650060834,
        "moderator_role": 964382007251570688,
        ....

```

Now, let's build some custom messages for our guild.

```
...
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
```

For each color, you can add a custom emoji, alert, user message, and admin message. Remember, admin messages get
posted to the channel specified in `admin_channel`. All messages should be formatted as
[Python f-strings](https://realpython.com/python-f-strings/). You can read more about them by reading
[this article](https://realpython.com/python-f-strings/).

You *can* use `None` in lieu of an alert, emoji, or admin message but the actual message must contain *at
least* one character.

You can also use the following placeholders to reference other Discord resources:

```
    @USER will link to the message's original author.
    #CHANNEL will link to the original message's channel.
    #ADMIN_CHANNEL will link to the channel specified under "admin_channel".
    !MODERATOR_ROLE will tag the role specified under "moderator_role".
```

If you don't want to customize the messages, the bot will automatically use a default message.

### Personalization

Next, open `personalization.py` and skim through its contents. This file lets you personalize the bot and turn them into
a "character" that matches the theme of your Discord Guild. After editing it, the settings you want to use should be
stored in `personalization.py`.

### Review Setup

By this point, you should have downloaded the project, created a virtual environment, and installed the
project's dependencies. In addition, you should have stored your bot's credentials in `.env` and your guild
information in `configuration.py`. You may also have personalized the bot and given them some character using the
`personalization.py` file. Review the instructions one more time and make sure you're happy with these settings.

### Add Bot To Discord Guild

You'll need to add the bot you created in the [Discord Developer Portal](https://discord.com/developers/docs/intro)
to your Discord Guild. Ensure that the bot has all the permissions it needs. We recommend enabling all
`TEXT PERMISSIONS` and the following `GENERAL PERMISSIONS`: `Manage Roles`, `Manage Channels`, `Change Nickname`,
`Manage Nicknames`, `Read Messages/View Channels`, and `Moderate Members`, which include permissions for future
features. If you included a private administration channel in your configuration, you'll also need to make
sure that the bot has permission to post in *that* channel.

### Run Bot

Open your terminal and navigate to the project's folder. Like before, we need to activate the virtual environment
using `$ source venv/bin/activate` (Mac/Linux, bash/zsh) or `C:\> venv\Scripts\activate.bat` (Windows, cmd.exe). Then,
type `python3 bot.py`. After a bit, an announcement should display on the terminal, letting you know that the bot
is live. If you check your guild, the bot should now be online. Make sure all the commands work and, if they do,
you're done.

Congratulations! You installed the Stoplight-Bot.

## Credits

Robbie of BTC came up with the idea for the Stoplight-Bot. The code was written by Aaron Thompson in 2022.

