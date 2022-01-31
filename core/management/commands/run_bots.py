from django.core.management.base import BaseCommand

from core.bots import HexToTextBot, TranslationBot


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        TranslationBot().start()
        HexToTextBot().start()
