"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

import settings
import ephem
import datetime

def greet_user(update, context):
    name=update['message']['chat']['first_name']
    username=update['message']['chat']['username']
    print(f'Пользователем {username} вызван /start')
    update.message.reply_text(f"Привет, {name}! Ты вызвал команду /start")


def talk_to_me(update, context):
    user_text = update.message.text 
    name=update['message']['chat']['first_name']
    print(user_text)
    update.message.reply_text(f"{name}! {user_text}")


def get_plannet_constellation(update, context):
    name=update['message']['chat']['first_name']
    username=update['message']['chat']['username']
    print(f'Пользователем {username} вызван /planet')
    user_planet=update.message.text.split()[1].capitalize()
    print(user_planet)
    if hasattr(ephem, user_planet):
        planet=getattr(ephem, user_planet)(datetime.date.today())
        print(planet)
        constellation = ephem.constellation(planet)
        print(constellation)
        update.message.reply_text(f"Привет, {name}! Ты вызвал команду /planet. Ответ: {constellation}")
    else:
        update.message.reply_text(f"Извините, я не знаю такую планету! Попробуйте ещё раз.")

# def get_plannet_constellation(update, context):
#     user_text = update.message.text
#     planet_name = user_text.split()[1].capitalize()
#     if hasattr(ephem, planet_name):
#         planet = getattr(ephem, planet_name)(datetime.now())
#         update.message.reply_text(f"Планета {planet_name} находится в созвездии {ephem.constellation(planet)[1]}")
#     else:
#         update.message.reply_text(f"Извините, я не знаю такую планету! Попробуйте ещё раз.")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_plannet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
