import os
from pyrogram import Client 

TOKEN=os.environ.get("BOT_TOKEN", ' ')
API_ID = int(os.environ.get("API_ID",'1234'))
API_HASH= os.environ.get("API_HASH", ' ')

app = Client(
        "Stylish_text_bot",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins = dict(
        root="plugins"),
        workers=50
    )

print("BOT HAS RUNNING SUCCESFULLY")
app.run()
