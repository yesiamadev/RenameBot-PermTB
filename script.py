class script(object):
    START_TEXT = """ A Simple And Fastest File Renamer Bot With Permanent Thumbnail support!💯

<b>Send me any Telegram file and choose appropriate option! </b>
For Know More Hit /help.
@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):

#   TRChatBase(update.from_user.id, update.text, "/help")
    buttons = [[
        InlineKeyboardButton('🆘 Help 🆘', callback_data='help'),
        InlineKeyboardButton('Upgrade💸', callback_data='upgrade_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )"""

    RENAME_403_ERR = "What Are You Doing? You are Banned"
    UPGRADE_TEXT = "CONTACT @Ek_comme_nt_bot"
    DOWNLOAD_START = "Give Me Some Time 🙏..."
    UPLOAD_START = "Starting to upload 😝..."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "**Thank you for Using Me. @ekbotz_update.**"
    SAVED_THUMB = "Thumbnail Saved as permanent ✅ This Is Permanent"
    DEL_THUMB = "Thumbnail cleared succesfully!"
    NO_THUMB = "No thumbnails found!😐"
    SAVED_RECVD_DOC_FILE = "File Downloaded Successfully 😎"
    CUSTOM_CAPTION_UL_FILE = " "
    HELP_USER = """It's not that complicated😅
    
<b>1. Send me any Telegram File.
2. Choose appropriate option.
   Enjoy😍.</b>"""

