
import telebot

bot=telebot.TeleBot("8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA")

@bot.message_handler(content_types=['new_chat_members'])
def welcome_to_new_members(message):
    for new_member in message.new_chat_members:
        bot.send_message(message.chat.id,f"خوش اومدی به گروه {message.from_user.first_name}")


@bot.message_handler(regexp="خر")
def regexp_message(message):
    bot.reply_to(message, "حرفی که زدی درست نبود")


bot.infinity_polling()

# @bot.message_handler(commands="/hello ")
# def wel_hel_han(message):
#     bot.reply_to(message ,"hi \n baby")

# @bot.message_handler(commands=['admin'])
# def get_admin(m):
#     a=bot.get_chat(chat_id=m.chat.id)
#     print(a)



    
# bot.infinity_polling()