# For the two translators rapid api will be used
# Snippets of Rapid Api code were used to generate these classes
import requests
import os
import json
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
key = os.getenv('key')


class GoogleTranslate:
    def _init_(self):
        self.__url: str = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        self.__headers: dict = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

    def translate(self, phrase) -> str:
        translation = f'q={phrase}&target=en&source=es'
        response = requests.request(
            "POST", self.__url, data=translation, headers=self.__headers)
        json_response = json.loads(response.text)
        return json_response['data']['translations'][0]['translatedText']


class MicrosoftTranslator:
    def _init_(self):
        self.__url: str = "https://microsoft-translator-text.p.rapidapi.com/translate"
        self.__headers: dict = {
            "content-type": "application/json",
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
        }
        self.__querystring = {"to[0]": "en", "api-version": "3.0",
                              "profanityAction": "NoAction", "textType": "plain"}

    def translate(self, phrase) -> str:
        translation = [{"Text": phrase}]
        response = requests.request(
            "POST", self.__url, json=translation, headers=self.__headers, params=self.__querystring)
        json_response = json.loads(response.text)
        return json_response[0]['translations'][0]['text']
