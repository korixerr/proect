
import random
import telebot

TOKEN = "8241411530:AAGOlZKSmDUcmrHttwgZDJWR_w49WMDVz_I"

bot = telebot.TeleBot(TOKEN)

chars = "abcdefghijklmnopqrstuvwxyz"
chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars += "0123456789"
chars += "!@#$%^&*"

default_length = 12

def make_password(length):
    password = ""
    for i in range(length):
        char = random.choice(chars)
        password += char
    return password

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для паролей.")
    bot.send_message(message.chat.id, "Напиши /generate 1-100, чтобы получить пароль.")

@bot.message_handler(commands=['generate'])
def generate(message):
    try:
        parts = message.text.split()
        if len(parts) > 1:
            length = int(parts[1])
        else:
            length = default_length
    except:
        bot.send_message(message.chat.id, "Ошибка: укажи число после /generate.")
        return

    if length < 1 or length > 100:
        bot.send_message(message.chat.id, "Длина от 1 до 100.")
        return

    pwd = make_password(length)
    bot.send_message(message.chat.id, f"Твой пароль:\n{pwd}")

print("Бот запущен. Ожидание сообщений...")
bot.polling()