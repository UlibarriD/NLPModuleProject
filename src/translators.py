# For the two translators rapid api will be used
import requests
import os
import json
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
key = os.getenv('key')


class GoogleTranslate:
    def __init__(self):
        """Naming dunder: https://towardsdatascience.com/whats-the-meaning-of-single-and-double-underscores-in-python-3d27d57d6bd1
        so these should be single underscore
        
        also, if you copied this code from somewhere, be sure to cite that source! 
        """
        self.__url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        self.__headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

    def translate(self, phrase):
        translation = f'q={phrase}&target=en&source=es'
        response = requests.request(
            "POST", self.__url, data=translation, headers=self.__headers)
        json_response = json.loads(response.text)
        return json_response['data']['translations'][0]['translatedText']


class MicrosoftTranslator:
    def __init__(self):
        self.__url = "https://microsoft-translator-text.p.rapidapi.com/translate"
        self.__headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
        }
        self.__querystring = {"to[0]": "en", "api-version": "3.0",
                              "profanityAction": "NoAction", "textType": "plain"}

    def translate(self, phrase):
        translation = [{"Text": phrase}]
        response = requests.request(
            "POST", self.__url, json=translation, headers=self.__headers, params=self.__querystring)
        json_response = json.loads(response.text)
        return json_response[0]['translations'][0]['text']
