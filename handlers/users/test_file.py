from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.types import ContentTypes
from loader import dp,bot

@dp.message_handler(content_types=ContentTypes.TEXT)
async def i(m:Message):
    await m.answer("<b>❌Mavjud bo'lmagan buyruq!</b>")
# @dp.message_handler(content_types=ContentTypes.VIDEO)
# async def r(m:Message):
#     au = m.video.file_id
#     await m.answer(au)