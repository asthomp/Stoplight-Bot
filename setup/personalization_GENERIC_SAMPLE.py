import random
from itertools import cycle

# Bot Key (Name)
key = "stoplight"

# Command Prefixes - do not remove the " " or you will have a bad time.
prefixes = ["Stoplight ", "stoplight ", "STOPLIGHT "]

# Bot Name Variants - Stoplight-bot can listen for variations in its name.
variants = ["Stoplight", "stoplight", "STOPLIGHT", "Stoplight-bot", "Stoplight-Bot", "stoplight-bot", "STOPLIGHT-BOT"]

# Administrative
ping = f"{key.capitalize()} is live!"

# Sample Bot Description
# This string can be used in the 'Discord Developer Portal' as your bot's description.
sample_bot_description = f"Stoplight-Bot lets you anonymously share your comfort level. " \
                         f"Use `/green` if you're good-to-go, `/yellow` to proceed with " \
                         f"caution, or `/red` if the conversation should stop. You can see " \
                         f"a full list of commands with `/`."

# Activities
watching = cycle(["the road", "for trouble", "paint dry"])
listening = cycle(["Men at Work - Safety Dance", "Rihanna - S&M", "Vintage Culture, Fancy Inc - Cali Dreams"])
playing = cycle(["Stoplight", "w/ a Ouija Board", "it safe", "The-Floor-Is-Lava", "Redlight-Greenlight"])

# Triggers & Responses
compliment_trigger = ['you\'re beautiful', 'love you', 'you are beautiful', 'is beautiful', 'is sexy',
                      'you\'re handsome', 'you\'re so pretty', 'your eyes', 'beautiful eyes',
                      'you\'re so wonderful', 'you\'re wonderful', 'you\'re awesome', 'you are awesome',
                      'you\'re amazing', 'you are amazing', 'so amazing',
                      'pretty mouth', 'is pretty', 'great day', 'nice day',
                      'you\'re amazing']

compliment_response = ['Thank you!.', 'Thanks!', ':heart:', 'That\'s kind of you to say.']

greetings_trigger = [f"hiya, {key}", f"hiya {key}", f"hello, {key}", f"hello {key}", f"hey {key}", f"hey, {key}",
                     f"hi, {key}", f"hi {key}", f"howdy, {key}", f"howdy {key}", f"yo {key}", f"yo {key}"]

greetings_response = ["Hello.", "Hi. Are you drinking enough water?"]

what_trigger = [f"what\'s up, {key}", f"whats up {key}", f"what\'s the word, {key}", f"whats the word, {key}",
                f"what\'s the word {key}", f"whats the word {key}", f"what\'s up, {key}", f"what\'s up {key}",
                f"whats up, {key}", f"whats up {key}", f"what are you doing, {key}", f"what are you doing {key}",
                f"what\'re you doing, {key}", f"what\'re you doing {key}", f"what\'s happening, {key}",
                f"whats happening {key}", f"what\'s going on, {key}", f"what\'s going on {key}",
                f"whatcha doin\', {key}", f"whatcha doin\' {key}", f"whatcha all doin\', {key}",
                f"whatcha all doin\' {key}", f"what are you up to, {key}", f"what are you up to {key}",
                f"what\'re you up to, {key}", f"what\'re you up to {key}"]

what_response = ["Why did the scarecrow get a promotion? He was out standing in his field.", "Why do chicken coops "
                                                                                             "have two doors? Because "
                                                                                             "if they had four, "
                                                                                             "they\'d be chicken "
                                                                                             "sedans."]

how_trigger = [f"how are you, {key}", f"how are you {key}", f"how\'re you, {key}", f"how\'re you {key}",
               f"how are you doing, {key}", f"how are you doing {key}", f"how\'re you doing, {key}",
               f"how\'re you doing {key}", f"how\'re you doin, {key}", f"how\'re you doin\' {key}",
               f"how are you doin, {key}", f"how are you doin\' {key}", f"how\'re you doin {key}",
               f"how\'s it going, {key}", f"how\'s it going {key}", f"hows it going, {key}", f"hows it going {key}",
               f"how\'s your day going, {key}", f"how\'s your day going {key}", f"hows your day going, {key}",
               f"hows your day going {key}", f"how is your day going, {key}", f"how is your day going {key}",
               f"how\'s it going {key}", f"how\'re things going over there, {key}",
               f"how\'re things going over there {key}", f"how are things going over there, {key}",
               f"how are things going over there {key}", f"how is your day goin, {key}", f"how is your day goin {key}",
               f"how\'re things goin over there, {key}", f"how\'re things goin over there {key}",
               f"how are things goin over there, {key}", f"how are things goin over there {key}",
               f"how is your day goin\', {key}", f"how is your day goin\' {key}",
               f"how\'re things goin\' over there, {key}", f"how\'re things goin\' over there {key}",
               f"how are things goin\' over there, {key}", f"how are things goin\' over there {key}",
               f"how you doin {key}", f"how you doin, {key}", f"how you doing {key}", f"how you doing, {key}"]

how_response = ["Wonderful.", "Today is going to be amazing.", "Great! How are you?"]

welcome_trigger = [f"thanks, {key}", f"thanks, {key}.", f"thanks, {key}!", f"thanks {key}",
                   f"thanks {key}.", f"thanks {key}!", f"thank you {key}", f"thank you {key}.", f"thank you {key}!",
                   f"thank you, {key}", f"thank you, {key}.", f"thank you, {key}!"]

welcome_response = ["You\'re very welcome.", "Think nothing of it.", "You\'re welcome.", "You\'re very welcome.",
                    "Of course.", "I suppose you owe me a favor, don\'t you?"]

sorry_trigger = [f"sorry, {key}", f"sorry, {key}.", f"sorry {key}", f"sorry {key}.",
                 f"my bad {key}", f"my bad {key}.", f"my bad, {key}", f"my bad, {key}."]

sorry_response = ["No problem!", "That\'s okay.", "Tomorrow\'s a new day."]
