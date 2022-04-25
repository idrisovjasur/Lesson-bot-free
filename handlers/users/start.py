from aiogram import types
import asyncpg
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from keyboards.inline.checksub import inline
from data.config import CHANNELS, ADMINS
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.misc.subscribtion import check
from aiogram.types import CallbackQuery
from loader import dp , bot,db
from utils.misc.subscribtion import check
from keyboards.default.keyboard import bosh_sahifa

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username,
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id = message.from_user.id)


    users = await db.count_users()
    msg = f"Bazaga {user[1]} qoshildi , bazada {users} ta odam bor!"

    await bot.send_message(chat_id=ADMINS[0],text=msg)




    text = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        link = await chat.export_invite_link()
        a = f"👉 <a href='{link}'>{chat.title}</a>\n"
        text+= f"<b>Assalomu Alaykum {message.from_user.full_name}" \
               f"\nBotdan to\'liq foydalanish uchun quydagi kanalga obuna bo\'ling\n\n" \
               f"{a}</b>"

        await message.answer(f"{text}",reply_markup=inline, disable_web_page_preview = True)



@dp.callback_query_handler(text = 'obuna')
async def cheak(callback:CallbackQuery):

    await callback.answer()
    text = str()
    for channel in CHANNELS:
        status = await check(user_id=callback.from_user.id,channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            text+= f"<b>✅ {channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
            await callback.message.reply(text,disable_web_page_preview=True)
            await callback.message.answer(f'salom {callback.from_user.get_mention(as_html=True)} botga xush kelibsiz!\n'
                                          f'✅ Botdan to\'liq foydalanishingiz mumkin!',reply_markup=bosh_sahifa)
            # await callback.message.answer_voice('AwACAgIAAxkBAAIZ4GJh-c1DM8JT2gt8R7BNdkBcBijqAAI7EwACZ4MRSy1yw0b6NTYIJAQ',caption='<b>Assalomu Alaykum , hurmatli foydalanuvchi!</b>'

        else:
            link = await channel.export_invite_link()
            text+='<b>❌ Kanalga Obuna Bo\'lmagansiz! Obuna bo\'lish 👇\n\n</b>'
            text+=f"<a href = '{link}'>---->Obuna bo'lish</a>"
            await callback.message.reply(text,disable_web_page_preview=True)




