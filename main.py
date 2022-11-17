import telebot
from telebot import types, apihelper
import time
import logging
from globals import *
token = '5724247177:AAHqQx7yJY-QHpLTvlS0m0kHJIFZjWKZ6yo'
bot = telebot.TeleBot(token)

apihelper.ENABLE_MIDDLEWARE = True
apihelper.SESSION_TIME_TO_LIVE = 5 * 60

@bot.message_handler(content_types=['text'])
def handler(message):
    try:
        if message.text == '/start':
            globals()[message.chat.id] = list()
            bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name}! I'll help you to register your opportunity.")
            print(message,flush=True)
            print(message.from_user.first_name,flush=True)

            if message.from_user.first_name in globals()['traders']:
                print('Here it is',message, flush=True)

                markup = types.ReplyKeyboardMarkup()
                item1 = types.KeyboardButton("Purchase")
                item2 = types.KeyboardButton("Sale")
                markup.add(item1, item2)

                bot.send_message(message.chat.id, text='Are you going to buy or sell?', reply_markup=markup)

                globals()[message.chat.id].append(message.from_user.first_name)

            if message.from_user.first_name not in globals()['traders']:
                markup1 = types.ReplyKeyboardMarkup()
                for i in globals()['traders']:
                    item = types.KeyboardButton(i)
                    markup1.add(item)

                time.sleep(2)

                bot.send_message(message.chat.id, text='Your name is not in my list of the traders.')
                time.sleep(2)
                bot.send_message(message.chat.id, text='Please select one option:',reply_markup=markup1)

        elif message.text in globals()['traders']:
            markup = types.ReplyKeyboardMarkup()
            item1 = types.KeyboardButton("Purchase")
            item2 = types.KeyboardButton("Sale")
            markup.add(item1, item2)

            bot.send_message(message.chat.id, text='Are you going to buy or sell?', reply_markup=markup)
            globals()[message.chat.id].append(message.text)

        elif message.text in ['Purchase', 'Sale']:
            markup = types.ReplyKeyboardMarkup()
            for i in globals()['match'][globals()[message.chat.id][0]]['C']:
                item = types.KeyboardButton(i)
                markup.add(item)
            bot.send_message(message.chat.id, text='Please enter the name of the country', reply_markup=markup)
            globals()[message.chat.id].append(message.text)

        elif message.text in globals()['countries']:
            markup = types.ReplyKeyboardMarkup()
            for i in globals()['match'][globals()[message.chat.id][0]]['G']:
                item = types.KeyboardButton(i)
                markup.add(item)
            bot.send_message(message.chat.id, text='Please enter the grade', reply_markup=markup)
            globals()[message.chat.id].append(message.text)

        elif message.text in globals()['grades']:
            markup = types.ReplyKeyboardMarkup()
            for i in globals()['terms']:
                item = types.KeyboardButton(i)
                markup.add(item)
            bot.send_message(message.chat.id, text='Please enter the incoterm', reply_markup=markup)
            globals()[message.chat.id].append(message.text)

        elif message.text in globals()['terms']:
            markup = types.ReplyKeyboardMarkup()
            for i in ['MT','ST']:
                item = types.KeyboardButton(i)
                markup.add(item)
            bot.send_message(message.chat.id, text='Please enter amount', reply_markup=markup)
            globals()[message.chat.id].append(message.text)

        elif message.text in ['MT','ST']:
            markup = types.ReplyKeyboardMarkup()
            for i in ['MT/cntr','ST/cntr']:
                item = types.KeyboardButton(i)
                markup.add(item)
            bot.send_message(message.chat.id, text='Please enter the min. payload', reply_markup=markup)
            globals()[message.chat.id].append(message.text)

        elif message.text in ['MT/cntr','ST/cntr']:
            markup = types.ReplyKeyboardMarkup()
            for i in ['EUR','USD']:
                item = types.KeyboardButton(i)
                markup.add(item)
            bot.send_message(message.chat.id, text='Please enter the price', reply_markup=markup)
            globals()[message.chat.id].append(message.text)

        elif message.text in ['USD','EUR']:
            # print('Done',flush=True)

            globals()[message.chat.id].append(message.text)

            # print(globals(), flush=True)
            print(globals()[message.chat.id], flush=True)

            bot.send_message(message.chat.id, text='Your opportunity has been recorded!')

            print(globals()[message.chat.id], flush=True)

            print(globals()[message.chat.id], flush=True)

            msg = f'The new {globals()[message.chat.id][1]} from {globals()[message.chat.id][0]}:\n' \
                  f'Country: {globals()[message.chat.id][2]}\n'\
                  f'Grade: {globals()[message.chat.id][3]}\n'\
                  f'Incoterm: {globals()[message.chat.id][4]}\n'\
                  f'Amount: {globals()[message.chat.id][5]} {globals()[message.chat.id][6]}\n'\
                  f'Min. payload: {globals()[message.chat.id][7]} {globals()[message.chat.id][8]}\n'\
                  f'Price: {globals()[message.chat.id][9]} {globals()[message.chat.id][10]}'

            print(msg, flush=True)
            bot.send_message('@TradingOpportunitiesChanel', text=msg)

            del globals()[message.chat.id]
        elif message.text.isnumeric():
            globals()[message.chat.id].append(message.text)
    except Exception as e:
        print(e)

bot.polling(none_stop=True)

