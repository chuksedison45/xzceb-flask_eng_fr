"""
Translator is used to translate between english and french language
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f'{apikey}')
translator_instance = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator_instance.set_service_url(f'{url}')

def english_to_french(english_text):
    """
    The function translates english text to french
    """
    translation = translator_instance.translate(text=english_text,
    model_id='en-fr').get_result()
    #translation = json.dumps(translation, indent=2, ensure_ascii=False)['translations']
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    The function translates french text to english text
    """
    translation = translator_instance.translate(text=french_text,
    model_id='fr-en').get_result()
    #translation = json.dumps(translation, indent=2, ensure_ascii=False)['translations']
    english_text = translation['translations'][0]['translation']
    return english_text

if __name__ == '__main__':
    print(french_to_english("Bonjour"))
