from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAADBQADCAIAAu2miygAAadRdNRrAdoC")
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name}! Hii
I am powerful VC music Bot..š„
I can play songs in your group's VC š

To listen songs also add @munna_vc_robot to your group..

And don't forgot to promote me with all rights..š
Otherwise I can't play songs..š

Use the buttons below to know more about me..š„
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Š¼ŅÆ ĻĻĪ·ĪµŃš„", url="https://t.me/sedxd",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ĻŅŅĪ¹cĪ¹Ī±ā gŃĻĻĻš„", url="https://t.me/X_F0RCE_TEAM"
                    ),
                    InlineKeyboardButton(
                        "Ī±Š²ĻĻŃ Š¼ĻĪ·Ī·Ī±š„", url="https://t.me/aboutmunna"
                    ),
                    InlineKeyboardButton(
                        "āļø cĻŠ¼Š¼Ī±Ī·ās", url="https://telegra.ph/ššššš-šššššššš-04-18"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ā Ī±āā ŃĻ ŅÆĻĻŃ gŃĻĻĻ ā", url="https://t.me/munna_vc_robot?startgroup=true"
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
        "šš»āāļø Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ā", callback_data="close"
                    )
                ]
            ]
        )
    )
