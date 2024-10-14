import os
from codes.dataReader.rawDataReader import RawDataReader
from codes.preprocessor.characterProcessor import CharacterProcessor
from codes.resultManager.resultSaver import ResultSaver
from codes.translator.googleTranslator import GoogleTranslator
from codes.translator.papagoTranslator import PapagoTranslator

class WrapperTranslator:
    def __init__(self, data_path, translator_type):
        self.data_path = data_path
        self.data_loader = RawDataReader(data_path)
        self.char_processor = CharacterProcessor()

        if translator_type == "google":
            self.translator_instance = GoogleTranslator()
        elif translator_type == "papago":
            self.translator_instance = PapagoTranslator()

    def run(self, filename, save_result_folder):
        raw_data = self.data_loader.loadSingleRawData(filename)

        src_lang = 'en'
        dest_lang = 'ko'
        translated_data = []

        for df, filename in raw_data:
            df['translation_result'] = df['word'].apply(lambda text: text if self.char_processor.hasKorean(text) else self.translator_instance.translateLang(text, src_lang, dest_lang))
            df['translation_result'] = df['translation_result'].apply(lambda text: self.char_processor.replaceText(text, "RAW", "생"))
            df['translation_result'] = df['translation_result'].apply(lambda text: self.char_processor.replaceText(text, "Raw", "생"))
            translated_data.append((df, filename))

        save_folder_path = os.path.join(save_result_folder, "translatedData")

        if not os.path.exists(save_folder_path):
            os.makedirs(save_folder_path)

        saver = ResultSaver(save_folder_path)

        for df, original_filename in translated_data:
            file_base_name = os.path.splitext(original_filename)[0]
            file_name = f"translated_{file_base_name}"
            saver.save(df, file_name, "excel")