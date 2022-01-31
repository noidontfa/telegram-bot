import prettytable as pt
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from core import services
from core.models import Language
from core.utils import _translate


def translate(update: Update, context: CallbackContext):
    args = context.args
    if not len(args):
        update.message.reply_text("Invalid command: no input")
        return
    text = " ".join(args)
    user_id = update.message.chat.id
    translation_default = services.get_translation_default(user_id=user_id)
    translation = _translate(
        text, src=translation_default.src, dest=translation_default.dest
    )
    update.message.reply_html(
        f"""
        {translation.text}
    """
    )


def default_translate(update: Update, context: CallbackContext):
    text = update.message.text
    if not text:
        return
    user_id = update.message.chat.id
    translation_default = services.get_translation_default(user_id=user_id)
    translation = _translate(
        text, src=translation_default.src, dest=translation_default.dest
    )
    update.message.reply_text(
        f"""
        {translation.text}
    """
    )


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def list_language(update: Update, context: CallbackContext):
    table = pt.PrettyTable(["Name", "Code"])
    table.align["Name"] = "l"
    table.align["Code"] = "l"
    for lang in Language.objects.all():
        table.add_row([lang.name, lang.code])
    update.message.reply_text(f"```{table}```", parse_mode=ParseMode.MARKDOWN_V2)


def set_translation_default(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    src = context.args[0]
    dest = context.args[1]
    translation_default = services.set_translation_default(
        user_id=user_id, src=src, dest=dest
    )
    table = pt.PrettyTable(["Source", "Destination"])
    table.add_row(
        [
            f"{translation_default.src_name} / {translation_default.src}",
            f"{translation_default.dest_name} / {translation_default.dest}",
        ]
    )
    update.message.reply_text(f"```{table}```", parse_mode=ParseMode.MARKDOWN_V2)


def get_translation_default(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    translation_default = services.get_translation_default(user_id)
    table = pt.PrettyTable(["Source", "Destination"])
    table.add_row(
        [
            f"{translation_default.src_name} / {translation_default.src}",
            f"{translation_default.dest_name} / {translation_default.dest}",
        ]
    )
    update.message.reply_text(f"```{table}```", parse_mode=ParseMode.MARKDOWN_V2)
