from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from states.holatlar import ALLSTATE
from aiogram.types import ContentTypes
from loader import dp,bot
from keyboards.default.keyboard import frontend,java_scriptlar
from keyboards.default.keyboard import (bosh_sahifa,berdiyev_j,html_1,css,sass,jQuery,react_keyboard,amalyot_key,
                                        zokir_1,berdiyev_j_2,berdiyev_saslar,
                                        ulugbek_samig,
                                        bootlar,farxod_java_keyboard,berdiyev_java_keyboard,samar_react_keyboard,abu_tech_keyboard_react,
                                        )


@dp.message_handler(Text('📂 FrontEnd'))
async def front(message:Message):
    await message.answer('<b>👨‍💻Quydagi darslarni birini tanlang</b>',reply_markup=frontend)
#################################################HTML
@dp.message_handler(Text('HTML5'))
async def htmlll(message:Message,state:FSMContext):
    await message.answer(f"HTML Darslar:",reply_markup=html_1)
    await ALLSTATE.html.set()

@dp.message_handler(state=ALLSTATE.html)
async def html(message:Message,state:FSMContext):
    if message.text=='Saidbek Arslonov':
        file = 'BAACAgIAAxkBAAIPhWJgBy7gEw_y1v9aWiZtGhUy11uLAAJ_AwACCuuwS1dDvNva-B7MJAQ'
        await message.answer_video(file, caption='📹 1 Soatda HTMLni o\'rganamiz')
    elif message.text=='Berdiyev Javohir':
        await message.answer('Darslar:',reply_markup=berdiyev_j)
        await ALLSTATE.berdiyev_j.set()
    elif message.text=='⬆️Ortga':
        await state.finish()
        await message.answer(f"{message.text}",reply_markup=frontend)

@dp.message_handler(state=ALLSTATE.berdiyev_j)
async def ber(message:Message,state:FSMContext):
    if message.text=='1-dars':
            file = 'BAACAgIAAxkBAAIPimJgCh2M0Sbxac0h5KFVjJ1-Hf1fAAKkDwACsFqhS_lBNS7e_5tOJAQ'
            await message.answer_video(file,caption=f"HTML5 1-Dars o\'zbek tilida.HTML haqida.Web dasturlash   Kirish:\n"
                                            f"Youtube: https://www.youtube.com/watch?v=UyGKgrKgRaM")
    elif message.text=='2-dars':
            file = 'BAACAgIAAxkBAAIPjGJgCp46pZD9Az3mY_WvUgOFKLPmAAKlDwACsFqhS625zmaUpZCXJAQ'
            await message.answer_video(file,caption=f"HTML5 2-dars (matnlar, img qo'shish, havolalar). Web dasturlash\n"
                                              f"Youtube: https://www.youtube.com/watch?v=MFfms2VvGUA")

    elif message.text=='3-dars':
            file = 'BAACAgIAAxkBAAIPjGJgCp46pZD9Az3mY_WvUgOFKLPmAAKlDwACsFqhS625zmaUpZCXJAQ'
            await message.answer_video(file,caption=f"HTML5 3-Dars o'zbek tilida | Web Dasturlash (Formalar, Ro'yxatlar, Jadvalar)\n"
                                            f"Youtube: https://youtu.be/Dm3GZoqLVF4")

    elif message.text=='⬆️Ortga':
        await ALLSTATE.html.set()
        await message.answer(f"{message.text}",reply_markup=html_1)
##############################################################################

###############CSSS
@dp.message_handler(Text('CSS3'))
async def html(message:Message):
    await message.answer(f"{message.text}",reply_markup=css)
    await ALLSTATE.css.set()

@dp.message_handler(state=ALLSTATE.css)
async def csslar(message:Message,state:FSMContext):
    if message.text=='Berdiyev Javohir':
        await message.answer(f"{message.text}",reply_markup=berdiyev_j_2)
        await ALLSTATE.berdiyev_j_css.set()

    elif message.text=='Zokir Rakhmonov':
        await message.answer(f"{message.text}",reply_markup=zokir_1)
        await ALLSTATE.zokir_css.set()

    elif message.text=='⬆️Ortga':
        await state.finish()
        await message.answer(f"{message.text}",reply_markup=frontend)

@dp.message_handler(state=ALLSTATE.berdiyev_j_css)
async def berdiyev_css(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIS12JhEHr4ikZAoSuaPx_4K1AaeiJcAAIDBwACbw14S624H2ndJwABcyQE'
        await message.answer_video(file_id,caption='📹 Web Dasturlash 4-Dars | CSS 3 kirish asosiy bo\'lim ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIS2WJhELEo829cDzL7GTHNMOQFxs56AALBBwACL3fJSwE0cof4eBD_JAQ'
        await message.answer_video(file_id,caption='📹 Web Dasturlash. CSS 3  2-Dars | textlar, box module, fontlar bilan ishlash ')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIS22JhEPzvxPplARl5bF7_XkRaHaCRAALlBwACXA-oSy2_-tCVzHTPJAQ'
        await message.answer_video(file_id,caption='📹 HTML va CSS foydalanib O\'zbeksiton bayrog\'ini yasash ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAIS3WJhETNXVxwqMd24GIEHqc8Cj7-LAAJqBgACJE2hS_WwtJrNytRWJAQ'
        await message.answer_video(file_id,caption='📹 Web Dasturlash. CSS 3  4-Dars | Float, Display, Position lar bilan ishlash ')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAIS32JhEXgpBybgn5MO51QwVvz38bm2AALgBgACnYhBS8Mp6O_YLQ8xJAQ'
        await message.answer_video(file_id,caption='📹 CSS3 5-dars (amaliyot) - HTML ca CSS dan foydalanib template yasash, Web dasturlash ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIS4WJhEapH4EgqAe02oo8ED6J-Sns7AAIOCAACb26BSVWKlWKPbyceJAQ'
        await message.answer_video(file_id,caption='📹 CSS 6-dars Animatsiya yasash 1-qism Transition va Transform 2D haqida ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAIS4WJhEapH4EgqAe02oo8ED6J-Sns7AAIOCAACb26BSVWKlWKPbyceJAQ'
        await message.answer_video(file_id,caption='📹 CSS 7-dars Animatsiya yasash 1-qism Transition va Transform 2D haqida ')
    elif message.text=='⬆️Ortga':
        await ALLSTATE.css.set()
        await message.answer(f"{message.text}",reply_markup=css)

@dp.message_handler(state=ALLSTATE.zokir_css)
async def zokir_csss(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAITLGJhE1vWm2UhXg2cvqeE3R6omtZOAAMRAAK-qZBKYVcEg2bL4vUkBA'
        await message.answer_video(file_id,caption='📹 CSS (O\'zbek Tilida) - Qism 1 ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAITLmJhE5WdFTUiCG8QvT3HQaOyFOxzAALXCQACoUfhSpYrk6hRc-ZrJAQ'
        await message.answer_video(file_id,caption='📹 CSS (O\'zbek Tilida) - Qism 2 ')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAITMGJhE70FEhLJlp3YmzSlKX981IxwAAJnBwAC9KW5S-sLciIbjoQcJAQ'
        await message.answer_video(file_id,caption='📹 CSS (O\'zbek Tilida) - Qism 3 ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAITMmJhE_dcbYUKs5Rb5DU92jLrMQS1AAJrBwAC9KW5SzyvtTRICAzWJAQ'
        await message.answer_video(file_id,caption='📹 CSS - Position: [relative, absolute, fixed, sticky](O\'zbek Tilida) - Qism 4')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAITNGJhFBx2E8I3_9-hqU1rxszJHAmpAAKFCAACiVigSl85XPVMxaJHJAQ'
        await message.answer_video(file_id,caption='📹 CSS - Responsive Design | O\'zbek Tilida | viewport, media, max-width, vw, vh | - Qism 5  ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAITNmJhFFHklgOuQPYn-YoNohMlmf9NAAI2BwAC45u4SkdG3V6YzYYsJAQ'
        await message.answer_video(file_id,caption='📹 CSS - Flexbox | O\'zbek Tilida | direction, justify, align, wrap, shrink, grow, basis, order | Qism 6')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAITOGJhFHpa4_L5QITSQohSDImxjfBCAAJxBwAC9KW5SxDUmpbrmW1zJAQ'
        await message.answer_video(file_id,caption='📹 CSS - Grid | O\'zbek Tilida | Columns, Rows, Units, Gap, Template, Align, Justify, Area| Qism 7 ')
    elif message.text=='CSS Asoslari':
        file_id = 'BAACAgIAAxkBAAITa2JhFjJOR36axrMy9e_rLNFB0uaBAAJyBgACvvmQSg9lWWq2dQkeJAQ'
        await message.answer_video(file_id,caption='📹 CSS Asoslari ')
    elif message.text=='⬆️Ortga':
        await ALLSTATE.css.set()
        await message.answer(f"{message.text}",reply_markup=css)
#################################

@dp.message_handler(Text('Sass'))
async def html(message:Message):
    await message.answer(f"{message.text}",reply_markup=sass)
    await ALLSTATE.sass.set()

@dp.message_handler(state=ALLSTATE.sass)
async def sasss(message:Message,state:FSMContext):
    if message.text=='Berdiyev Javohir':
        await message.answer(f"{message.text}",reply_markup=berdiyev_saslar)
        await ALLSTATE.ber_sass.set()

    elif message.text=='⬆️Ortga':
        await state.finish()
        await message.answer(f"{message.text}",reply_markup=frontend)

@dp.message_handler(state=ALLSTATE.ber_sass)
async def berdiyev_sas(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAITjmJhGgABCd5WuHddh4Lhfkv-d2OBuwACqhcAAs4miUtkj7qY5Wk_diQE'
        await message.answer_video(file_id,caption='📹 SASS haqida,  1-dars umumiy ma\'lumotlar')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAITkGJhGi7ZmZFH9HPC_TDM0ncjuK-_AAJMEwACg_6YSyyMEeo1JDTDJAQ'
        await message.answer_video(file_id,caption='📹 SCSS 2-dars, Partial.scss haqida  ')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.sass.set()
        await message.answer(f"{message.text}",reply_markup=sass)

#########################################

################BOOT
@dp.message_handler(Text('Bootstrap4'))
async def html(message:Message):
    await message.answer(f"{message.text}",reply_markup=bootlar)
    await ALLSTATE.boot.set()

@dp.message_handler(state=ALLSTATE.boot)
async def boot_strap(message:Message,state:FSMContext):
    if message.text=='Ulug\'bek Samigjanov':
        await message.answer(f'{message.text}',reply_markup=ulugbek_samig)
        await ALLSTATE.ulug_sam.set()
    if message.text=='⬆️Ortga':
        await state.finish()
        await message.answer(f"{message.text}",reply_markup=frontend)

@dp.message_handler(state=ALLSTATE.ulug_sam)
async def ulugbek(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIUUWJhKfVg0WoMVXaONjzehrfcyxI-AAJ-CgACLEzJSsAW_ZtFBooRJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 1. Kirish ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIUU2JhKhVxypgZ3EIyImdbL1_OKy0XAAKwDAAC51DQSs1DKtEgOD_sJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 2. Bootstrap va uning versiyalari. Kurs loyihasi ')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIUVWJhKjoB_xwx4-PBwuV-N9R26fAUAALmCwACbZXZSiUAAYqXSIAIliQE'
        await message.answer_video(file_id,caption='📹 Bootstrap | 3. Bootstrapni o\'rnatib olish ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAIUV2JhKmYCr5sutUdUCM1jIqpz_2H-AAJsCgAC61rgSh0YikPT7rchJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 4. Breakpoints va Containers ')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAIUWWJhKop7ksuKBkrlq0zurrg5FqtrAAL3CwACtB25S3vErnvo5GsDJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 5. Grid (1-qism)  ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIUW2JhKq_6a1dfpINriMLViQIJz_4GAAIyDQACifkJS-Yf_k3lIxBJJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 6. Grid (2-qism) ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAIUXWJhKuthXdG-CzKn_N0leU2F_G_pAAJ1CwAC3moZS8G_Bzv0Ea6BJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 7. Columns')
    elif message.text=='CSS Asoslari':
        file_id = 'BAACAgIAAxkBAAITa2JhFjJOR36axrMy9e_rLNFB0uaBAAJyBgACvvmQSg9lWWq2dQkeJAQ'
        await message.answer_video(file_id,caption='📹 CSS Asoslari ')
    if message.text=='8-dars':
        file_id = 'BAACAgIAAxkBAAIUX2JhK0eweOnjUXh_QA9CjjVkrgVkAAJXDQACEyQhS7HxmEeibJnGJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 8. Gutters ')

    elif message.text=='9-dars':
        file_id = 'BAACAgIAAxkBAAIUYWJhK2_w99rBahnN-vDhp0wiw16iAAIVCwACwiswS4VMGtoyckazJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 9. Typography ')
    elif message.text=='10-dars':
        file_id = 'BAACAgIAAxkBAAIUY2JhK5B5LBynWAszci1kq0eINNJdAALUCwACX_c5S3w_4hqclN5hJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 10. Images ')
    elif message.text=='11-dars':
        file_id = 'BAACAgIAAxkBAAIUZWJhK7heGEltfXFmKnRks9ll6QdaAAItDQAC-dxRS3uV-NMZ2iKbJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 11. Tables ')

    elif message.text=='12-dars':
        file_id = 'BAACAgIAAxkBAAIUZ2JhK93epa3zhBcm83UmsJ5kOf6FAAIYDgACa5bRSzt7dogcf3pYJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 12. Formalar. Form control ')

    elif message.text=='13-dars':
        file_id = 'BAACAgIAAxkBAAIUaWJhLBIbmvUeuGQe-OoEF4xxNLnnAAIwDAACP8GxSzLeZHqqVgJBJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 13. Select. Checks & Radios. Range ')

    elif message.text=='14-dars':
        file_id = 'BAACAgIAAxkBAAIUa2JhLFfoohhPmsbaVXst53rv1lOLAALKCwACCz6wS8GHDFjKxOk1JAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 14. Input group')

    elif message.text=='15-dars':
        file_id = 'BAACAgIAAxkBAAIUbWJhLNll2jOf4lZeChB9AySgV8ejAAJVDQACkQLAS8tIpfdxD7LuJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 15. Floating labels. Form layout ')

    elif message.text=='16-dars':
        file_id = 'BAACAgIAAxkBAAIUb2JhLQJRW6AcxQgbP7ZDAnX99sHfAALeDAAC2tTIS8igBAfZS0NBJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 16. Validation  ')

    elif message.text=='17-dars':
        file_id = 'BAACAgIAAxkBAAIUcWJhLSP41DZvZq8uMcC_T0oaKgoJAALECgACc-zpS_x_fDuUrMj7JAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 17. Accordion, alerts, badge, breadcrumb ')

    if message.text=='18-dars':
        file_id = 'BAACAgIAAxkBAAIUc2JhLU-1YutQjNWXgStEdujsvU4RAAJtCwACBYD5S977sLiCxUUdJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 18. Button, button group  ')

    elif message.text=='19-dars':
        file_id = 'BAACAgIAAxkBAAIUdWJhLWseuTuiFW5EnYQgDuq2RJubAALjCQACI8YAAUiiDi8l4Qhg9SQE'
        await message.answer_video(file_id,caption='📹 Bootstrap | 19. Card ')
    elif message.text=='20-dars':
        file_id = 'BAACAgIAAxkBAAIUd2JhLYjD9by0yAYwsyJ6ilcPFJZfAAL7DQACITkISE3gm2fzhOUOJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 20. Carousel ')
    elif message.text=='21-dars':
        file_id = 'BAACAgIAAxkBAAIUeWJhLbny8tps6aIR1wkkup1HJNyhAAIcCQACOfcRSGJ6s04sXCkJJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 21. Collapse, Dropdowns, List group')

    elif message.text=='22-dars':
        file_id = 'BAACAgIAAxkBAAIUe2JhLd0uShVUUhVrXCLiLYNl-gABwQAC3gwAAtoSOEiyj6gZOc6a8yQE'
        await message.answer_video(file_id,caption='📹 Bootstrap | 22. Modal ')

    elif message.text=='23-dars':
        file_id = 'BAACAgIAAxkBAAIUfWJhLfktQpYGtBgRsuuoVEkdDc6fAAK0DQACT41ASA9Ue9QuZpmNJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 23. Navs, tabs, navbar ')

    elif message.text=='24-dars':
        file_id = 'BAACAgIAAxkBAAIUf2JhLhrpBrEFq9AHmQuDqvRfaVtQAALbDAAC_XeASBLAlMoDHZIGJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 24. Offcanvas, pagination ')

    elif message.text=='25-dars':
        file_id = 'BAACAgIAAxkBAAIUgWJhLk7wZdPRYhfyy4rJ6kQThea5AAKwDQAC9eCRSLAg71oE62DRJAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 25. Popover, progress ')


    elif message.text=='⬆️Ortga':
        await ALLSTATE.boot.set()
        await message.answer(f"{message.text}",reply_markup=bootlar)

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=gdqjNTgRmIw'>LINK</a></b>")
####################################################


#########################Javascript
@dp.message_handler(Text('JavaScript & ES6'))
async def html(message:Message):
    await message.answer(f"{message.text}",reply_markup=java_scriptlar)
    await ALLSTATE.javascrpt.set()

@dp.message_handler(state=ALLSTATE.javascrpt)
async def java_script(message:Message,state:FSMContext):
    if message.text=='Berdiyev Javohir':
        await message.answer(f"{message.text}",reply_markup=berdiyev_java_keyboard)

        await ALLSTATE.berdiyev_java_script.set()

    elif message.text=='Farxod Dadajonov':

        await message.answer(f'{message.text}',reply_markup=farxod_java_keyboard)

        await ALLSTATE.farxod_java_script.set()
    elif message.text=='⬆️Ortga':
        await state.finish()
        await message.answer(f"{message.text}",reply_markup=frontend)

@dp.message_handler(state=ALLSTATE.berdiyev_java_script)
async def berdiyev_java(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIU8WJhNLz8cQdEiFVNY-D6R5z4KyM6AAKxCQACLDTASPf0GBO8EXbzJAQ'
        await message.answer_video(file_id,caption='📹 Javascirpt 1-dars. Ummiy ma\'lumotlar, Javascript haqida  ')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIU82JhNOhn_9Kwxl9zj_9QXVyn6TRRAAJTCgAC4OdpSXeKgPS-gojwJAQ'
        await message.answer_video(file_id,caption='📹 Javascript asoslari 2-dars. Variables, Data types Interaction: alert, prompt, confirm lar haqida')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIU9WJhNQj-92MhtbXAJr831dJfua7bAAKGCgACYJowSeLNzb-2rRbBJAQ'
        await message.answer_video(file_id,caption='📹 Javascript asoslari 3-dars.  Arithmetic Operators ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAIU92JhNS3eHcqa0tf52x7PQmw_Hh9pAAIJCQAC3j5oSQJGYj1vR6CIJAQ'
        await message.answer_video(file_id,caption='📹 Javascript 4-dars, Math functions haqida  ')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAIU_WJhNXaAZQNteDvjnAkdFINn0uhsAAIQCwACULQYSsupGaxB0jqMJAQ'
        await message.answer_video(file_id,caption='📹 Javascript 5-dars, Logical operations(Mantiqiy amallar) haqida ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIU_2JhNZUOxMMlPQX_cjNm9elcdfExAALsCAACZoRZSnOKYjxi6O3gJAQ'
        await message.answer_video(file_id,caption='📹 Javascript 6-dars, If else haqida  ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAIVAWJhNbcq6xb31CiegaZ8OxkTh43WAALsCgACTQi5SraHVcI3eTM7JAQ'
        await message.answer_video(file_id,caption='📹 Javascript 7-dars, Looplar haqida. for, while, do while ')

    if message.text=='8-dars':
        file_id = 'BAACAgIAAxkBAAIVA2JhNeJfeQIh6X9SBBldVW9vE4wFAAK6CQACV1j5SutBKPB1TcF4JAQ'
        await message.answer_video(file_id,caption='📹 Javascript 8- dars, Javascriptda Objectlar haqida bo\'ladi.  ')

    elif message.text=='9-dars':
        file_id = 'BAACAgIAAxkBAAIVB2JhNoUm28GlGqXH7UO8zU-hauF6AAIICwACNn5ZS4PP26_65M49JAQ'
        await message.answer_video(file_id,caption='📹 Bootstrap | 9. Typography ')
    elif message.text=='10-dars':
        file_id = 'BAACAgIAAxkBAAIVBWJhNlArt_tyqbaKZPF8uhpSWoo4AAKXCgACApSpSyC7BuaGwNGUJAQ'
        await message.answer_video(file_id,caption='📹 Javascript 10- dars, Javascriptda Array haqida bo\'ladi. ')
    elif message.text=='11-dars':
        file_id = 'BAACAgIAAxkBAAIVCWJhNqP1ab2ifd0j6MvaM8_kWrGPAALtCgACpBGgSKo_fbpcSCl4JAQ'
        await message.answer_video(file_id,caption='📹 Javascript 11- dars. for in va for of looplari haqida  ')

    elif message.text=='12-dars':
        file_id = 'BAACAgIAAxkBAAIVC2JhNsaRQxFgzQscHEbTcYFDS4qqAAKDCwAC4mTYSE51-TKFdwO_JAQ'
        await message.answer_video(file_id,caption='📹 Javascript 12- dars. Javascript da DOM bilan ishlash')

    elif message.text=='13-dars':
        file_id = 'BAACAgIAAxkBAAIVDWJhNyGwd97Tv4bBPTgzzGZW6oYtAAJlCgACr2MhSsm27Jht8jW7JAQ'
        await message.answer_video(file_id,caption='📹 Javascript Eventlar haqida ')

    elif message.text=='14-dars':
        file_id = 'BAACAgIAAxkBAAIVD2JhN0IvIvtoJolkxBE_OcZ1o72gAALsCwACP3cgSugb65LnjoXtJAQ'
        await message.answer_video(file_id,caption='📹   Javascript 14-dars. DOM js,  factory va constructor functionlar haqida ')

    elif message.text=='15-dars':
        file_id = 'BAACAgIAAxkBAAIVEWJhN2eJEvEObxk5Be9yuFyM3cGTAALxCwACjNbISzlO57ZDdOTlJAQ'
        await message.answer_video(file_id,caption='📹 Javascript 15-dars. Reference va Primitive typelar  haqida  ')

    elif message.text=='16-dars':
        file_id = 'BAACAgIAAxkBAAIVE2JhN5LWMpsqZxGGI916RHqgU8wxAALBCQACoq1BS7935bi4Le44JAQ'
        await message.answer_video(file_id,caption='📹 Javascript 16-dars. Getter-Setter va Try Catch lar  haqida   ')

    elif message.text=='17-dars':
        file_id = 'BAACAgIAAxkBAAIVFWJhN8wICD0ZnHnPmSHUGxiuK11fAALWCwAC1jqJSfbpP5qGB90fJAQ'
        await message.answer_video(file_id,caption='📹 Javascript 17-dars. Function arguments haqida')

    if message.text=='18-dars':
        file_id = 'BAACAgIAAxkBAAIVF2JhN_0Pl8_WU8pKyNB3vvtByU9yAAJmCwACr1iRSTf0fiySo9XqJAQ'
        await message.answer_video(file_id,caption='📹 Javascript yordamida carousel effekt yasab ko\'rish ')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.javascrpt.set()
        await message.answer(f"{message.text}",reply_markup=java_scriptlar)

@dp.message_handler(state=ALLSTATE.farxod_java_script)
async def farxod(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIVc2JhPB_x6W7wH3iqjOpARRuWulffAAKcBAACjvs5SvA3d7p-8FwtJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 1-Dars. Dasturlash muhitini o\'rnatish va sozlash.')

    elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIVdWJhPFxinG8BtbZX9R-CBhPj7E9GAAKnBAACjvs5Sqc0SmiS_x39JAQ'
        await message.answer_video(file_id,caption='JavaScript asoslari. 2-Dars. Ilk JavaScript kodimiz')
    elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIVeWJhPJRMOWOHbC_X--5-sXduEK47AAJ1BQAC0gE5SmJyvMPO2KW7JAQ'
        await message.answer_video(file_id,caption='JavaScript asoslari. 3-Dars. O\'zgaruvchilar va konstantalar. ')
    elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAIVe2JhPN9okTkZqKl4qgFCLd_Xbgr_AAJKBgACSz04SlpYPJkmh2f0JAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 4-Dars. O\'zgaruvchilarning turlari va primitiv turlar haqida.   ')

    elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAIVfWJhPQMxB8QSBfRzmg41FpK1Wr73AALxBAACVg6xS1iVnjyZgCg0JAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 5-Dars. Objectlar haqida.  ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIVgGJhPUm54olRRS0AAae0f1qsbmfIbgACSAUAAqcjcEoMj5An7rkb9CQE'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 6-Dars. Massivlar haqida.  ')

    elif message.text=='7-dars':
        file_id = 'BAACAgIAAxkBAAIVf2JhPTGN4rQmsrb7nVBNPnRNWsH7AAJIBQACpyNwSgyPkCfuuRv0JAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 7-Dars. Funktsiyalar bilan tanishamiz. ')

    elif message.text=='8-dars':
        file_id = 'BAACAgIAAxkBAAIVhWJhPZGEIXYZmqGSXksP-MbGS_QrAAJJBQACpyNwSsPM0AbbJvm3JAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 8-Dars. Arifmetik Operatorlar.   ')

    elif message.text=='9-dars':
        file_id = 'BAACAgIAAxkBAAIViWJhPdg--VZasv4m-5FReYL2qOajAALlBAACenR4SjCWDhEufVaHJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 9-Dars. Solishtiruv va tenglik operatorlari. ')
    elif message.text=='10-dars':
        file_id = 'BAACAgIAAxkBAAIVi2JhPgUEfsr_SNaPwLZVDKpSxXEiAAL1BAACVg6xS9uVKT-HrRRmJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 10-Dars. Ternary shartli operatori haqida ')
    elif message.text=='11-dars':
        file_id = 'BAACAgIAAxkBAAIVjWJhPilykGxslZHYbPpyNC-9DGGDAAJsBQACuL9xSqa1kVsQF8eCJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 11-Dars, 1-qism. Mantiqiy operatorlar ')

    elif message.text=='12-dars':
        file_id = 'BAACAgIAAxkBAAIVj2JhPk0upFJLw1ZuQr67jgLJJQInAAJtBQACuL9xSiGjuUrZsOFvJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 12-Dars. Amaliy mashg\'ulot. ')

    elif message.text=='13-dars':
        file_id = 'BAACAgIAAxkBAAIVkWJhPnjv7c2e2OGFXijovtvjEU63AAJKBQACpyNwSv07b6unjKQeJAQ'
        await message.answer_video(file_id,caption='📹 Javascript Eventlar haqida ')

    elif message.text=='14-dars':
        file_id = 'BAACAgIAAxkBAAIVk2JhPtno3gk4AAGWxe8lWqrFcnPQpQACbgUAAri_cUp4cwspw11n-iQE'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 14-Dars. switch case haqida. ')

    elif message.text=='15-dars':
        file_id = 'BAACAgIAAxkBAAIVlWJhPvuojh3fnWe6XhyQ8uKUn5YbAAKzBAACMAhQSgWce5P3a-__JAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 15-Dars. for loop haqida  ')

    elif message.text=='16-dars':
        file_id = 'BAACAgIAAxkBAAIVl2JhPysFus6IzSXFeAU6VrDQZ8CrAAJLBQACpyNwSkWIaK7tlgfnJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 16-Dars. while va do...while haqida  ')

    elif message.text=='17-dars':
        file_id = 'BAACAgIAAxkBAAIVmWJhP1WI7QeDK-Cfe6z958ryikxUAAL2BQACmrrASVcoLqSfYSfNJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 17-Dars. break va continue ko\'rsatmalari haqida. ')

    if message.text=='18-dars':
        file_id = 'BAACAgIAAxkBAAIVm2JhP35tp3Gclw1vMRnFR7PdcFvLAAJwBQACuL9xSne0qRHMIYiUJAQ'
        await message.answer_video(file_id,caption='📹 JavaScript asoslari. 18-Dars. for-in va for-of loop\'lari  haqida.')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.javascrpt.set()
        await message.answer(f"{message.text}",reply_markup=java_scriptlar)

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/watch?v=DFyzRUsLwYE'>LINK</a></b>")
##########################

@dp.message_handler(Text('jQuery'))
async def html(message:Message):
    await message.answer(f"<b>{message.text}:\nHozircha Darslar yuklanmoqda...\n\n❌Bu bo\'lim 'пусто'</b>",reply_markup=jQuery)

#################REACT
@dp.message_handler(Text('React'))
async def html(message:Message):
    await message.answer(f"{message.text}",reply_markup=react_keyboard)
    await ALLSTATE.react.set()

@dp.message_handler(state=ALLSTATE.react)
async def react_def(message:Message,state:FSMContext):
    if message.text=='Abu tech':
        await message.answer(f"{message.text}",reply_markup=abu_tech_keyboard_react)
        await ALLSTATE.abu_tech_react.set()

    elif message.text=='Samar Badriddinov':
        await message.answer(f"{message.text}",reply_markup=samar_react_keyboard)
        await ALLSTATE.samar_react.set()

    elif message.text=='⬆️Ortga':
        await message.answer(f"{message.text}",reply_markup=frontend)
        await state.finish()


@dp.message_handler(state=ALLSTATE.abu_tech_react)
async def abu_tech_reactlari(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIW72JhSogHiNaxERrmFtraeMALkrRVAALMAQAC1lfgRdXdxffmwNpmJAQ'
        await message.answer_video(file_id,caption='01 - ReactJS  (uzbek) kirish _ React nima.mp4')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIW8WJhSrW9g1mIiKM9eHgTSIiD6KgYAALNAQAC1lfgRUktRURHgpx0JAQ'
        await message.answer_video(file_id,caption='02 - ReactJs (o\'zbek tilida) - renderDom haqida.mp4')
    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIW82JhStW2DbE9lyQPHpqvt1qLRpqKAALOAQAC1lfgRWkNUGLst0imJAQ'
        await message.answer_video(file_id,caption='03 - ReactJS (uzbek) - react JSX nima.mp4 ')
    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIW9WJhSvaCQMepLMfl7Wjcl_dwzxJPAALPAQAC1lfgRRnB-Or-vkT2JAQ'
        await message.answer_video(file_id,caption='04 - Reactjs (o\'zbek) - react components.mp4 ')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIW92JhSxzNKnsdpcU1AVvgfhbSv8xcAALQAQAC1lfgRWHyU3m_cGyVJAQ'
        await message.answer_video(file_id,caption='05 - Reactjs (uz) State.mp4 ')

    elif message.text=='6-dars':
        file_id = 'BAACAgEAAxkBAAIW-WJhS0vNvGtM-_FiUqNI2cmwpwEaAALRAQAC1lfgRfasFCaAUYsoJAQ'
        await message.answer_video(file_id,caption='📹 06 - React Lifecycle uz.mp4 ')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIW-2JhS2c6j4WPzEvj11Ari15JFliFAALSAQAC1lfgRfJ2SLmVzceGJAQ'
        await message.answer_video(file_id,caption='📹 07 - React uzbek - Form va event boshqaruvi.mp4')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIW_WJhS4ZEcR28rnB5h8HPg0Bm5gbkAALTAQAC1lfgRTXn1hxqQqLBJAQ'
        await message.answer_video(file_id,caption='📹 08 - Reactjs (uzbek) - Conditional Rendering.mp4   ')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIW_2JhS6hbI7VcVboc4ht9YSu52FP5AALUAQAC1lfgRa5REd7wnXQ8JAQ'
        await message.answer_video(file_id,caption='📹 09 - Reactjs router haqida uzbek tilida.mp4 ')
    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIXQmJhT9entPwa-xvV0EAUGA4-aMWaAALVAQAC1lfgRe68aI-O5TBqJAQ'
        await message.answer_video(file_id,caption='📹 10 - Fetch get - reactjs uzbek.mp4 ')
    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIXRGJhT_Wve2_BV37eqYVjFyTp1YztAALWAQAC1lfgRRmB6_x6BbgQJAQ'
        await message.answer_video(file_id,caption='📹 11 - REACT.JS - FETCH POST _ O\'ZBEKCHA REACT JS DARSLARI.mp4 ')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIXRmJhUBz0QUDREPiMKArgCP7paYPiAALXAQAC1lfgRfi17p7_DSpTJAQ'
        await message.answer_video(file_id,caption='📹 12 - 12.Axios Get Post.mp4 ')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIXSGJhUDdS7cYae14fdDoh5LHcgowgAALYAQAC1lfgRd6XocIXaRr0JAQ'
        await message.answer_video(file_id,caption='📹 13 - React.js - Style uzbekcha.mp4 ')

    elif message.text=='14-dars':
        file_id = 'BAACAgEAAxkBAAIXSmJhUFMEsE6AOazLtIun6TxrOevHAALZAQAC1lfgRfuEBo3UZGgYJAQ'
        await message.answer_video(file_id,caption='📹 14 - React master class darslari haqida _ Professional react darslari.mp4')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.react.set()
        await message.answer(f"{message.text}",reply_markup=react_keyboard)

@dp.message_handler(state=ALLSTATE.samar_react)
async def abu_tech_reactlari(message:Message,state:FSMContext):
    if message.text=='1-dars':
        file_id = 'BAACAgEAAxkBAAIXcWJhUr3MKhtcCAVM_0twERnNZPYVAAJoAgACXrVJRVFShSeA8Q1GJAQ'
        await message.answer_video(file_id,caption='01 - ReactJS to\'liq kurs _ ReactJS darslar _ Kurs haqida batafsil ma\'lumot.mp4')

    elif message.text=='2-dars':
        file_id = 'BAACAgEAAxkBAAIXc2JhUvk_TYqNjlHtOVazFkIWt-EeAAJpAgACXrVJRcwHcO2fUpD2JAQ'
        await message.answer_video(file_id,caption='02 - ReactJS nima _ ReactJS darslari _ ReactJS 2-dars.mp4')
    elif message.text=='3-dars':
        file_id = 'BAACAgEAAxkBAAIXdWJhUz4ue0VVWLbukZeusd9SyXWVAAJqAgACXrVJReUupOkMF2PUJAQ'
        await message.answer_video(file_id,caption='03 - ReactJS UI Kutubxona _ Funktsiya, Class Component _ ReactJS darslari _ ReactJS 3-dars.mp4')
    elif message.text=='4-dars':
        file_id = 'BAACAgEAAxkBAAIXd2JhU3sphw1-6LrGH9bava1rBtAMAAJrAgACXrVJRaa117HCGoBPJAQ'
        await message.answer_video(file_id,caption='04 - ReactJS props _ ReactJS darslari _ ReactJS 4-dars.mp4')

    elif message.text=='5-dars':
        file_id = 'BAACAgEAAxkBAAIXeWJhU8hDqOG_jCAv06Gdtu-e59NZAAJtAgACXrVJRYuE5VnNkYM9JAQ'
        await message.answer_video(file_id,caption='05 - ReactJS ma\'lumotlarni tartiblash _ ReactJS darslari _ ReactJS 5-dars.mp4 ')

    elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIXe2JhU_SgKbLaM3fC2HPRwf9Xw2dmAAL6DgACdluhS3hHrWm4Uy1ZJAQ'
        await message.answer_video(file_id,caption='📹 6 - ReactJS hook UseMemo, Qidiruv Tizimi || ReactJS darslari || ReactJS 6-dars ')

    elif message.text=='7-dars':
        file_id = 'BAACAgEAAxkBAAIXfWJhVDvWYSvh2VWo2pq7wdcob8svAAJwAgACXrVJRes6_5rpkmmQJAQ'
        await message.answer_video(file_id,caption='📹 07 - ReactJS Animatsiya bilan ishlash _ ReactJS darslari _ ReactJS 7-dars.mp4')

    elif message.text=='8-dars':
        file_id = 'BAACAgEAAxkBAAIXf2JhVHOpQdL6XRMi-Klg7Um9bf95AAJyAgACXrVJRVRAqIk8bst9JAQ'
        await message.answer_video(file_id,caption='📹 08 - ReactJS modal oyna _ ReactJS darslari _ ReactJS 8-dars.mp4 ')

    elif message.text=='9-dars':
        file_id = 'BAACAgEAAxkBAAIXgWJhVKUPpCYm2FsgzxT6uV-GsqTOAAJ0AgACXrVJRWRQL3eCltvzJAQ'
        await message.answer_video(file_id,caption='📹 09 - ReactJS Shaxsiy huklar _ ReactJS darslari _ ReactJS 9-dars.mp4 ')
    elif message.text=='10-dars':
        file_id = 'BAACAgEAAxkBAAIXQmJhT9entPwa-xvV0EAUGA4-aMWaAALVAQAC1lfgRe68aI-O5TBqJAQ'
        await message.answer_video(file_id,caption='📹 10 - Fetch get - reactjs uzbek.mp4 ')
    elif message.text=='11-dars':
        file_id = 'BAACAgEAAxkBAAIXg2JhVPXPJPzEmSCzjK3lDDV5enIQAAJ4AgACXrVJRWA4qWfYi064JAQ'
        await message.answer_video(file_id,caption='📹11 - ReactJS Pagination _ ReactJS Darslari _ ReactJS 11-dars.mp4 ')

    elif message.text=='12-dars':
        file_id = 'BAACAgEAAxkBAAIXhWJhVR5PA4x-0chVLRUIWdtmWyC7AAJ5AgACXrVJRSTUkdnOI_1JJAQ'
        await message.answer_video(file_id,caption='📹 12 - ReactJS React Router Dom kutubxonasi_ ReactJS darslari _ ReactJS 12-dars.mp4 ')

    elif message.text=='13-dars':
        file_id = 'BAACAgEAAxkBAAIXh2JhVTu9Zped1Mzhkmg_HNZOAtXtAAJ7AgACXrVJRYNZUYNoTQ6xJAQ'
        await message.answer_video(file_id,caption='📹 13 - ReactJS Ro\'yhatdan o\'tish _ ReactJS darslar _ ReactJS 13-dars.mp4')

    elif message.text=='14-dars':
        file_id = 'BAACAgEAAxkBAAIXiWJhVXoz21aRxdSwk3sMIe1oFR-YAAJ-AgACXrVJRZlL-UBelJ0tJAQ'
        await message.answer_video(file_id,caption='📹 14 - ReactJS O\'yin loyihasi _ ReactJS darslar _ ReactJS 14-dars.mp4')

    elif message.text=='15-dars':
        file_id = 'BAACAgEAAxkBAAIXi2JhVZJimIeV1n00maZgPjrgPuTKAAKAAgACXrVJRb4dHFjGZuB9JAQ'
        await message.answer_video(file_id,caption='📹 15 - ReactJS API ulash _ ReactJS darslari _ ReactJS 15-dars.mp4')

    elif message.text=='16-dars':
        file_id = 'BAACAgEAAxkBAAIXjWJhVcGrq1GkBTpvLVe2iP9BFTLxAAKBAgACXrVJRa6uO1cSF0LrJAQ'
        await message.answer_video(file_id,caption='📹 16 - ReactJS Sticker ko\'rsatish _ ReactJS darslari _ ReactJS 16-dars.mp4  ')

    elif message.text=='17-dars':
        file_id = 'BAACAgEAAxkBAAIXj2JhVe_C1fHrbx1-FLfOeHWyUv1kAAKCAgACXrVJRaDGYJ965aSsJAQ'
        await message.answer_video(file_id,caption='📹 17 - Redux nima _ Redux darslari _ Redux 1-dars..mp4 ')

    if message.text=='18-dars':
        file_id = 'BAACAgEAAxkBAAIXkWJhVhKo-ogRHWRUrEjBZgRdWhCkAAKDAgACXrVJRRhgNl1TzND7JAQ'
        await message.answer_video(file_id,caption='📹 18 - Redux createStore _ Redux darslari _ Redux 2-dars..mp4')

    elif message.text=='⬆️Ortga':
        await ALLSTATE.react.set()
        await message.answer(f"{message.text}",reply_markup=react_keyboard)

    elif message.text=='Davomi...':
        await message.answer(f"<b>👁 Qolgan videolarni You Tubedan tomosha qiling!\n\n"
                             f"<a href='https://www.youtube.com/channel/UC9Nvv7-5jjzlKRtX8Kfpx4A'>LINK</a></b>")
########################
@dp.message_handler(text='Amaliyot darslar (html/css)')
async def htmlllar(message:Message):
    await message.answer(f"{message.text}",reply_markup=amalyot_key)
    await ALLSTATE.amalyot.set()
@dp.message_handler(state=ALLSTATE.amalyot)
async def amalyotlar(message:Message,state:FSMContext):
     if message.text=='1-dars':
        file_id = 'BAACAgIAAxkBAAIYMWJh5TfzWCLvt0NxBr0U8q8RhoovAALHBgACQHYhSR7DsnFLIqaEJAQ'
        await message.answer_video(file_id,caption='📹 Eid muborak animatisiya yasash , HTML CSS ')

     elif message.text=='2-dars':
        file_id = 'BAACAgIAAxkBAAIYM2Jh5V_ykmSFeXc2hsmZ4KYMBe9HAAKSCAACap8JSSYN5DauzSlfJAQ'
        await message.answer_video(file_id,caption='📹  saytini yasash. HTML va CSS amaliy mashg\'ulot. ')
     elif message.text=='3-dars':
        file_id = 'BAACAgIAAxkBAAIYNWJh5ZAs6G5I53KjauG2a9YkR_k8AAIHCAACtuqZSOVS7ae_6-5cJAQ'
        await message.answer_video(file_id,caption='📹 Calculator yasash - HTML, CSS va Js dan foydalanib, Amaliyot dars ')
     elif message.text=='4-dars':
        file_id = 'BAACAgIAAxkBAAIYN2Jh5bdbxS-6oVbcA8gsAnkM9R0vAAIVDAACGiIZSOEmZj3FUzPJJAQ'
        await message.answer_video(file_id,caption='📹 Amaliyot dars -  Login Page yasash - HTML+CSS va BOOTSTRAPdan foydalanib ')

     elif message.text=='5-dars':
        file_id = 'BAACAgIAAxkBAAIYOWJh5djjC4Ww55OLouULzr4GAo1gAALgBgACnYhBS8Mp6O_YLQ8xJAQ'
        await message.answer_video(file_id,caption='📹 CSS3 5-dars (amaliyot) - HTML ca CSS dan foydalanib template yasash, Web dasturlash ')

     elif message.text=='6-dars':
        file_id = 'BAACAgIAAxkBAAIYO2Jh5fzjkYalvXbbf9Hx2jTZBnt9AAJ5BwACzZZRSfhyR9YtqKfRJAQ'
        await message.answer_video(file_id,caption='📹 📹 Eid muborak animatisiya yasash , HTML CSS JS')

     elif message.text=='⬆️Ortga':
         await state.finish()
         await message.answer(f"{message.text}",reply_markup=frontend)
###################################################################
@dp.message_handler(Text('⬆️Ortga'))
@dp.message_handler(Text('🏠Asosiy Menyu'))
async def bosh(message:Message):
    await message.answer(f"{message.text}",reply_markup=bosh_sahifa)