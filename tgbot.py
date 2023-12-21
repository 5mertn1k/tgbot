import random
import telebot

bot_token = '6774828149:AAGv0BOFdV4-5zgKhAfTIzyvxzysfnDgoVM'  # Здесь нужно указать токен  бота
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, 'Привет! Я загадал число от 1 до 100. Попробуй угадать!')

    # Генерация случайного числа
    secret_number = random.randint(1, 100)

    # Добавляем информацию в хранилище данных бота (чтобы следить за текущим числом)
    bot.data = {}
    bot.data[1] =  secret_number

@bot.message_handler(func=lambda message: True) #указывает, что функция должна быть вызывана для каждого входящего сообщения в чате.
def guess_number(message):
    

    try:
        # Пытаемся преобразовать введенный текст в число
        user_number = int(message.text)
        
        # Получаем текущее загаданное число из хранилища данных бота
        secret_number = bot.data[1]
        
        if user_number == secret_number:
            bot.send_message(message.chat.id, 'Поздравляю, ты угадал число!')
            secret_number = random.randint(1, 100) #после того, как пользователь угадал число, генерируем новое
            bot.data = {}
            bot.data[1] =  secret_number
        elif user_number < secret_number:
            bot.send_message(message.chat.id, 'Загаданное число больше!')
        else:
            bot.send_message(message.chat.id, 'Загаданное число меньше!')
    except ValueError:
        # Если введенное значение невозможно преобразовать в число
        bot.send_message(message.chat.id, 'Пожалуйста, введи число от 1 до 100.')



bot.polling()

