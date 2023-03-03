import random


# Randomly selects an activity that the bot will be "watching," "listening," or "playing."
async def get_random_activity(discord, client, watching, playing, listening):
    activity_choice = random.randint(1, 3)

    if activity_choice == 1:
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=next(watching)))
    elif activity_choice == 2:
        await client.change_presence(
            activity=discord.Game(name=next(playing)))
    else:
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name=next(listening)))
