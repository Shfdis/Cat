import telebot
from Quiz import *
from Question import *
from Cat import *
from questionMarkup import *
from questionWithBack import *
from resultHandler import *
import restartMarkup
from input import *
token = input()
bot = telebot.TeleBot(token)
stage = {}
tests = {}
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    global stage
    global tests
    stage[message.from_user.id] = -2
    stage.update({message.from_user.id : -1})
    tests.update({message.from_user.id : Test()})
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button1 = telebot.types.KeyboardButton(text="я согласен")
    button2 = telebot.types.KeyboardButton(text="я не согласен")
    keyboard.row(button1)
    keyboard.row(button2)
    bot.send_message(message.from_user.id, tests[message.from_user.id].start(), reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global stage
    global tests
    if message.from_user.id not in stage:
        restartMarkup.getMarkup(bot, message)
        return
    if stage[message.from_user.id] == -2:
        restartMarkup.getMarkup(bot, message)
        return
    if stage[message.from_user.id] == -1:
        if message.text == 'я согласен':
            stage.update({message.from_user.id : 0})
            quest = tests[message.from_user.id].ask_question()
            bot.send_message(message.from_user.id, quest.ques, reply_markup=QuestionMarkup(tests, message))
        elif message.text == 'я не согласен':
            keyboard = telebot.types.ReplyKeyboardMarkup()
            bot.send_message(message.from_user.id, "Вы что, не кот что ли, давайте заново", reply_markup=keyboard)
        else:
            keyboard = telebot.types.ReplyKeyboardMarkup()
            bot.send_message(message.from_user.id, "Очепятка, попробуйте ещё раз", reply_markup=keyboard)
    else:
        if tests[message.from_user.id].get_answer(message.text):
            if len(tests[message.from_user.id].questions) - 1 > stage[message.from_user.id]:
                stage[message.from_user.id] += 1
                quest = tests[message.from_user.id].ask_question()
                bot.send_message(message.from_user.id, quest.ques, reply_markup=(QuestionMarkup if stage[message.from_user.id] <= 0 else QuestionWithBack)(tests, message))
            else:
                getResult(tests, message, bot)
                stage[message.from_user.id] = -2
        elif message.text == 'назад':
            tests[message.from_user.id].return_ques()
            quest = tests[message.from_user.id].ask_question()
            bot.send_message(message.from_user.id, quest.ques, reply_markup=(QuestionMarkup if stage[message.from_user.id] <= 0 else QuestionWithBack)(tests, message))
        else:
            keyboard = telebot.types.ReplyKeyboardMarkup()
            bot.send_message(message.from_user.id, "Очепятка, попробуйте ещё раз", reply_markup=keyboard)
            quest = tests[message.from_user.id].ask_question()
            bot.send_message(message.from_user.id, quest.ques, reply_markup=QuestionMarkup(tests, message))
bot.infinity_polling()