import telebot
from config import *
from extensions import Converter, APIException
import traceback


bot = telebot.TeleBot(TOKEN) #создаю бота

@bot.message_handler(commands= ['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Что бы начать работу необходимо ввести: \n' \
'-----------------------------------------------------------------------\n' \
'<валюту, цену которой вы хотите узнать>\n' \
'-----------------------------------------------------------------------\n' \
'<валюту, в которой надо узнать цену первой валюты>\n' \
'-----------------------------------------------------------------------\n' \
'<количество первой валюты>\n' \
'-----------------------------------------------------------------------\n' \
'<Например: usd rub 100> <Вводить в одну строку через пробел!>\n' \
'-----------------------------------------------------------------------\n' \
'<Если нужно ввести не целое число, то вводить через точку! Например: 100.5> \n' \
'-----------------------------------------------------------------------\n' \
'Что бы увидеть список доступных валют, введите: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands= ['values'])
def values(message: telebot.types.Message):
    text = 'Список доступных валют:\n'
    for k,v in rate_list.items():
        text = f'{text}\n{k}: {v}'#с каждой строчки пишу новый ключ
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    input_rates = message.text.split()
    try:
        if len(input_rates) != 3:
            raise APIException('Неверное количество параметров!')
        base, quote, amount = input_rates
        result = Converter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка в комаде:\n{e}')
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, result)


bot.polling(none_stop= True)