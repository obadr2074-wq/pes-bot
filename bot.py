import telebot

TOKEN = "8625176321:AAEuakDcG1ssjLLZL1lJaee8RTvohQ_g5uM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بيك في بوت PES ⚽\nاكتب /help عشان تشوف الاوامر")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "الاوامر:\n/start - البداية\n/pes - معلومات PES")

@bot.message_handler(commands=['pes'])
def pes(message):
    bot.reply_to(message, "بوت PES شغال تمام ✅")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

print("البوت شغال...")
bot.polling()
