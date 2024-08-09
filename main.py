import os
from dotenv import load_dotenv
import telebot
from telebot.types import ReactionTypeEmoji

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)

if "BOT_TOKEN" in os.environ:
    print("Check")
else:
    print("Not check")

@bot.message_handler()
def clown_react(message):
    if message.from_user.id == 5566979429:    # To debug, substitute with any id
        print("React")
        bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji("🤡")])
    else:
        text = message.text.lower()
        if ("lotto" in text or "lotti" in text) and ("cerco" in text or "compro" in text) and ("%" in text):
            print("React")
            bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji("🤡")])
        else:
            print("Not react")
            pass
        pass

bot.infinity_polling()