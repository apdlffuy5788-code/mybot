import os
import threading
import time
import telebot
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(func=lambda m: True)
def reply(message):
    try:
        bot.reply_to(message, "وصلت رسالتك ✅ البوت شغال")
    except Exception as e:
        print(e)

def run_bot():
    while True:
        try:
            print("Bot started...")
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print("Bot stopped, restarting...", e)
            time.sleep(5)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
