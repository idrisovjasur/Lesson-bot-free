from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.default.keyboard import bosh_sahifa, qoshimcha_malumotlar_key
from states.holatlar import ALLSTATE
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(Text('Qo\'shimcha bo\'limlar ✨'))
async def front(message:Message):
    await message.answer('Tanlang:',reply_markup=qoshimcha_malumotlar_key)

@dp.message_handler(Text('Web maqolalar'))
async def maq(message:Message):

        await message.answer(f"<b>Domen tanlashda maslahatlar\n"
                             f"Saytni yozib bo'ldingiz, endichi? To'g'ri, uni internetga joylash kerak. "
                             f"Bu uchun esa to'g'ri domen tanlay olishingiz kerak. Quyida asosiy maslahatlar:\n"
                             f"Domen zonasini tanlash"
                             f"Domenlar shartli ravishda 2 turga bo'linadi: geografik joylashuviga qarab (.ru, .uz, .kz); "
                             f"yo'nalishiga qarab (tijoriy saytlar — .com, ta'limiy saytlar — .edu, notijoriy saytlar — .org va h.k)."
                             f"Domen nomi"
                             f"Sayt nomini tanlashda turli belgi va raqamlardan foydalanmang. Ular eslab qolish uchun qiyin. Shuningdek, nom"
                             f" tanlab bo'lganingizdan keyin uni Google dan qidirib ko'ring. Agarda u raqiblaringiz domenidan bitta"
                             f" harf yoki tire bilan farq qilsa unda boshqa variantlarni ko'ring."
                             f"Kompaniya faoliyati yoki brend nomi?"
                             f"Siz saytingizga o'z kompniyangiz faoliyatidan kelib chiqib nom berishingiz mumkin. "
                             f"Masalan, telremont.uz, tashmebel.uz. Kamchiligi, bunday nomlar allaqachon band bo'lishi mumkin."
                             f"2-variant esa bu bevosita brend nomidan foydalanish. Ko'p kompaniyalar shu yo'ldan boradi: samsung.com, toshiba.com, artel.uz. "
                             f"Kamchiligi, boshlang'ich etapda reklama qilish qiyin bo'ladi. Hech kim notanish firmani internetdan qidirmaydi."
                             f"✅ GO</b>")
        file_id = 'AgACAgIAAxkBAAIf3GJk0eoGsdWCH8pyot20R7k1uHr6AAK5uDEbE5ZQScU2RZA9rzmoAQADAgADeAADJAQ'

        await message.answer_photo(file_id,caption='<b>Haqiqiy dasturchi bo\'lish yo\'lida zararli 3 odatdan voz keching'
                                                   '1. Qisqa kod yozishdan voz kechish. Yaxshi dasturchi bo\'lish uchun qisqa kod yozish kerak emas, asosiysi tushunarli kod yozish kerak. Yozgan kodingizni qancha ekanligi muhim emas, muhimi uni boshqalar ham tushinishi kerak.'
                                                   '2. Sharxlar qo\'ymaslikdan voz keching. Sharh ya’ni komentariyalarni tashlab ketsangiz, kodingizni o’qiyotgan odam tushunmasligi mumkin . Ayniqsa katta loyihalarda komentariyasiz kodni tushunish qiyin bo’ladi.' \
                                                     '3. Hech qachon o\'rganishdan voz kechmang. Ko’p yaxshi dasturchilar “Bitta tilni yaxshi o’rganib oldim, menga shu yetadi” deb o’ylashadi. Yo’q! Aslo unday emas. Dasturlash butun Hayot davomida o’rganib, malaka oshirib boriladigan soha</b>')

@dp.message_handler(Text('Web resurslar'))
async def result_def(message:Message):
    file_id = 'BQACAgIAAxkBAAIgLmJk1cIZLM_-IkCxISbkeOk8EHSTAAKYCwAC-a54SPwdPipFTRJ9JAQ'
    await message.answer_document(file_id,caption='Javascript dasturlash tili boʻyicha oʻzbek tilidagi kichik kitob\n'
                                                  'Vosidiy Muslim tomonidan yozilgan Javascript dasturlash tili boʻyicha '
                                                  'fundamental bilimlarni oʻz ichiga olgan oʻzbek tilidagi kitob.')
    id = 'BQACAgIAAxkBAAIgM2Jk1x9aggkkFVQj0s2fuo4-6d2fAAKkDAADfshL8ymEk6GEOJkkBA'
    await message.answer_document(id,caption='💎 Frontendga oid eng yaxshi kitoblar'
                                             'Bugungi postda Frontendga oid o\'zimda bor bo\'lgan eng yaxshi kitoblarni '
                                             'jamlab sizlarga taqdim etmoqchiman. Ushbu zip papkada pullik kitoblar ham mavjud.'
                                             '🗜Zip papkada siz HTML, CSS, JavaScript, Jquery ga oid ingliz va o\'zbek tilidagi kitoblarni topishingiz mumkin bo\'ladi.'
                                             '✅ Ushbu kitoblarni yaqin tanishlaringiz, do\'stlaringiz bilan ham ulashishni unutmang!')

    id1 = 'BQACAgIAAxkBAAIgQGJk16SZIFuqgTN9cG0V5roOgWmQAAJ0CwAC3XXxSMTGmI2kbk87JAQ'
    await message.answer_document(id1,caption='Dasturlash bo\'yicha eng '
                                              'yaxshi saytni endi #Offline ham ishlatsak bo\'ladi. Eng so\'nggi versiyasini #2020')

@dp.message_handler(Text('⬆️Ortga'))
async def ortga(message:Message):
    await message.answer(f"{message.text}",reply_markup=bosh_sahifa)

















# @dp.message_handler(Text('📊 Statistika'))
# async def front(message:Message):
#     await message.answer('Mavjud emas!')
#
# @dp.message_handler(Text('💬 Fikr bildirish'))
# async def fikr(message:Message):
#     await message.answer('Fikrlar qabul qilinmaydi')