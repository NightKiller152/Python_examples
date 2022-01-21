#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types
from configs import User, surnames, insert_in_db, chatid, add_id, names, categories, send_email

TOKEN = "bot_token"
bot = telebot.TeleBot(TOKEN)

problem = []
chatids = []


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not User.isRunning:
        chat_id = message.chat.id
        if chat_id in chatid:
            Surname = chatid[chat_id]
            Name = names[Surname]
            msg = bot.send_message(message.chat.id, 'Здравствуйте, ' + Name + '!')
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            for category in categories:
                markup.add(category)
            msg = bot.reply_to(message, 'Выберите категорию проблемы:', reply_markup=markup)
            bot.register_next_step_handler(msg, askProblem)
            problem.append(Surname)
            return markup
        else:
            msg = bot.send_message(message.chat.id, 'Здравствуйте, введите фамилию!')
            bot.register_next_step_handler(msg, askSurname)



def askSurname(message):
    chat_id = message.chat.id
    us_sname = message.text.capitalize()
    if us_sname in surnames:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Техника', 'ПО', 'Сеть', 'Другое')
        msg = bot.reply_to(message, 'Выберите категорию проблемы:', reply_markup=markup)
        bot.register_next_step_handler(msg, askProblem)
        problem.append(us_sname)
        chatids.append(chat_id)
        chatids.append(us_sname)
        add_id(chatids)
        return markup

    else:
        bot.send_message(chat_id, 'Вас нет в списке, проверьте правильность введенной фамилии!')
        bot.register_next_step_handler(message, askSurname)

    return message.text


def askProblem(message):
    chat_id = message.chat.id
    us_cat = message.text
    problem.append(us_cat)
    markup = types.ReplyKeyboardRemove(selective=True)
    msg = bot.send_message(message.chat.id, 'Опишите вашу проблему!', reply_markup=markup)
    bot.register_next_step_handler(msg, end)


def end(message):
    chat_id = message.chat.id
    desc = message.text
    msg = bot.send_message(message.chat.id, 'Спасибо за обращение! В ближайшее время мы решим вашу проблему!\nДля создания новой заявки напишите /start')
    problem.append(desc)
    send_email(problem)
    print(problem)
    insert_in_db(problem)
    problem.clear()


bot.polling(none_stop=True, interval=0)
