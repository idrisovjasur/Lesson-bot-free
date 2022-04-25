from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.default.algor_key import algor_full_key
from keyboards.default.keyboard import bosh_sahifa, algoritm_key
from states.holatlar import ALLSTATE
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(Text('Algoritm'))
async def front(message:Message):
    await message.answer('👨‍💻Quydagi darslarni birini tanlang',reply_markup=algoritm_key)
    await ALLSTATE.algoritm.set()

@dp.message_handler(state=ALLSTATE.algoritm)
async def algor_def(message:Message,state:FSMContext):
    if message.text=='Sariqdev':
        await message.answer(f"{message.text}",reply_markup=algor_full_key)
        await ALLSTATE.sariq_algoritm.set()

    if message.text=='⬆️Ortga':
        await message.answer(f"{message.text}",reply_markup=bosh_sahifa)
        await state.finish()

@dp.message_handler(state=ALLSTATE.sariq_algoritm)
async def sariq_def_algor(message:Message,state:FSMContext):

    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIiF2Jk-1dJnxus9cVzsp62HcgYaloOAAKGAQACxYLZRTcfH-Ap3jDYJAQ'
        await message.answer_video(file_id,caption='01 - #00 ALGORITMLAR _`Ma`lumotlar Tuzilmasi va Algoritmlar` kirish darsi..mp4')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIiGWJk-9psczxVyyQKKUlfgX_U9SHqAAKIAQACxYLZRRIZAAGDLN6rlSQE'
        await message.answer_video(file_id,caption='#02 ALGORITMLAR _ BINARY SEARCH.mp4')

    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIiG2Jk--9qmocHnSoHdOsoogcNavMJAAKJAQACxYLZRalc-ZO3RKwrJAQ'
        await message.answer_video(file_id,caption='#03 ALGORITMLAR _ Big O.mp4')

    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIiHWJk_AbH0s01zRXlrq02AfjViVftAAKKAQACxYLZRXr8T9jtizHYJAQ'
        await message.answer_video(file_id,caption='#04 ALGORITMLAR _ ARRAY.mp4')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIiH2Jk_BqSKy5J-MfA7Svo_E2bGpkUAAKLAQACxYLZReS795DsWAjjJAQ'
        await message.answer_video(file_id,caption='#05 ALGORITMLAR _ LINKED LISTS.mp4')

    elif message.text=='6-dars':
        file_id = 'BAACAgEAAxkBAAIiIWJk_C6kv7W39Ot22RERYsTYmFlzAAKMAQACxYLZRQMv7iB6k02QJAQ'
        await message.answer_video(file_id,caption='#06 ALGORITMLAR _ LINKED LISTS. AMALIYOT.mp4')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIiI2Jk_EW9IgTsQcaAXChWLxQwupbxAAKNAQACxYLZRWJHPjz77FjBJAQ'
        await message.answer_video(file_id,caption='#07 ALGORITMLAR _ SELECTION SORT.mp4')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIiJWJk_Fprb7devsoiYidvAjLTAAFmMAACjgEAAsWC2UXXeAffPRJHiyQE'
        await message.answer_video(file_id,caption='#08 ALGORITMLAR _ REKURSIYA.mp4')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIiJ2Jk_G_RjXUSvl4Rcp38K8jteATIAAKPAQACxYLZRRK35Y128M5xJAQ'
        await message.answer_video(file_id,caption='#09 ALGORITMLAR _ STACK VA REKURSIYA.mp4')

    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIiKWJk_I1GI7I2D7nB3LmQdsPFliNDAAKQAQACxYLZRUAhsc2XRwJaJAQ'
        await message.answer_video(file_id,caption='#10 ALGORITMLAR _ Divide and Conquer.mp4')

    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIiMGJk_OKMi2Cw1YRLvINaUD_P4I0WAAKRAQACxYLZRae3YdfGwTnkJAQ'
        await message.answer_video(file_id,caption='#11 ALGORITMLAR _ Quicksort.mp4')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIiMmJk_QVWSJMqHhY-vZpPCot2AAFvHgACkgEAAsWC2UWmDn46iM8i3SQE'
        await message.answer_video(file_id,caption='#12 ALGORITMLAR _ Bubble sort.mp4')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIiNGJk_SHBm5iXDodc2o4fRxZ3PJFkAAKTAQACxYLZRa0NwlZ6tJnAJAQ'
        await message.answer_video(file_id,caption='#13 ALGORITMLAR _ Merge Sort.mp4')

    elif message.text=='14-dars':
        file_id = 'BAACAgEAAxkBAAIiNmJk_TcgTvO8vfVHiL0iRqy8Se0UAAKUAQACxYLZRbBMJUnf1C_TJAQ'
        await message.answer_video(file_id,caption='#14 ALGORITMLAR _ Hash tables.mp4')

    elif message.text=='15-dars':
        file_id = 'BAACAgEAAxkBAAIiOGJk_UstB8lHXWpqRYNYOCdwK_YjAAKVAQACxYLZRfUOcl80SrhXJAQ'
        await message.answer_video(file_id,caption='#15 ALGORITMLAR _ Graph Maʼlumotlar tuzilmasi va Breadth-First algoritmi.mp4')

    elif message.text=='16-dars':
        file_id = 'BAACAgEAAxkBAAIiOmJk_V8vytXACzcTf7kiMB_NdwZxAAKWAQACxYLZRTHgktGHK0XdJAQ'
        await message.answer_video(file_id,caption='#16 ALGORITMLAR _ Graph va Breadth-First Search Dasturi.mp4')

    elif message.text=='17-dars':
        file_id = 'BAACAgEAAxkBAAIiPGJk_XfCMDiGDA2bTEl9rK5422HdAAKXAQACxYLZRXAiw0tqXjGqJAQ'
        await message.answer_video(file_id,caption='#17 ALGORITMLAR _ Dijkstra Algoritmi.mp4')

    elif message.text=='18-dars':
        file_id = 'BAACAgEAAxkBAAIiPmJk_ZIY-muV4LtcjpsHDpyUtVoBAAKYAQACxYLZRUB3Wm5hoL4CJAQ'
        await message.answer_video(file_id,caption='#18 ALGORITMLAR _ Ochko\'z Algoritmlar.mp4')

    elif message.text=='19-dars':
        file_id = 'BAACAgEAAxkBAAIiQGJk_a28F9EC9tXAWAZtf24tgtYYAAKZAQACxYLZRcwatDq79emzJAQ'
        await message.answer_video(file_id,caption='#19 ALGORITMLAR _ NP-Muammolar.mp4')

    elif message.text=='20-dars':
        file_id = 'BAACAgEAAxkBAAIiQmJk_djpyV7gkImUNosxX99PEBXqAAKaAQACxYLZRcVIimDInuNrJAQ'
        await message.answer_video(file_id,caption='#20 ALGORITMLAR _ Dynamic Programming.mp4')

    elif message.text=='21-dars':
        file_id = 'BAACAgEAAxkBAAIiRGJk_fF0u97aSQSvmo9v3md6-vM2AAKbAQACxYLZRbztfiIbN0ARJAQ'
        await message.answer_video(file_id,caption='#21 ALGORITMLAR _ Dynamic Programming. 2-qism.mp4')

    elif message.text=='22-dars':
        file_id = 'BAACAgEAAxkBAAIiRmJk_gg7dvb-9GZOFIIXFp2y104KAAKcAQACxYLZRXVRdLKmh1isJAQ'
        await message.answer_video(file_id,caption='#22 ALGORITMLAR _ K-NN algoritmi. Klassifikasiya muammosi.mp4')

    elif message.text=='23-dars':
        file_id = 'BAACAgEAAxkBAAIiSGJk_iFf_ZgvI-CfJ7ZjSUKJ30-aAAKeAQACxYLZRZYYAnJExyihJAQ'
        await message.answer_video(file_id,caption='#23 ALGORITMLAR _ Mustaqil o\'rganish uchun tavsiyalar. 1-qism..mp4')

    elif message.text=='24-dars':
        file_id = 'BAACAgEAAxkBAAIiSmJk_qNnXwOhEcrR1_RSsHTDvxXRAAKeAQACxYLZRZYYAnJExyihJAQ'
        await message.answer_video(file_id,caption='#24 ALGORITMLAR _ Mustaqil o\'rganish uchun tavsiyalar. 1-qism..mp4')

    elif message.text=='25-dars':
        file_id = 'BAACAgEAAxkBAAIiTGJk_r7IrTxzSV-_7cjhY2pRs58bAAKfAQACxYLZRb37zuYRZ493JAQ'
        await message.answer_video(file_id,caption='#25 ALGORITMLAR _ Mustaqil o\'rganish uchun tavsiyalar. 2-qism..mp4')

    if message.text=='⬆️Ortga':
        await message.answer(f"{message.text}",reply_markup=algoritm_key)
        await ALLSTATE.algoritm.set()
    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=-f54HjaFp4w'>LINK</a></b>")