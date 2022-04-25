from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup

inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Obunani tekshirish',callback_data='obuna'),
            InlineKeyboardButton(text='🔜Kanalga o\'tish',url='https://t.me/Oliy_matematika_kanali')
        ]
    ]
)

