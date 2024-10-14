import pandas as pd
import re

class CharacterProcessor:
    def __init__(self):
        pass

    def replaceText(self, text, src, dest):
        replaced_text = text.replace(src, dest)

        return replaced_text
    
    def hasKorean(self, text):
        return bool(re.search(r'[가-힣]', text))
    
    def hasEnglish(self, text):
        return bool(re.search(r'[a-zA-Z]', text))