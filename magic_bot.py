import config
import telebot
import random
from telebot import types
import time

bot = telebot.TeleBot(config.token)
answers = ['Бесспорно', 'Даже не думай', 'Мне кажется — «да»', 'Вероятнее всего', 'Спроси позже',
           'Предрешено', 'Пока не ясно, попробуй снова', 'Мой ответ — «нет»', 'Лучше не рассказывать',
           'Никаких сомнений', 'Определённо да', 'По моим данным — «нет»', 'Хорошие перспективы',
           'Можешь быть уверен в этом', 'Перспективы не очень хорошие', 'Знаки говорят — «да',
           'Да', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

variable = ['Секунду...', 'Дай подумаю..', 'Опять???', 'Вам не надоело?', 'Окей, только очки протру']

@bot.message_handler(commands=['start',])
def welcome(message):
    bot.send_message(message.chat.id, text='Введи свой вопрос, и я дам ответ 🔮')


@bot.message_handler(commands=['help',])
def welcome(message):
    bot.send_message(message.chat.id, text='Я - магический-бот предсказатель! Введи /start,'
                                           ' чтобы получить своё пророчество 🔮')

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text == 'Попрощаться':
        bot.send_message(message.chat.id, text='До скорой встречи!', reply_markup=no_markup)
    elif message.text.endswith('?'):
        bot.send_message(message.chat.id, text=random.choice(answers), reply_markup=markup)
    elif message.text == 'Спросить ещё':
        mess = random.choice(variable)
        bot.send_message(message.chat.id, text=mess)
        time.sleep(2)
        if mess == 'Опять???' or mess == 'Вам не надоело?':
            bot.send_message(message.chat.id, text='Ну ладно, вводите свой вопрос')
        else:
            bot.send_message(message.chat.id, text='Хорошо я готов. Вводите свой вопрос')
    else:
        bot.send_message(message.chat.id, text='Хм.. Это мало похоже на вопрос.. Попробуйте ещё раз', reply_markup=markup)



markup = types.ReplyKeyboardMarkup()
markup.row('Спросить ещё', 'Попрощаться')
no_markup = types.ReplyKeyboardRemove()


if __name__ == '__main__':
    bot.polling(none_stop=True)