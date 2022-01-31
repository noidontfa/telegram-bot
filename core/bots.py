import logging

from django.conf import settings
from telegram.ext import CommandHandler, Filters, MessageHandler

from core.bot_core import TelegramBot
from core.bot_hex_to_text_func import hex_to_text
from core.bot_translation_func import (
    default_translate,
    get_translation_default,
    hello,
    list_language,
    set_translation_default,
    translate,
)

logger = logging.getLogger(__name__)


class TranslationBot(TelegramBot):
    token = settings.TRANSLATION_BOT_TOKEN

    def init_event(self):
        self.add_handler(self.hello_command)
        self.add_handler(self.translate_command)
        self.add_handler(self.list_language_command)
        self.add_handler(self.set_translation_default_command)
        self.add_handler(self.get_translation_default_command)
        self.add_handler(self.default_command)

    @property
    def hello_command(self) -> CommandHandler:
        return CommandHandler("hello", hello)

    @property
    def translate_command(self) -> CommandHandler:
        return CommandHandler("translate", translate)

    @property
    def default_command(self) -> MessageHandler:
        return MessageHandler(Filters.text, default_translate)

    @property
    def list_language_command(self) -> CommandHandler:
        return CommandHandler("list_language", list_language)

    @property
    def set_translation_default_command(self) -> CommandHandler:
        return CommandHandler("set_translation_default", set_translation_default)

    @property
    def get_translation_default_command(self) -> CommandHandler:
        return CommandHandler("get_translation_default", get_translation_default)


class HexToTextBot(TelegramBot):
    token = settings.HEX_TO_TEXT_BOT_TOKEN

    def init_event(self):
        self.add_handler(self.hex_to_text_command)

    @property
    def hex_to_text_command(self):
        return MessageHandler(Filters.text, hex_to_text)
