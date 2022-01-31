from django.contrib import admin

from core.models import DefaultTranslation, Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(DefaultTranslation)
class DefaultTranslationAdmin(admin.ModelAdmin):
    pass
