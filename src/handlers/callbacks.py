from telegram import Update
from telegram.ext import CallbackContext
import config

def promocode_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id

    # Проверяем подписку пользователя на канал
    member = context.bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)
    if member.status in ['member', 'administrator', 'creator']:
        query.answer()
        query.edit_message_text("Спасибо за подписку! Ваш промокод: **PROMO2025**")
    else:
        query.answer()
        query.edit_message_text(
            f"Пожалуйста, подпишитесь на канал {config.CHANNEL_ID} и попробуйте снова."
        )
