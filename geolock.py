import logging
from multiprocessing.connection import answer_challenge

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5134397524:AAFYIPxTOdnxt_E2V-ZrpeaaSs3HpSLJ19U'

#Configure logging
logging.basicConfig(level=logging.INFO)

# Initialze bot and Dispatche
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def geo(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    await message.reply("Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)


@dp.message_handler(content_types=["location"])
async def location(message: types.Message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        await message.answer("https://www.google.com/search?q=%s+%s" % (message.location.latitude, message.location.longitude))
        
            


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


