from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAADBQADwQIAAgsnYFQgp59vWmBXLAIQ")
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name}! Hii
I am powerful VC music Bot..🔥
I can play songs in your group's VC 😉

To listen songs also add @munna_vc_robot to your group..

And don't forgot to promote me with all rights..😉
Otherwise I can't play songs..🙄

Use the buttons below to know more about me..🔥
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "мү σωηεя🔥", url="https://t.me/sedxd",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "σғғιcιαℓ gяσυρ🔥", url="https://t.me/X_F0RCE_TEAM"
                    ),
                    InlineKeyboardButton(
                        "αвσυт мυηηα🔥", url="https://t.me/aboutmunna"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Commands", url="https://telegra.ph/𝐌𝐔𝐍𝐍𝐀-𝐓𝐑𝐈𝐏𝐀𝐓𝐇𝐈-04-18"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/munna_vc_robot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
