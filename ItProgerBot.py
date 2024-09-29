import telebot
import requests
import webbrowser
import json



API="04f305407680788c341ed9ff92f14a5a"

bot=telebot.TeleBot("7709143061:AAF_7_yHvDCmGUTecn9pF7uuERoVvGzkwQY")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши название города и я скажу тебе погоду")

    bot.register_next_step_handler(message,get_weather)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Я подскажу тебе погоду!")

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open("https://www.hltv.org/")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.strip().lower()
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data=json.loads(res.text)
        temp=data["main"]['temp']
        bot.reply_to(message, f'Сейчас погода {temp}')

    else:
        bot.reply_to(message, "Город указан неверно")

bot.polling(non_stop=True)


