from django.core.management.base import BaseCommand
from googletrans import LANGUAGES

from core.models import Language


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for key, value in LANGUAGES.items():
            Language.objects.get_or_create(name=value, code=key)
        print("Done!")
