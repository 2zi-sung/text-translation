from googletrans import Translator
import time

class GoogleTranslator:
    def __init__(self):
        self.google_translator = Translator()
        self.counter = 0

    def translateLang(self, text, src_lang, dest_lang):
        self.counter += 1
        try:
            translation = self.google_translator.translate(text, src=src_lang, dest=dest_lang)
            translation_text = translation.text
            print(f"{self.counter}: {text}")
        except:
            time.sleep(10)
            translation = self.google_translator.translate(text, src=src_lang, dest=dest_lang)
            translation_text = translation.text
            print(f"{self.counter}: {text}")
            
        return translation_text
