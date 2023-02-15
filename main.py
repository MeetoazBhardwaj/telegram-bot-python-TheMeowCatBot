import telebot  # pip install python-telegram-bot
import meowgif  # to access gif link --> will find an alternative to it so anyone can add gifs
import time


help1 = '''
here are the commands and inline texts 
you can use: 
\hello
\meow
on
bot senses inline texts such as 
dance meow money 

we are making our bot smarter and you can help
by dropping your suggestions, ideas over 
@TheMeowChatBot_Team :)
Thank you!
🦋🍦🌻🖤
'''

# Get you own API_KEY and assign it to this API_KEY variable below to Test your version of this bot
API_KEY = '#############################'
bot = telebot.TeleBot(API_KEY)

start_text = '''
Get ready to bring some furry fun to your Telegram chats with 
our meow bot ! Simply mention the word "meow", and our bot will 
instantly send a cute cat GIF to brighten up your conversation. 
But that's not all - our bot has a few surprises in store for you. 
Try "dance"..."hey" for a playful greeting that will make you feel 
right at home.There are many more surprises waiting for you, 
so get ready to discover them all. With the Meow Bot, 
you'll never have a dull moment in your chats again. 

use /help for more information

Thanks for adding meow bot, 
Cheers to all the furry fun to your conversations!
🦋🍦🌻🖤

note: if you want to learn how to make a bot like this, help us make
this bot better, check out the Github repository created for this bot 
at https://github.com/MeetoazBhardwaj/telegram-bot-python-TheMeowCatBot
Thank you!
'''


# forwards slash + command
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(chat_id=message.chat.id, text=start_text)


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Bello human :)")


@bot.message_handler(commands=['meow'])
def gif(message):
    bot.send_animation(message.chat.id, meowgif.giveMeowGif())


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help1)


@bot.message_handler(content_types=['text'])
# message.from_user.id ---> sends within the bot
# message.chat.id ---> sends in the group

def get_text_messages(message):
    # my functions
    def username_text(text):
        return '@' + message.from_user.username + ' ' + text

    if 'hey' in message.text.lower():
        bot.send_message(message.chat.id, "meow says hey!")
    elif 'miss' in message.text.lower():
        # bot.send_message(message.from_user.id, 'meow misses you too :)')
        bot.send_message(message.chat.id, 'meow misses you too :)')
    elif 'money' in message.text.lower():
        bot.send_animation(message.chat.id, 'https://media.giphy.com/media/ND6xkVPaj8tHO/giphy.gif')
    elif 'dance' in message.text.lower():
        bot.send_animation(message.chat.id, 'https://media.giphy.com/media/1qB3EwE3c54A/giphy.gif')
    elif 'good morning' in message.text.lower():
        bot.send_message(message.chat.id, 'good morning :)')
    elif 'fuck' in message.text.lower():
        bot.send_message(message.chat.id, username_text('used a bad word, me hurt :('))
    elif 'meow' in message.text.lower():
        bot.send_animation(message.chat.id, meowgif.giveMeowGif())
    elif 'sing' in message.text.lower():
        bot.send_message(message.chat.id, username_text("sings meow-meow 🎶"))
    elif 'again' in message.text.lower():
        bot.send_message(message.chat.id, username_text("again? 🙄"))
    elif 'exam' in message.text.lower():
        bot.send_message(message.chat.id, username_text("ʕっ•ᴥ•ʔっ You got this!! 🐝🎶"))



print('Bot Working . . .')
while True:
    try:
        bot.polling()
        print(bot.process_new_messages())
    except Exception:
        time.sleep(10)
