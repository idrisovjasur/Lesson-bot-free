# from aiogram.dispatcher.filters import Text
# from aiogram.types import Message
# from aiogram.types import ContentTypes
# from loader import dp,bot
# from states.holatlar import ALLSTATE
#
# from keyboards.default.keyboard import (bosh_sahifa,berdiyev_j,
#                                         html_1,
#                                         css,
#                                         sass,
#                                         boot,
#                                         java_script,
#                                         jQuery,
#                                         react,
#                                         amalyot)
#
#
# ####Front
#
#
#
#
# @dp.message_handler(Text('CSS3'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=css)
#
#
# @dp.message_handler(Text('Sass'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=sass)
#
#
# @dp.message_handler(Text('Bootstrap4'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=boot)
#
#
# @dp.message_handler(Text('JavaScript & ES6'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=java_script)
#
#
# @dp.message_handler(Text('jQuery'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=jQuery)
#
#
# @dp.message_handler(Text('React'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=react)
#
#
# @dp.message_handler(Text('Amaliyot darslar (html/css)'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=amalyot)
#
# @dp.message_handler(Text('🏠Asosiy Menyu'))
# async def html(message:Message):
#     await message.answer(f"{message.text}",reply_markup=bosh_sahifa)
#
# ####
#
# #######
# @dp.message_handler(Text('Saidbek Arslonov'))
# async def said(message:Message):
#     file = 'BAACAgIAAxkBAAIPhWJgBy7gEw_y1v9aWiZtGhUy11uLAAJ_AwACCuuwS1dDvNva-B7MJAQ'
#     await message.answer_video(file,caption='📹 1 Soatda HTMLni o\'rganamiz')
#
# @dp.message_handler(Text('Berdiyev Javohir'))
# async def said(message:Message):
#     await message.answer(f'{message.text}',reply_markup=berdiyev_j)
#
# @dp.message_handler(Text('1-dars'))
# async def ber(message:Message):
#     file = 'BAACAgIAAxkBAAIPimJgCh2M0Sbxac0h5KFVjJ1-Hf1fAAKkDwACsFqhS_lBNS7e_5tOJAQ'
#     await message.answer_video(file,caption=f"HTML5 1-Dars o\'zbek tilida.HTML haqida.Web dasturlash   Kirish:\n"
#                                             f"Youtube: https://www.youtube.com/watch?v=UyGKgrKgRaM")
#
# @dp.message_handler(Text('2-dars'))
# async def ber(message:Message):
#     file = 'BAACAgIAAxkBAAIPjGJgCp46pZD9Az3mY_WvUgOFKLPmAAKlDwACsFqhS625zmaUpZCXJAQ'
#     await message.answer_video(file,caption=f"HTML5 2-dars (matnlar, img qo'shish, havolalar). Web dasturlash\n"
#                                             f"Youtube: https://www.youtube.com/watch?v=MFfms2VvGUA")
#
# @dp.message_handler(Text('3-dars'))
# async def ber(message:Message):
#     file = 'BAACAgIAAxkBAAIPjGJgCp46pZD9Az3mY_WvUgOFKLPmAAKlDwACsFqhS625zmaUpZCXJAQ'
#     await message.answer_video(file,caption=f"HTML5 3-Dars o'zbek tilida | Web Dasturlash (Formalar, Ro'yxatlar, Jadvalar)\n"
#                                             f"Youtube: https://youtu.be/Dm3GZoqLVF4")
#######



