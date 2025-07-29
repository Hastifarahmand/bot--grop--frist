
import telebot

bot=telebot.TeleBot("8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA")

@bot.message_handler(content_types=['new_chat_members'])
def welcome_to_new_members(message):
    for new_member in message.new_chat_members:
        bot.send_message(message.chat.id,f"welcome to grop{message}")


@bot.message_handler(regexp="خر")
def regexp_message(message):
    bot.reply_to(message, "What your saying is not appropriate here.")
bot.infinity_polling()

@bot.message_handler(commands="/hello ")
def wel_hel_han(message):
    bot.reply_to(message ,"hi {message.chat.id}")
@bot.message_handler(content_types=['new_ch'
'at_members'])
@bot.message_handler("chat_id"=CHAT_ID)

def save_member(message):
    for member in  message.new_chat_members:
        bot.