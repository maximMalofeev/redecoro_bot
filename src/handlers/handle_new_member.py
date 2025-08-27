from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

import config

def handle_new_member(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        keyboard = [
            [InlineKeyboardButton("Получить промокод", callback_data=f"get_promocode_{member.id}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = (
            f"Привет, {member.full_name}!\n\n"
            f"Подпишись на наш канал: {config.CHANNEL_ID}\n"
            "И получи промокод на скидку! 🎁"
        )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
            reply_markup=reply_markup
        )