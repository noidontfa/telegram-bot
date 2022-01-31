from googletrans import Translator
from googletrans.models import Translated


def _translate(text: str, dest="vi", src=None) -> Translated:
    translator = Translator()
    lang = src
    if not lang:
        detected = translator.detect(text)
        lang = detected.lang
    translation = translator.translate(text, src=lang, dest=dest)
    return translation


def _hex_to_text(hex_str: str) -> str:
    return bytearray.fromhex(hex_str).decode()
