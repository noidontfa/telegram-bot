from django.conf import settings
from telegram.ext import CommandHandler, Filters, MessageHandler
import logging

from core.bot_core import TelegramBot
from core.bot_translation_func import hello, translate, default_translate, list_language, set_translation_default, \
    get_translation_default

logger = logging.getLogger(__name__)


class TranslationBot(TelegramBot):
    token = settings.TRANSLATION_BOT_TOKEN

    def init_event(self):
        self.add_handler(self.hello_command())
        self.add_handler(self.translate_command())
        self.add_handler(self.list_language_command())
        self.add_handler(self.set_translation_default_command())
        self.add_handler(self.get_translation_default_command())
        self.add_handler(self.default_command())

    @classmethod
    def hello_command(cls) -> CommandHandler:
        return CommandHandler('hello', hello)

    @classmethod
    def translate_command(cls) -> CommandHandler:
        return CommandHandler('translate', translate)

    @classmethod
    def default_command(cls) -> MessageHandler:
        return MessageHandler(Filters.text, default_translate)

    @classmethod
    def list_language_command(cls) -> CommandHandler:
        return CommandHandler('list_language', list_language)

    @classmethod
    def set_translation_default_command(cls) -> CommandHandler:
        return CommandHandler('set_translation_default', set_translation_default)

    @classmethod
    def get_translation_default_command(cls) -> CommandHandler:
        return CommandHandler('get_translation_default', get_translation_default)
