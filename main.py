import telebot
from telebot import types
import time
import logging
from globals import *
token = '5724247177:AAHqQx7yJY-QHpLTvlS0m0kHJIFZjWKZ6yo'
bot = telebot.TeleBot(token)

def handler(message):
    if message['text'] == '/start':
        globals()[message['id']] = list()
        bot.send_message(message['id'], f"Hi, {message['from']}! I'll help you to register your opportunity.")
        print(message,flush=True)
        print(message['from'],flush=True)

        if message['from'] in globals()['traders']:
            print('Here it is',message, flush=True)

            markup = types.ReplyKeyboardMarkup()
            item1 = types.KeyboardButton("Purchase")
            item2 = types.KeyboardButton("Sale")
            markup.add(item1, item2)

            bot.send_message(message['id'], text='Are you going to buy or sell?', reply_markup=markup)

            globals()[message['id']].append(message['from'])

        if message['from'] not in globals()['traders']:
            markup1 = types.ReplyKeyboardMarkup()
            for i in globals()['traders']:
                item = types.KeyboardButton(i)
                markup1.add(item)

            time.sleep(2)

            bot.send_message(message['id'], text='Your name is not in my list of the traders.')
            time.sleep(2)
            bot.send_message(message['id'], text='Please select one option:',reply_markup=markup1)

    elif message['text'] in globals()['traders']:
        markup = types.ReplyKeyboardMarkup()
        item1 = types.KeyboardButton("Purchase")
        item2 = types.KeyboardButton("Sale")
        markup.add(item1, item2)

        bot.send_message(message['id'], text='Are you going to buy or sell?', reply_markup=markup)
        globals()[message['id']].append(message['text'])

    elif message['text'] in ['Purchase', 'Sale']:
        markup = types.ReplyKeyboardMarkup()
        for i in globals()['match'][globals()[message['id']][0]]['C']:
            item = types.KeyboardButton(i)
            markup.add(item)
        bot.send_message(message['id'], text='Please enter the name of the country', reply_markup=markup)
        globals()[message['id']].append(message['text'])

    elif message['text'] in globals()['countries']:
        markup = types.ReplyKeyboardMarkup()
        print('Done',message['text'],flush=True)
        for i in globals()['match'][globals()[message['id']][0]]['G']:
            item = types.KeyboardButton(i)
            markup.add(item)
        bot.send_message(message['id'], text='Please enter the grade', reply_markup=markup)
        globals()[message['id']].append(message['text'])

    elif message['text'] in globals()['grades']:
        markup = types.ReplyKeyboardMarkup()
        for i in globals()['terms']:
            item = types.KeyboardButton(i)
            markup.add(item)
        bot.send_message(message['id'], text='Please enter the incoterm', reply_markup=markup)
        globals()[message['id']].append(message['text'])

    elif message['text'] in globals()['terms']:
        markup = types.ReplyKeyboardMarkup()
        for i in ['MT','ST']:
            item = types.KeyboardButton(i)
            markup.add(item)
        bot.send_message(message['id'], text='Please enter amount', reply_markup=markup)
        globals()[message['id']].append(message['text'])

    elif message['text'] in ['MT','ST']:
        markup = types.ReplyKeyboardMarkup()
        for i in ['MT/cntr','ST/cntr']:
            item = types.KeyboardButton(i)
            markup.add(item)
        bot.send_message(message['id'], text='Please enter the min. payload', reply_markup=markup)
        globals()[message['id']].append(message['text'])

    elif message['text'] in ['MT/cntr','ST/cntr']:
        markup = types.ReplyKeyboardMarkup()
        for i in ['EUR','USD']:
            item = types.KeyboardButton(i)
            markup.add(item)
        bot.send_message(message['id'], text='Please enter the price', reply_markup=markup)
        globals()[message['id']].append(message['text'])

    elif message['text'] in ['USD','EUR']:
        # print('Done',flush=True)

        globals()[message['id']].append(message['text'])

        # print(globals(), flush=True)
        print(globals()[message['id']], flush=True)

        bot.send_message(message['id'], text='Your opportunity has been recorded!')

        print(globals()[message['id']], flush=True)

        print(globals()[message['id']], flush=True)

        msg = f'The new {globals()[message["id"]][1]} from {globals()[message["id"]][0]}:\n' \
              f'Country: {globals()[message["id"]][2]}\n'\
              f'Grade: {globals()[message["id"]][3]}\n'\
              f'Incoterm: {globals()[message["id"]][4]}\n'\
              f'Amount: {globals()[message["id"]][5]} {globals()[message["id"]][6]}\n'\
              f'Min. payload: {globals()[message["id"]][7]} {globals()[message["id"]][8]}\n'\
              f'Price: {globals()[message["id"]][9]} {globals()[message["id"]][10]}'

        print(msg, flush=True)
        bot.send_message('@TradingOpportunitiesChanel', text=msg)

        del globals()[message['id']]
    elif message['text'].isnumeric():
        globals()[message['id']].append(message['text'])

# bot.polling(none_stop=True)

