import telebot
class QuestionMarkup(telebot.types.ReplyKeyboardMarkup):
    def __init__(self, tests, message):
        super().__init__()
        quest = tests[message.from_user.id].ask_question()
        for i in quest.answers:
            button = telebot.types.KeyboardButton(text = i.ans)
            self.row(button)
