# # کد یوتیوبر 
# import requests

# TOKEN = '8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA'
# url = f'https://api.telegram.org/bot{"8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA"}/deleteWebhook'

# response = requests.get(url)
# print(response.json())


# import telebot
# # Api_key="8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA"
# # bot=telebot.TeleBot(Api_key)
# bot=telebot.TeleBot("8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA")

# @bot.message_handler(commands=['start'])
# def welcome_start(message):
#     bot.send_message(message.chat.id ,"welcome to hastibot")
# @bot.message_handler(commands=["hell"])
# def welcome_start(message):
#     # bot.send_message(message.chat.id ,"hell ok")
#     bot.reply_to(message, "hello not find riply")

# # @bot.

# # bot.polling()
# bot.infinity_polling()

# # pip install TelegramBotAPI











import telebot

bot=telebot.TeleBot("8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA")

@bot.message_handler(content_types=['new_chat_members'])
def welcome_to_new_members(message):
    for new_member in message.new_chat_members:
        bot.send_message(message.chat.id,f"welcome to grop{message}")


@bot.message_handler(regexp="خر")
def regexp_message(message):
    bot.add_deleted_business_messages_handler(message , message.chat.remove)

bot.infinity_polling()
