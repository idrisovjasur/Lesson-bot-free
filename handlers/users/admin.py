from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType
import datetime
from aiogram.types import ReplyKeyboardRemove
from  aiogram.dispatcher.filters import Text

from keyboards.default.backend_keyboard import otmen
from keyboards.default.keyboard import bosh_sahifa
from states.holatlar import ALLSTATE
from data.config import ADMINS
from loader import db , dp , bot
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentTypes
@dp.message_handler(Command('reklama_text'),user_id = ADMINS)
async def reklama(message:Message,state:FSMContext):
    await message.answer("Salom admin!\nText ni kiriting")
    await ALLSTATE.tex_rek.set()

@dp.message_handler(state=ALLSTATE.tex_rek)
async def text_def_rek(message:Message,state:FSMContext):
    text = message.text

    await state.update_data(
        {
            'text':text
        }
    )

    data = await state.get_data()
    text = data.get('text')
    users = await db.select_all_users()

    for user in users:
        id = user[3]
        await bot.send_message(chat_id=id,text=text)

    await state.finish()


# @dp.message_handler(Command('reklama_photo'))
# async def reklama_photo(message:Message):
#     await message.answer("Admin photo yuboring!")
#     await ALLSTATE.photo_rek.set()
#
#
# @dp.message_handler(content_types=ContentTypes.PHOTO,state=ALLSTATE.photo_rek)
# async def photo_reklamaaa(message:Message,state:FSMContext):
#     photo = message.photo[-1].file_id
#     await state.update_data(
#         {
#             'photo':photo
#         }
#     )
#     data = await state.get_data()
#     photo = data.get('photo')
#
#
#     users = await db.select_all_users()
#
#     for user in users:
#         id = user[3]
#
#         await bot.send_photo(photo)
#
#     await state.finish()


@dp.message_handler(Text('📊 Statistika'))
async def statistika(message:Message):

    all_user = await db.count_users()
    data = datetime.datetime.today()

    msg = f"<b>👥 Botdagi obunachilar:  {all_user} ta</b>\n"
    msg+=f"<b>🕖Bugungi sana: {data}</b>\n\n"
    msg+=f"<b>📊 Bot statistikasi</b>"

    await message.answer(msg)
# Command(['myCommand'], ignore_caption=False), content_types=[ContentType.TEXT, ContentType.DOCUMENT]
@dp.message_handler(Text('💬 Fikr bildirish'), content_types=[ContentType.TEXT, ContentType.DOCUMENT,ContentType.VOICE,ContentType.PHOTO])
async def fikr(message:Message):
    await message.answer("<b>Fikringizni bot adminiga yuboraman,\n❗️Muhim xabarlar bilan murojat qiling!</b>",reply_markup=otmen)
    await ALLSTATE.xabar.set()


@dp.message_handler(state=ALLSTATE.xabar)
async def xabar_uchun(message:Message,state:FSMContext):
    if message.text=='🚫Bekor qilish':
        await message.answer(f"{message.text}",reply_markup=bosh_sahifa)
        await state.finish()
    else:
        text = message.text
        await state.update_data(
            {
                'text':text
            }
        )
        data = await state.get_data()
        text = data.get('text')
        text+='\n\n'
        text+=f"@{message.from_user.username} dan xabar!"

        await bot.send_message(chat_id=ADMINS[0],text=text)
        await message.answer("<b>✅ Raxmat! Xabaringiz adminga yuborildi!</b>",reply_markup=bosh_sahifa)

        await state.finish()


