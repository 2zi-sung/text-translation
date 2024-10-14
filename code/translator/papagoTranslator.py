import requests

class PapagoTranslator:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def translateLang(self, text, src_lang, dest_lang):
        url = "https://openapi.naver.com/v1/papago/n2mt"

        headers = {
            "X-Naver-Client-Id": self.client_id,
            "X-Naver-Client-Secret": self.client_secret,
        }

        data = {
            "source": src_lang,
            "target": dest_lang,
            "text": text,
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            result = response.json()
            return result['message']['result']['translatedText']
        
        else:
            return "Error: " + str(response.status_code)