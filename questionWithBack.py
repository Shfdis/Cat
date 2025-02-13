from questionMarkup import *
class QuestionWithBack(QuestionMarkup):
    def __init__(self, tests, message):
        super().__init__(tests, message)
        keyboard = telebot.types.ReplyKeyboardMarkup()
        button1 = telebot.types.KeyboardButton(text="назад")
        self.row(button1)
