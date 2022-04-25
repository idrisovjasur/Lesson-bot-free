from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.default.keyboard import bosh_sahifa
from states.holatlar import ALLSTATE
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.english_keyboard import english, bigenner_key,call_uzb_key,intermedet_key,elementry_key


@dp.message_handler(Text('English'))
async def front(message:Message):
    await message.answer('👨‍💻Quydagi darslarni birini tanlang',reply_markup=english)
    await ALLSTATE.english.set()

@dp.message_handler(state=ALLSTATE.english)
async def english_def(message:Message,state:FSMContext):
    if message.text=='Beginner':
        await message.answer(f"{message.text}",reply_markup=bigenner_key)
        await ALLSTATE.bigenner.set()

    elif message.text=='Elementary':
        await message.answer(f"{message.text}",reply_markup=elementry_key)
        await ALLSTATE.elementary.set()

    elif message.text=='Intermediate':
        await message.answer(f"{message.text}",reply_markup=intermedet_key)
        await ALLSTATE.intermedet.set()

    elif message.text=='Co-learning(UZB)':
        await message.answer(f"{message.text}",reply_markup=call_uzb_key)
        await ALLSTATE.call_uzb.set()

    elif message.text=='⬆️Ortga':
        await message.answer(f'{message.text}',reply_markup=bosh_sahifa)
        await state.finish()

@dp.message_handler(state=ALLSTATE.bigenner)
async def def_bigenner_state(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIexGJkwhC6GWOhrm8CSMjx26XiiQZmAAL7BQACR9ywRZH6oPEf7J_qJAQ'
        await message.answer_video(file_id,caption='01 - Beginner Levels - Lesson 1 - Nice To Meet You!.mp4 ')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIexmJkwi5InrDGlLxc35M-WyUkm-TuAAL8BQACR9ywRUS9ioSWO5prJAQ'
        await message.answer_video(file_id,caption='📹02 - Beginner Levels - Lesson 2 - How Are You.mp4 ')
    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIeyGJkwlPF50kQwJAYOpVzVJ4eFT1SAAL9BQACR9ywRTb-ozyHFOw_JAQ'
        await message.answer_video(file_id,caption='📹03 - Beginner Levels - Lesson 3 - What does she look like.mp4 ')
    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIeymJkwnDl1LrjTtTpUT1REUZON92dAAL-BQACR9ywRdDudC7Q4cbBJAQ'
        await message.answer_video(file_id,caption='📹04 - Beginner Levels - Lesson 4 - Where are you from.mp4 ')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIezGJkwo-U8CgwphS43fjENauwLjPSAAL_BQACR9ywRZy73NaGER0LJAQ'
        await message.answer_video(file_id,caption='📹 BAACAgEAAxkBAAIezGJkwo-U8CgwphS43fjENauwLjPSAAL_BQACR9ywRZy73NaGER0LJAQ ')

    elif message.text=='6-dars':
        file_id = 'BAACAgEAAxkBAAIezmJkwroiqAbeNPGHmqMFEuIsuVHEAAMGAAJH3LBFr4nbfzaV3vAkBA'
        await message.answer_video(file_id,caption='📹 06 - Beginner Levels - Lesson 6 - My Family.mp4 ')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIe0GJkwtPqZ8hEf-n67DXtW4CItgaRAAIBBgACR9ywRXPBycWjn8QeJAQ'
        await message.answer_video(file_id,caption='📹 07 - Beginner Levels - Lesson 7 - These are my relatives.mp4')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIe0mJkwvSw1D4AAbOsHv3qPdd87cPWigACAgYAAkfcsEVyxOkGcEkb2iQE'
        await message.answer_video(file_id,caption='📹08 - Beginner Levels - Lesson 8 - What do you do.mp4 ')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIe1GJkwxFfLj-_TN9MTQXiLW6Pusj3AAIDBgACR9ywRUO1QlHkhftXJAQ'
        await message.answer_video(file_id,caption='📹09 - Beginner Levels - Lesson 9 - Where do you work.mp4 ')
    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIe1mJkwy7ZM1X_lqsvB-iRO4HD8X7-AAIEBgACR9ywRZ2taLYPWF1KJAQ'
        await message.answer_video(file_id,caption='📹10 - Beginner Levels - Lesson 10 - What time is it.mp4 ')
    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIe2GJkw0ozu7de6wd_7UR9GQozdf4rAAIFBgACR9ywRbxOXEUQLDfaJAQ'
        await message.answer_video(file_id,caption='📹 11 - Beginner Levels - Lesson 11 - What day is it.mp4 ')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIe2mJkw2WQ4UsPNaoYX9kV86GEXXDOAAIGBgACR9ywRVEMF5uYxLwEJAQ'
        await message.answer_video(file_id,caption='📹 12 - Beginner Levels - Lesson 12 - How is the weather.mp4')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIe3GJkw4DdW9bZCz1fHzOZJiw049hzAAIHBgACR9ywRSxm3Pd3c3__JAQ'
        await message.answer_video(file_id,caption='📹13 - Beginner Levels - Lesson 13 - What are you wearing.mp4 ')

    elif message.text=='14-dars':
        file_id = 'BAACAgEAAxkBAAIe3mJkw5vvyCY5bw5dfjQ3U5w-m6ldAAIIBgACR9ywRRCebPczY6AZJAQ'
        await message.answer_video(file_id,caption='📹14 - Beginner Levels - Lesson 14 - The Body.mp4')

    elif message.text=='15-dars':
        file_id = 'BAACAgEAAxkBAAIe4GJkw7iEk3twUEESG2QTsR1aWyjsAAIJBgACR9ywRQNZczypFxgYJAQ'
        await message.answer_video(file_id,caption='📹 15 - Beginner Levels - Lesson 15 - What\'s the matter.mp4 ')

    elif message.text=='16-dars':
        file_id = 'BAACAgEAAxkBAAIe4mJkw9lRiVxD3pbcUpiYjoQxuCk2AAIKBgACR9ywRWAdyxl1FGf6JAQ'
        await message.answer_video(file_id,caption='📹16 - Beginner Levels - Lesson 16 - Home sweet home.mp4  ')

    elif message.text=='17-dars':
        file_id = 'BAACAgEAAxkBAAIe5GJkw_bnj911ZLLVcgvTR9iXN3O3AAILBgACR9ywRfudMioPtXPcJAQ'
        await message.answer_video(file_id,caption='📹17 - Beginner Levels - Lesson 17 - Tell me about your furniture.mp4 ')

    if message.text=='18-dars':
        file_id = 'BAACAgEAAxkBAAIe5mJkxBn5C7Y6c7hQ1p-sMTK-HWj4AAIMBgACR9ywRVWzf7fGA24xJAQ'
        await message.answer_video(file_id,caption='📹18 - Beginner Levels - Lesson 18 - I\'m Hungry.mp4')

    elif message.text=='19-dars':
        file_id = 'BAACAgEAAxkBAAIe6GJkxDv2_JXDEce7hAheKx-bgUAVAAINBgACR9ywRbx-DaOx6TP3JAQ'
        await message.answer_video(file_id,caption='📹 19 - Beginner Levels - Lesson 19 - What sports can you play.mp4')
    elif message.text=='20-dars':
        file_id = 'BAACAgEAAxkBAAIe6mJkxFR57S1V9pHDByR8_I47L8nSAAIOBgACR9ywRdD5L2qKGDINJAQ'
        await message.answer_video(file_id,caption='📹 20 - Beginner Levels - Lesson 20 - What did you do yesterday.mp4')
    elif message.text=='21-dars':
        file_id = 'BAACAgEAAxkBAAIe7GJkxGzzCrtrL8JiYvkzKwE2p3iEAAIPBgACR9ywRdqO52G8HfYFJAQ'
        await message.answer_video(file_id,caption='📹21 - Beginner Levels - Lesson 21 - What are you going to do.mp4')

    elif message.text=='22-dars':
        file_id = 'BAACAgEAAxkBAAIe7mJkxI7KtpInBwaBiXTIduweTpQ-AAIQBgACR9ywRd-R2SDk99ORJAQ'
        await message.answer_video(file_id,caption='📹 22 - Beginner Levels - Lesson 22 - Would you like to go.mp4')

    elif message.text=='23-dars':
        file_id = 'BAACAgEAAxkBAAIe8GJkxK6aHhbRZ0bod1wwKvdRDclJAAIRBgACR9ywRXwMO45SzlauJAQ'
        await message.answer_video(file_id,caption='📹23 - Beginner Levels - Lesson 23 - My Vacation.mp4')

    elif message.text=='24-dars':
        file_id = 'BAACAgEAAxkBAAIe8mJkxNh6WXp-63c17n2iCXn-j5u1AAISBgACR9ywRcLLTLXIgvCkJAQ'
        await message.answer_video(file_id,caption='📹 24 - Beginner Levels - Lesson 24 - How do you travel.mp4 ')

    elif message.text=='25-dars':
        file_id = 'BAACAgEAAxkBAAIe9GJkxPZZ--ChixnQxM5Y_Nx6Mcl2AAITBgACR9ywRShn2pVnvB8IJAQ'
        await message.answer_video(file_id,caption='📹 25 - Beginner Levels - Lesson 25 - How do you get there.mp4')

    elif message.text=='26-dars':
        file_id = 'BAACAgEAAxkBAAIe9mJkxROhHZWpqN7wOgtyvSin-dL4AAIUBgACR9ywRWEdPcrWBpwLJAQ'
        await message.answer_video(file_id,caption='📹26 - Beginner Levels - Lesson 26 - Ask Me A Question.mp4 ')

    elif message.text=='27-dars':
        file_id = 'BAACAgEAAxkBAAIe-GJkxTUL7VaE7JsV0HSmbyv46gQDAAIVBgACR9ywRUmkJxcC42kgJAQ'
        await message.answer_video(file_id,caption='📹 27 - Beginner Levels - Lesson 27 - I don\'t know.mp4 ')

    elif message.text=='28-dars':
        file_id = 'BAACAgEAAxkBAAIe-mJkxVciIr7-owulL39wtQP57jVQAAIWBgACR9ywRWhKlrBVcV24JAQ'
        await message.answer_video(file_id,caption='📹 28 - Beginner Levels - Lesson 28 - Review (Lesson 1 to 9).mp4 ')


    elif message.text=='⬆️Ortga':
        await ALLSTATE.english.set()
        await message.answer(f"{message.text}",reply_markup=english)

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=-f54HjaFp4w'>LINK</a></b>")

@dp.message_handler(state=ALLSTATE.elementary)
async def element_def(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIhMmJk8sAng1rsta0wZZ8VlOUDB9zHAAKYAQACqWe5RcDioYJiWmAwJAQ'
        await message.answer_video(file_id,caption='01 - Elementary Levels - Lesson 1 - Welcome.mp4')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIhNGJk8w4GUC_3zuJEIv-hFOfY4aiGAAKZAQACqWe5Rdm5r2yE8P_oJAQ'
        await message.answer_video(file_id,caption='02 - Elementary Levels - Lesson 2 - Special Days.mp4')

    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIhNmJk81V1Uw4_IzZSOvgXJhvGzuDlAAKaAQACqWe5RVHeEhX7iyApJAQ'
        await message.answer_video(file_id,caption='03 - Elementary Levels - Lesson 3 - Entertaining.mp4')

    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIhOGJk824SiINDOOcYojKUPjxZ8qPqAAKbAQACqWe5RYv1_VL2-u_yJAQ'
        await message.answer_video(file_id,caption='04 - Elementary Levels - Lesson 4 - School Days.mp4')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIhOmJk84dohfZn96ggwA99GsavmCY3AAKcAQACqWe5RTXGdGaVsmMOJAQ'
        await message.answer_video(file_id,caption='05 - Elementary Levels - Lesson 5 - Where is it.mp4')

    elif message.text=='6-dars':
        file_id = 'BAACAgEAAxkBAAIhPGJk88lxk1cangujkH_KTBGxmUrHAAKdAQACqWe5ReobrlWiRBkRJAQ'
        await message.answer_video(file_id,caption='06 - Elementary Levels - Lesson 6 - Shopping.mp4')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIhPmJk8_bF25jiGwKN1m6Dm6YCItOuAAKeAQACqWe5RS_O3N7I2JolJAQ'
        await message.answer_video(file_id,caption='07 - Elementary Levels  - Lesson 7 - For me.mp4')

   # elif message.text=='CSS Asoslari':
    #    file_id = 'BAACAgIAAxkBAAITa2JhFjJOR36axrMy9e_rLNFB0uaBAAJyBgACvvmQSg9lWWq2dQkeJAQ'
    #    await message.answer_video(file_id,caption='📹 CSS Asoslari ')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIhQGJk9CqN7dY4O6tqz7Ri1kitm2AnAAKfAQACqWe5Rcwu-j5m2BYmJAQ'
        await message.answer_video(file_id,caption='08 - Elementary Levels - Lesson 8 - Activities.mp4')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIhQmJk9ENgN99H7xoTqTLqfXG_W2EiAAKgAQACqWe5RQgLy5HTno8mJAQ'
        await message.answer_video(file_id,caption='09 - Elementary Levels - Lesson 9 - Listen to the music.mp4')

    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIhRGJk9F5F_eWl-D5zaVbdHuTU9dtRAAKhAQACqWe5RevtPnzxG-a_JAQ'
        await message.answer_video(file_id,caption='10 - Elementary Levels - Lesson 10 - What\'s For Dinner.mp4')

    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIhRmJk9Hz5ZVpM3cJSkCb27TpQZZFkAAKiAQACqWe5RY2rPptp_vUaJAQ'
        await message.answer_video(file_id,caption='11 - Elementary Levels - Lesson 11 - He is taller than I am.mp4')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIhSGJk9KCVLpd4hC33y71eGmNABlLjAAKjAQACqWe5RWaFe17MkV7EJAQ'
        await message.answer_video(file_id,caption='12 - Elementary Levels - Lesson 12 - What is the tallest mountain.mp4')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIhSmJk9LgQg-hetWsMmH2bN5enIaiLAAKkAQACqWe5RalNcZiIOJL6JAQ'
        await message.answer_video(file_id,caption='13 - Elementary Levels - Lesson 13 - At Home.mp4')

    elif message.text=='14-dars':
        file_id = 'BAACAgEAAxkBAAIhTWJk9Ncloh6rlcSXyDm6YxBhC_fxAAKlAQACqWe5RVhERmq0F9kCJAQ'
        await message.answer_video(file_id,caption='14 - Elementary Levels - Lesson 14 - At The Station.mp4')

    elif message.text=='15-dars':
        file_id = 'BAACAgEAAxkBAAIhaGJk9Tjnh2a_nAVrYg6z_DPhpujjAAKmAQACqWe5RVkc88m5qP5LJAQ'
        await message.answer_video(file_id,caption='15 - Elementary Levels - Lesson 15 - Do This.mp4')

    elif message.text=='16-dars':
        file_id = 'BAACAgEAAxkBAAIhc2Jk9VdfrzyqyNVYfxhkEAMB2L5nAAKnAQACqWe5RSQtwVRZYLh1JAQ'
        await message.answer_video(file_id,caption='16 - Elementary Levels - Lesson 16 - Past Experiences.mp4')

    elif message.text=='17-dars':
        file_id = 'BAACAgEAAxkBAAIhgmJk9YE5YiX9ihg5lAvFHSduYA60AAKoAQACqWe5Rbn5e10F8mu-JAQ'
        await message.answer_video(file_id,caption='17 - Elementary Levels - Lesson 17 - Future Life.mp4')

    if message.text=='18-dars':
        file_id = 'BAACAgEAAxkBAAIhi2Jk9Z9vVeSq29ET28dEO-i94axvAAKpAQACqWe5RehGPAEV6ojKJAQ'
        await message.answer_video(file_id,caption='18 - Elementary Levels - Lesson 18 - I Wish Upon A Star.mp4')

    elif message.text=='19-dars':
        file_id = 'BAACAgEAAxkBAAIhjWJk9caK1U8AAeJ9oIHu6FNP-YhMJwACqgEAAqlnuUXL0AWn361UaCQE'
        await message.answer_video(file_id,caption='19 - Elementary Levels - Lesson 19 - World Knowledge.mp4')

    elif message.text=='20-dars':
        file_id = 'BAACAgEAAxkBAAIhkGJk9eToxbKGj5CUntdhSobhGCvuAAKrAQACqWe5ReX5VAcgmsIPJAQ'
        await message.answer_video(file_id,caption='20 - Elementary Levels - Lesson 20 - Getting around.mp4')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.english.set()
        await message.answer(f"{message.text}",reply_markup=english)

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=HV6h7MRrRNA'>LINK</a></b>")

@dp.message_handler(state=ALLSTATE.intermedet)
async def element_def(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIhkmJk9gKPVSbPdatH7TYcCWCqLAwmAAJxAgACdwAB8UUTPEVrXczqSiQE'
        await message.answer_video(file_id,caption='01 - Intermediate Levels - Lesson 1 - Horror Films.mp4')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIhlGJk9hjpZsHvBlMCRc1d1uN0C1_lAAJyAgACdwAB8UW1OuOeNnp0ciQE'
        await message.answer_video(file_id,caption='02 - Intermediate Levels - Lesson 2 - Rock n\' Roll.mp4')

    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIhlmJk9jQfiXv-ceKaGzTG9RcldmRIAAJzAgACdwAB8UVdTVlhB8A7CSQE'
        await message.answer_video(file_id,caption='03 - Intermediate Levels - Lesson 3 - Space.mp4')

    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIhmGJk9kgkXDDQVD3CdFOOJ9VHWzLQAAJ0AgACdwAB8UWOd57lR1v6ViQE'
        await message.answer_video(file_id,caption='04 - Intermediate Levels - Lesson 4 - On the farm.mp4')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIhmmJk9l6a0sNP-DZ2x_qPcv0J0yKzAAJ1AgACdwAB8UVxxFZ62fI-0CQE'
        await message.answer_video(file_id,caption='05 - Intermediate Levels - Lesson 5 - At the doctor\'s office.mp4')

    elif message.text=='6-dars':
        file_id = 'BAACAgEAAxkBAAIhnGJk9ngb7spxcN6BgfwzGxxbeIMYAAJ2AgACdwAB8UWmtbLvPelfjSQE'
        await message.answer_video(file_id,caption='06 - Intermediate Levels - Lesson 6 - At the circus.mp4')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIhnmJk9o0__KLgvdR5AifqabgWJAPgAAJ3AgACdwAB8UVW9y4DAktHcSQE'
        await message.answer_video(file_id,caption='07 - Intermediate Levels - Lesson 7 - At the beach.mp4')

    #elif message.text=='CSS Asoslari':
       # file_id = 'BAACAgIAAxkBAAITa2JhFjJOR36axrMy9e_rLNFB0uaBAAJyBgACvvmQSg9lWWq2dQkeJAQ'
        #await message.answer_video(file_id,caption='📹 CSS Asoslari ')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIhoGJk9qIQVj5EoCdtgu4p3n3AUYn3AAJ4AgACdwAB8UV9OSV6p2XJLiQE'
        await message.answer_video(file_id,caption='08 - Intermediate Levels - Lesson 8 - Crime doesn\'t pay.mp4')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIhomJk9sfGsiTpv1pFwoiKi6vkZ_jyAAJ5AgACdwAB8UWUOhYeou_OjyQE'
        await message.answer_video(file_id,caption='09 - Intermediate Levels - Lesson 9 - At the amusement park.mp4')

    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIhpGJk9uDl87ki1x_JQJtgP-1OVr_9AAJ6AgACdwAB8UVi-8cUwMQ_PiQE'
        await message.answer_video(file_id,caption='10 - Intermediate Levels - Lesson 10 - At the grocery store.mp4')

    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIhpmJk9vZybtw-m84WlQTngIHdBNqPAAJ7AgACdwAB8UVZgwO5zHJysiQE'
        await message.answer_video(file_id,caption='11 - Intermediate Levels - Lesson 11 - At the playground.mp4')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIhqGJk9wgWsUL_TVlIer0pPRcJZIReAAJ8AgACdwAB8UW7zjs6mbgqjiQE'
        await message.answer_video(file_id,caption='12 - Intermediate Levels - Lesson 12 - At the camp.mp4')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIhqmJk9xwcb9BUdphy20QBciHDmoozAAJ9AgACdwAB8UVfIOKc9J_YfiQE'
        await message.answer_video(file_id,caption='13 - Intermediate Levels - Lesson 13 - At the hotel.mp4')

    elif message.text=='14-dars':
        file_id = 'BAACAgEAAxkBAAIhrGJk9zXHXb4lT0PJNUPE7A3xwi8yAAJ-AgACdwAB8UUymHdlIlFyTyQE'
        await message.answer_video(file_id,caption='14 - Intermediate Levels - Lesson 14 - Fairy tales and legends.mp4')

    elif message.text=='15-dars':
        file_id = 'BAACAgEAAxkBAAIhrmJk90rA1nOX_wM5h-xGqwzS1Q5xAAJ_AgACdwAB8UWsezFxA5iXECQE'
        await message.answer_video(file_id,caption='15 - Intermediate Levels - Lesson 15 - Christmas.mp4')

    elif message.text=='16-dars':
        file_id = 'BAACAgEAAxkBAAIhsGJk918GtxoenLxrKsZktSnWmLUAA4ACAAJ3AAHxRRimfNYMq6bBJAQ'
        await message.answer_video(file_id,caption='16 - Intermediate Levels - Lesson 16 - In the workshop.mp4')

    elif message.text=='17-dars':
        file_id = 'BAACAgEAAxkBAAIhsmJk93fkdaCDglmCQFP6NZ6RPtBzAAKBAgACdwAB8UUIV2nlsrm_VyQE'
        await message.answer_video(file_id,caption='17 - Intermediate Levels - Lesson 17 - Under the water.mp4')

    if message.text=='18-dars':
        file_id = 'BAACAgEAAxkBAAIhtGJk95BBqj29Lp6feINAXcpklc9kAAKCAgACdwAB8UULJAcECNweiCQE'
        await message.answer_video(file_id,caption='18 - Intermediate Levels - Lesson 18 - At the doctors.mp4')

    elif message.text=='19-dars':
        file_id = 'BAACAgEAAxkBAAIhtmJk97Z-cxHqwBQYfVclLQLIddQuAAKDAgACdwAB8UVQahLJkwpLSiQE'
        await message.answer_video(file_id,caption='19 - Intermediate Levels - Lesson 19 - Preview (Lesson 1 to 9).mp4')

    elif message.text=='20-dars':
        file_id = 'BAACAgEAAxkBAAIhuGJk99QRgsTkOl76qee0vCm8t4RjAAKEAgACdwAB8UWKWi3iJ4K8ByQE'
        await message.answer_video(file_id,caption='20 - Intermediate Levels - Lesson 20 - Preview (Lesson 10 to 18).mp4')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.english.set()
        await message.answer(f"{message.text}",reply_markup=english)

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=HV6h7MRrRNA'>LINK</a></b>")


@dp.message_handler(state=ALLSTATE.call_uzb)
async def element_def(message:Message,state:FSMContext):

    if message.text=='1-dars':
        file_id = 'BAACAgQAAxkBAAIhumJk-A1nmf6ex6o2hItAmctgpwrqAAIBCgACR5MxUmgyGCSSta5SJAQ'
        await message.answer_video(file_id,caption='01 - Ingliz tili grammatikasi - 1.Kirish.mp4')

    elif message.text=='2-dars':
        file_id = 'BAACAgQAAxkBAAIhvGJk-Cdp_G5_ZMrxmmsxsv3Mq0xjAAICCgACR5MxUvSpCjSYXT3wJAQ'
        await message.answer_video(file_id,caption='02 - Ingliz tili grammatikasi - 2.To be fe\'li.mp4')

    elif message.text=='3-dars':
        file_id = 'BAACAgQAAxkBAAIhvmJk-ERPeO-7Zovd2N-jHKtlMe-vAAIDCgACR5MxUo7fSUpn_lMWJAQ'
        await message.answer_video(file_id,caption='03 - Ingliz tili grammatikasi - 3. To have fe\'li..mp4')

    elif message.text=='4-dars':
        file_id = 'BAACAgQAAxkBAAIhwGJk-Gbpcw7V1kf9fKbN5JUlf9rYAAIECgACR5MxUsb9gdZJ9I1bJAQ'
        await message.answer_video(file_id,caption='04 - Ingliz tili grammatikasi - 4. Present Simple..mp4')

    elif message.text=='5-dars':
        file_id = 'BAACAgQAAxkBAAIhwmJk-ITIaNyQv3a7sl4hGiUAAQb1OwACBQoAAkeTMVINzvXloG0DeyQE'
        await message.answer_video(file_id,caption='05 - Ingliz tili grammatikasi - 5. Present continuous..mp4')

    elif message.text=='6-dars':
        file_id = 'BAACAgQAAxkBAAIhxGJk-JvXAxHSKC8_bDxP5HCjzlzmAAIGCgACR5MxUhMyJWL53yiAJAQ'
        await message.answer_video(file_id,caption='06 - Ingliz tili grammatikasi - 6. Verbs..mp4')

    elif message.text=='7-dars':
        file_id = 'BAACAgQAAxkBAAIhxmJk-LR_G0htyp9W9CC5HQcU1FiwAAIHCgACR5MxUrr6wL0t-iVeJAQ'
        await message.answer_video(file_id,caption='07 - Ingliz tili grammatikasi - 7. Past simple..mp4')

   # elif message.text=='CSS Asoslari':
        #file_id = 'BAACAgIAAxkBAAITa2JhFjJOR36axrMy9e_rLNFB0uaBAAJyBgACvvmQSg9lWWq2dQkeJAQ'
       # await message.answer_video(file_id,caption='📹 CSS Asoslari ')

    elif message.text=='8-dars':
        file_id = 'BAACAgQAAxkBAAIhyGJk-Nlscz2h8rrBGwbUSOA3IX_ZAAIICgACR5MxUgy6HERnzq0CJAQ'
        await message.answer_video(file_id,caption='08 - Ingliz tili grammatikasi - 8. Past continuous.mp4')

    elif message.text=='9-dars':
        file_id = 'BAACAgQAAxkBAAIhymJk-QABDpMoQGysGh3S-Ips1Qi4GgACCQoAAkeTMVK1az4ECOMm-yQE'
        await message.answer_video(file_id,caption='09 - Ingliz tili grammatikasi - 9. Used to do va to be used to doing.mp4')

    elif message.text=='10-dars':
        file_id = 'BAACAgQAAxkBAAIhzGJk-SEG9uoGdttdzZpBpXZa5pgiAAIKCgACR5MxUiS5PQ3FXYgAASQE'
        await message.answer_video(file_id,caption='10 - Ingliz tili grammatikasi - 10. Present Perfect Simple.mp4')

    elif message.text=='11-dars':
        file_id = 'BAACAgQAAxkBAAIhzmJk-UZu-AINvDKnAmh86juqKDAuAAILCgACR5MxUsj7j-ssDH0_JAQ'
        await message.answer_video(file_id,caption='11 - Ingliz tili grammatikasi - 11. Present perfect continuous.mp4')

    elif message.text=='12-dars':
        file_id = 'BAACAgQAAxkBAAIh0GJk-WHreOKTPJRuSKLCm7RqOlLrAAIMCgACR5MxUlnanS7D3nEkJAQ'
        await message.answer_video(file_id,caption='12 - Ingliz tili grammatikasi - 12. Past perfect simple.mp4')

    elif message.text=='13-dars':
        file_id = 'BAACAgQAAxkBAAIh0mJk-XrRoGWL0OEHdXjeoFAl4pCSAAINCgACR5MxUrSvZTqF41qNJAQ'
        await message.answer_video(file_id,caption='13 - Ingliz tili grammatikasi - 13. Past perfect continuous.mp4')

    elif message.text=='14-dars':
        file_id = 'BAACAgQAAxkBAAIh1GJk-aUIw87AFEx_x_XCVlcHOn8oAAIOCgACR5MxUhmbBySsZ9wAASQE'
        await message.answer_video(file_id,caption='14 - Ingliz tili grammatikasi - 14. Kelajak zamon fe’llari..mp4')

    elif message.text=='15-dars':
        file_id = 'BAACAgQAAxkBAAIh1mJk-bvEP7MCJY1KOJd5fNgEl0LOAAIPCgACR5MxUhN_ft1eTUwkJAQ'
        await message.answer_video(file_id,caption='15 - Ingliz tili grammatikasi - 15. Future Perfect Simple.mp4')

    elif message.text=='16-dars':
        file_id = 'BAACAgQAAxkBAAIh2GJk-dJMTMTCVhq1tyL-YysnbTeIAAIQCgACR5MxUuHJkpw3uPbZJAQ'
        await message.answer_video(file_id,caption='16 - Ingliz tili grammatikasi - 16. Future continuous..mp4')

    elif message.text=='17-dars':
        file_id = 'BAACAgQAAxkBAAIh2mJk-eZT0o086nVx25tOjOXRsjoLAAIRCgACR5MxUnqaU0hZB7SuJAQ'
        await message.answer_video(file_id,caption='17 - Ingliz tili grammatikasi - 17. Ingliz tilidagi 12 ta zamon..mp4')

    if message.text=='18-dars':
        file_id = 'BAACAgQAAxkBAAIh3GJk-fzZ1SgUlxWyBPHMq_22EK06AAISCgACR5MxUnPSJGTKw5U7JAQ'
        await message.answer_video(file_id,caption='18 - Ingliz tili grammatikasi - 18. Gapda in, on va at ning ishlatilishi..mp4')

    elif message.text=='19-dars':
        file_id = 'BAACAgQAAxkBAAIh3mJk-hXzXlFgt-fdZx7qKuDJ2PLdAAITCgACR5MxUtFpX8XwXTttJAQ'
        await message.answer_video(file_id,caption='19 - Ingliz tili grammatikasi - 19.Sanaladigan va sanalmaydigan otlar..mp4')

    elif message.text=='20-dars':
        file_id = 'BAACAgQAAxkBAAIh4GJk-ilwGNt8wJnTnzLi4gPrZC2AAAIUCgACR5MxUs3eyaLdQxC4JAQ'
        await message.answer_video(file_id,caption='20 - Ingliz tili grammatikasi - 20. Article.mp4')

    elif message.text=='21-dars':
        file_id = 'BAACAgQAAxkBAAIh4mJk-lu58l5FaeV6nfNPp5lUqghfAAIVCgACR5MxUp0IH5U-SUqRJAQ'
        await message.answer_video(file_id,caption='21 - Ingliz tili grammatikasi - 21. Conditionals.mp4')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.english.set()
        await message.answer(f"{message.text}",reply_markup=english)

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=HV6h7MRrRNA'>LINK</a></b>")
