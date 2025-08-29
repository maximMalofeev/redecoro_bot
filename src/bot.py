from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
)
import config
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton(
                "Получить промокод",
                callback_data=f"get_promocode_{update.message.from_user.id}",
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        f"Привет!\n\n"
        f"Подпишись на наш канал: {config.CHANNEL_ID}\n"
        "И получи промокод на скидку! 🎁"
    )
    update.message.reply_text(message, reply_markup=reply_markup)


def promocode_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id

    # Проверяем подписку пользователя на канал
    member = context.bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)
    if member.status in ["member", "administrator", "creator"]:
        query.answer()
        query.edit_message_text(
            "Спасибо за подписку! Ваш промокод: redecoro_new\n\n"
            "Действует в оффлайн магазинах на весь ассортимент товаров бренда Redecoro.\n"
            "Период действия промокода: с 28 августа по 15 сентября.\n"
        )
    else:
        query.answer()
        current_text = query.message.text
        new_message_text = f"Пожалуйста, подпишитесь на канал {config.CHANNEL_ID} и попробуйте снова."
        if current_text == new_message_text:
            return # Avoid updating the message if it's already the same

        keyboard = [
            [
                InlineKeyboardButton(
                    "Получить промокод",
                    callback_data=f"get_promocode_{user_id}",
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(new_message_text, reply_markup=reply_markup)


def main():
    updater = Updater(token=config.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handler for /start command
    dispatcher.add_handler(CommandHandler("start", start))

    # Handler for promocode button
    dispatcher.add_handler(
        CallbackQueryHandler(promocode_callback, pattern=r"get_promocode_.*")
    )

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
