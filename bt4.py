import telebot
import json

bot = telebot.TeleBot("8045809996:AAGfi2BQw-jmhHBZPEY5PLcU72ZZIBQC8TA")

fosh2 = "fosh.txt"

# تابع برای ذخیره اطلاعات کاربران در فایل JSON
def save_user_data(user_data):
    try:
        with open('users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    # اضافه کردن کاربر جدید
    users.append(user_data)

    # نوشتن اطلاعات به فایل
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

@bot.message_handler(content_types=['new_chat_members'])
def welcome_to_new_members(message):
    for new_member in message.new_chat_members:
        user_data = {
            "id": new_member.id,
            "first_name": new_member.first_name,
            "last_name": new_member.last_name,
            "username": new_member.username if new_member.username else "N/A",
            "chat_id": message.chat.id
        }
        
        # ذخیره اطلاعات کاربر جدید
        save_user_data(user_data)

        bot.send_message(message.chat.id, f"خوش اومدی به گروه {new_member.first_name}")

@bot.message_handler(regexp="خر")
def regexp_message(message):
    bot.reply_to(message, "حرفی که زدی درست نبود")

# بارگذاری فحش‌ها از فایل و ثبت handler
with open(fosh2, "r", encoding="utf-8") as n:
    fosh = [line.strip() for line in n]

for word in fosh:
    @bot.message_handler(regexp=word)
    def handle_fosh(message):
        bot.reply_to(message, "حرفت بده. بعد از 4 بار اخطار بن میشی")

@bot.message_handler(commands=['admin'])
def get_admin(m):
    try:
        member = bot.get_chat_member(m.chat.id, m.from_user.id)
        print("User Info:", member)
    except Exception as e:
        print(f"Error: {e}")

# شروع به دریافت پیام‌ها
bot.infinity_polling()
