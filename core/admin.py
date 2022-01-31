from django.contrib import admin

from core.models import Language, DefaultTranslation


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(DefaultTranslation)
class DefaultTranslationAdmin(admin.ModelAdmin):
    pass
