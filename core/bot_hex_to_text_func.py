from telegram import Update
from telegram.ext import CallbackContext

from core.utils import _hex_to_text


def hex_to_text(update: Update, context: CallbackContext):
    text = update.message.text
    text_decoded = _hex_to_text(text)
    update.message.reply_text(
        f"""
            {text_decoded}
        """
    )
