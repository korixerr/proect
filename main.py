import telebot
from telebot import apihelper

# Настройка таймаутов (на случай блокировки)
apihelper.CONNECT_TIMEOUT = 30
apihelper.READ_TIMEOUT = 30

# Ваш токен
TOKEN = "8241411530:AAFqYxL-JKhZyplJapbJ0_0l8O1r1IQ2dzg"

# Создание бота
bot = telebot.TeleBot(TOKEN)

# Проверка, что токен работает
try:
    bot_info = bot.get_me()
    print(f"Бот успешно запущен: @{bot_info.username}")
except Exception as e:
    print(f"Ошибка: {e}")
    exit(1)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Бот работает!")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)