import telebot

def getResult(tests, message, bot):
    Lui = tests[message.from_user.id].end()
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button = telebot.types.KeyboardButton(text="/start")
    keyboard.add(button)
    bot.send_message(message.from_user.id, Lui.name + '\n' + Lui.description, reply_markup=keyboard)
    bot.send_photo(message.from_user.id, Lui.photo)