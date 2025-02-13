import telebot

def getMarkup(bot, message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button = telebot.types.KeyboardButton(text="/start")
    keyboard.add(button)
    bot.send_message(message.from_user.id, "Вы что, не кот что ли, пройдите тест!", reply_markup=keyboard)
    return 