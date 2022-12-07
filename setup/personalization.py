import random
from itertools import cycle

# Bot Key (Name)
key = "rowena"

# Command Prefixes - do not remove the " " or you will have a bad time.
# We recommend leaving the default 'stoplight' prefixes in place.
prefixes = ["Rowena ", "rowena ", "ROWENA ", "Stoplight ", "stoplight ", "STOPLIGHT "]

# Bot Name Variants - Stoplight-bot can listen for variations in its name.
variants = ["Rowena", "rowena", "ROWENA", "Queen of Hell", "Rowena MacLeod", "rowena macleod", "Rowena Macleod"]

# Administrative
ping = "Shall we discuss terms?"

# Sample Bot Description
# This string can be used in the 'Discord Developer Portal' as your bot's description.
# Replace {key} with one of the command prefixes for the bot.
sample_bot_description = f"Stoplight-Bot helps users anonymously share their comfort level with a given discussion." \
                         f" Use `{key} green` to say you're good-to-go. Use `{key} yellow` if the " \
                         f"conversation should proceed with caution. Use `{key} red` if the conversation " \
                         f"should end, full stop. You can see a list of commands with `{key} commands`."

# Activities
watching = cycle(["you", "Practical Magic"])
listening = cycle(["ACDC", "screams"])
playing = cycle(["Dream Date", "Ouija Board"])

# Triggers & Responses
compliment_trigger = ['you\'re beautiful', 'love you', 'you are beautiful', 'is beautiful', 'is sexy',
                      'you\'re handsome', 'you\'re so pretty', 'your eyes', 'beautiful eyes',
                      'you\'re so wonderful', 'you\'re wonderful', 'you\'re awesome', 'you are awesome',
                      'you\'re amazing', 'you are amazing', 'so amazing',
                      'pretty mouth', 'is pretty', 'great day', 'nice day',
                      'you\'re amazing']

compliment_response = ['Thank you, dear.', 'You know... no good deed goes unpunished. :devil:', ':heart:',
                       'That\'s kind of you to say.']

greetings_trigger = [f"hiya, {key}", f"hiya {key}", f"hello, {key}", f"hello {key}", f"hey {key}", f"hey, {key}",
                     f"hi, {key}", f"hi {key}", f"howdy, {key}", f"howdy {key}", f"yo {key}", f"yo {key}"]

greetings_response = ["Hello.", "Is that how you address the Queen of Hell?"]

what_trigger = [f"what\'s up, {key}", f"whats up {key}", f"what\'s the word, {key}", f"whats the word, {key}",
                f"what\'s the word {key}", f"whats the word {key}", f"what\'s up, {key}", f"what\'s up {key}",
                f"whats up, {key}", f"whats up {key}", f"what are you doing, {key}", f"what are you doing {key}",
                f"what\'re you doing, {key}", f"what\'re you doing {key}", f"what\'s happening, {key}",
                f"whats happening {key}", f"what\'s going on, {key}", f"what\'s going on {key}",
                f"whatcha doin\', {key}", f"whatcha doin\' {key}", f"whatcha all doin\', {key}",
                f"whatcha all doin\' {key}", f"what are you up to, {key}", f"what are you up to {key}",
                f"what\'re you up to, {key}", f"what\'re you up to {key}"]

what_response = ["Wouldn\'t you like to know?", "I\'m up to no good."]

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

how_response = ["Wonderful.", ":devil:", "Bad girls never tell."]

welcome_trigger = [f"thanks, {key}", f"thanks, {key}.", f"thanks, {key}!", f"thanks {key}",
                   f"thanks {key}.", f"thanks {key}!", f"thank you {key}", f"thank you {key}.", f"thank you {key}!",
                   f"thank you, {key}", f"thank you, {key}.", f"thank you, {key}!"]

welcome_response = ["You\'re very welcome.", "Think nothing of it.", "You\'re welcome.", "You\'re very welcome.",
                    "Of course.", "Anything for a friend of my boys.", "I suppose you owe me a favor, don\'t you?",
                    "That\'s just what *friends* do. Isn\'t it?", "Sign here, on the dotted line."]

sorry_trigger = [f"sorry, {key}", f"sorry, {key}.", f"sorry {key}", f"sorry {key}.",
                 f"my bad {key}", f"my bad {key}.", f"my bad, {key}", f"my bad, {key}."]

sorry_response = ["You should be.", "I know how you can make it up to me.", "I have a little job for you.",
                  "Do you think I\'d hold a grudge?"]
