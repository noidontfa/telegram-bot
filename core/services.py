from googletrans import LANGUAGES

from core.models import DefaultTranslation


def get_translation_default(user_id: str) -> DefaultTranslation:
    default = DefaultTranslation.objects.filter(user_id=user_id).first()
    if not default:
        default = DefaultTranslation.objects.create(
            user_id=user_id,
            src="en",
            dest="vi",
            src_name="english",
            dest_name="vietnamese",
        )
    return default


def set_translation_default(user_id: str, src="en", dest="vi") -> DefaultTranslation:
    default = get_translation_default(user_id=user_id)
    default.src = src
    default.src_name = LANGUAGES.get(src)
    default.dest = dest
    default.dest_name = LANGUAGES.get(dest)
    default.save()
    return default
