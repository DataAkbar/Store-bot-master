
from cgitb import text
import os
from handlers.user.menu import user_menu
from aiogram import executor, types
from utils.set_bot_commands import set_default_commands
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from data import config
from loader import dp, db, bot
from filters import IsAdmin, IsUser
import filters
import logging

filters.setup(dp)

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = '/user'
admin_message = '/admin'
catalog = '🛍️ Каталог'
balance = '💰 Баланс'
cart = '🛒 Сават'
delivery_status = '🚚 Буюртма ҳолати'


# @dp.message_handler(IsAdmin(), commands='start')
# async def cmd_start(message: types.Message):

#     markup = ReplyKeyboardMarkup(resize_keyboard=True)

#     # markup = ReplyKeyboardMarkup(selective=True)
#     markup.add(catalog)
#     markup.add(balance, cart)
#     markup.add(delivery_status)

#     await message.answer('''Салом! 👋

# 🤖 Мен ҳар қандай тоифадаги товарларни сотадиган бот-дўконман.
    
# 🛍️ Каталогга ўтиш ва ўзингизга ёққан маҳсулотларни танлаш учун буйруқдан фойдаланинг.

# 💰 Ҳисобингизни Yandex.kassa, Sberbank  ёки Qiwi орқали тўлдиришингиз мумкин.

# ❓ Саволларингиз борми? Муаммо эмас! /sos буйруғи сизга имкон қадар тезроқ жавоб беришга ҳаракат қиладиган администраторлар билан боғланишга ёрдам беради.
#     ''', reply_markup=markup)


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):

    cid = message.chat.id
    if cid not in config.ADMINS:
        config.ADMINS.append(cid)

    await message.answer('Админ режими ёқилди. /start bo\'sing', reply_markup=ReplyKeyboardRemove())


if config.ADMINS:
    @dp.message_handler(text=user_message)
    async def user_mode(message: types.Message):

        cid = message.chat.id
        if cid in config.ADMINS:
            config.ADMINS.remove(cid)

        await message.answer('User режими ёқилди. /start bo\'sing', reply_markup=ReplyKeyboardRemove())

async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()

    await bot.delete_webhook()
    await bot.set_webhook(config.WEBHOOK_URL)



async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == '__main__':

    if "HEROKU" in list(os.environ.keys()):

        executor.start_webhook(
            dispatcher=dp,
            webhook_path=config.WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )

    else:

        executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
