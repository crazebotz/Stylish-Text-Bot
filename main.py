from config import Config
from pyrogram import Client 


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "Stylish_text_bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
    )
    print("BOT HAS RUNNING SUCCESFULLY")
    app.run()
