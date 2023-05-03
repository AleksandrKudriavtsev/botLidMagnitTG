import sys
import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.chat_member import ChatMemberLeft

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config. TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Подписаться на канал", url="https://t.me/papateleg"))
    keyboard.add(InlineKeyboardButton("Я уже подписался", callback_data="check_subscription"))
    keyboard.add(InlineKeyboardButton("Хочу такого бота за 5000 рублей", url="https://t.me/aleksandr_kudr"))
    await message.answer("Приветствую! \nЧтобы забрать свой бонус - Инструкцию \n 🎁\"Делаем кнопку в закрепе ТГ\"🎁 \n подпишись на канал, что бы:\n• узнать как применить ботов в бизнесе ,\n• быть свободным от рутинных дел,\n• создавать себе дополнительные часы в сутках! \nТак же этот бот рекламирует сам себя. \nСделаю вам такого же 👇. ", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'check_subscription')
async def check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    chat_member = await bot.get_chat_member(chat_id="@papateleg", user_id=user_id)
    if not isinstance(chat_member, ChatMemberLeft):
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("Забрать подарок 🎁", url="https://telegra.ph/Pin-04-24-2"))
        #keyboard.add(InlineKeyboardButton("Хочу такого бота за 5000 рублей", url="https://t.me/aleksandr_kudr"))
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Спасибо за подписку!\n В благодарность от себя забирай подарок - \n🔥\"Делаем кнопку в закрепе ТГ\"🔥", reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("Подписаться на канал", url="https://t.me/papateleg"))
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Упс.. Вы еще не подписаны на канал. Подпишитесь 👇", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
    
for line in sys.stdin:
    if line.strip() == "exit":
        sys.exit()
