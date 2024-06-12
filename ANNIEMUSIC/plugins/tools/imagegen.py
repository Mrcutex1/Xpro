from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from MukeshAPI import api
from pyrogram.enums import ChatAction,ParseMode
from ANNIEMUSIC import app

@app.on_message(filters.command("imagine"))
async def imagine_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:

        text =message.text.split(None, 1)[1]
    Jarvis=await message.reply_text( "`Please wait...\n\nGenerating image .....`")
    try:
        await b.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        x=api.ai_image(text)
        with open("mukesh.jpg", 'wb') as f:
            f.write(x)
        caption = f"""
    💘sᴜᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ : {text}

    ✨ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ : [─‌⃛┼𝆺𝅥⃝ᶦϻ‌ ᵛ‌ᵎᵖ ≛⃝ 𝐀𝐫𝐲𝐚𝐧❣️𓆩𝐎𝐰𝐧𝐞𝐫𓆪ꪾ🥀⃝⃪•๋๋๋๋๋๋๋๋๋๋๋๋๋•๋](https://t.me/Ace_networkop)
    🥀ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}
    """
        await Jarvis.delete()
        await message.reply_photo("mukesh.jpg",caption=caption,quote=True)
    except Exception as e:
        await Jarvis.edit_text(f"error {e}")
    

__mod_name__ = "Aɪ ɪᴍᴀɢᴇ"
__help__ = """
 ➻ /imagine : ɢᴇɴᴇʀᴀᴛᴇ Aɪ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛᴇxᴛ
 """
