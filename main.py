import os
from pyrogram import Client, filters
from font import Fonts
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant

TOKEN=os.environ.get("BOT_TOKEN", '5852639486VV')
API_ID = int(os.environ.get("API_ID",'28160559'))
API_HASH= os.environ.get("API_HASH", 'ca5085c3f41b16df46dbeebed6e56081')


app = Client(
        "Stylish_text_bot",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        workers=20
    )



buttons = [
        [
            InlineKeyboardButton('π£Update Channelπ§βπ»', url="https://t.me/crazebots")
        ]
    ]

@app.on_message(filters.command('start'))
async def start(_, m):
        # start text
    text = f"""Hlw! {m.from_user.mention(style='md')}.

** I am Stylish Text Bot**

`I can help you to get stylish fonts. Just send me some text and see magic.`

**π² Made by :** @CrazeBots
"""
    # Buttons
   
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

async def forceSub(app, msg):
    try:
        await app.get_chat_member('crazebots', msg.from_user.id)
        return True
    except UserNotParticipant:
        await app.send_message(chat_id=msg.from_user.id, text="**Please Join My Update Channel To Use Me**", reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=msg.id)
        return False
    except:
        return True


@app.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):

    result = await forceSub(c,m)
    if result == False:
        return
    buttons = [[
        InlineKeyboardButton('ππ’πππ πππππ', callback_data='style+typewriter'),
        InlineKeyboardButton('ππ¦π₯ππππ', callback_data='style+outline'),
        InlineKeyboardButton('πππ«π’π', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('πΊππππ', callback_data='style+bold_cool'),
        InlineKeyboardButton('πππππ', callback_data='style+cool'),
        InlineKeyboardButton('Sα΄α΄ΚΚ Cα΄α΄s', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('ππΈππΎππ', callback_data='style+script'),
        InlineKeyboardButton('πΌπ¬π»π²πΉπ½', callback_data='style+script_bolt'),
        InlineKeyboardButton('α΅β±βΏΚΈ', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('αOα°Iα', callback_data='style+comic'),
        InlineKeyboardButton('π¦π?π»π', callback_data='style+sans'),
        InlineKeyboardButton('πππ£π¨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('ππ’π―π΄', callback_data='style+slant'),
        InlineKeyboardButton('π²πΊππ', callback_data='style+sim'),
         InlineKeyboardButton('βΈοΈβΎοΈβοΈβΈοΈβοΈβΊοΈβοΈ', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('ποΈποΈπ‘οΈποΈποΈποΈπ’οΈ', callback_data='style+circle_dark'),
        InlineKeyboardButton('ππ¬π±π₯π¦π ', callback_data='style+gothic'),
        InlineKeyboardButton('π²πππππ', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('CΝ‘ΝlΝ‘ΝoΝ‘ΝuΝ‘ΝdΝ‘ΝsΝ‘Ν', callback_data='style+cloud'),
        InlineKeyboardButton('HΜΜaΜΜpΜΜpΜΜyΜΜ', callback_data='style+happy'),
        InlineKeyboardButton('SΜΜaΜΜdΜΜ', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('Next β‘οΈ', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('πΈβπ΅βπͺβπ¨βπ?βπ¦βπ±β', callback_data='style+special'),
            InlineKeyboardButton('ππππ°ππ΄π', callback_data='style+squares'),
            InlineKeyboardButton('ποΈποΈποΈπ°οΈποΈπ΄οΈποΈ', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('κͺκͺα¦κͺκͺΆκͺα₯΄π²κͺ', callback_data='style+andalucia'),
            InlineKeyboardButton('ηͺεε αε', callback_data='style+manga'),
            InlineKeyboardButton('SΜΎtΜΎiΜΎnΜΎkΜΎyΜΎ', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('BΝ¦Μ₯uΝ¦Μ₯bΝ¦Μ₯bΝ¦Μ₯lΝ¦Μ₯eΝ¦Μ₯sΝ¦Μ₯', callback_data='style+bubbles'),
            InlineKeyboardButton('UΝnΝdΝeΝrΝlΝiΝnΝeΝ', callback_data='style+underline'),
            InlineKeyboardButton('κκκ·κ©κκκ', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('R?a?y?s?', callback_data='style+rays'),
            InlineKeyboardButton('B?i?r?d?s?', callback_data='style+birds'),
            InlineKeyboardButton('SΜΈlΜΈaΜΈsΜΈhΜΈ', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('SΜ·ΜΝΜ¨ΜΜͺΜ«Μ?ΝΜ²tΜ΄ΜΝΜΝΜΜΜΏΜΜΏΝΜ«ΜΌoΜ΄ΜΜΜΜΜΝΜΏΜΊΜpΜΈΝΜΝΜ‘ΜΊΜ³ΝΝΝ' , callback_data='style+stop'),
            InlineKeyboardButton('SΝΜΊkΝΜΊyΝΜΊlΝΜΊiΝΜΊnΝΜΊeΝΜΊ', callback_data='style+skyline'),
            InlineKeyboardButton('AΝrΝrΝoΝwΝsΝ', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('αͺαα­αΏα', callback_data='style+qvnes'),
            InlineKeyboardButton('SΜΆtΜΆrΜΆiΜΆkΜΆeΜΆ', callback_data='style+strike'),
            InlineKeyboardButton('FΰΌrΰΌoΰΌzΰΌeΰΌnΰΌ', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('β¬οΈ Back', callback_data='nxt+0')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@app.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer("TEXT STYLED SUCCESSFULLY")
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(f"**TAP TO COPY:**\n\n`{new_text}`", reply_markup=m.message.reply_markup)
    except:
        pass




os.system("clear")
print("BOT HAS RUNNING SUCCESFULLY")
app.run()
