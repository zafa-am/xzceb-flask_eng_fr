"""
This file contains functions for translating between English and French languages.
"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv() # Loads the local environment file as environment

# The following two commands fetch the environment variables
# apikey = os.environ['apikey']
apikey = 'ynYSaj_wbb0LHKSOFtrDSGBuH7IrLsqmgbM5lAt7D0Qh'
# url = os.environ['url']
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/960d829a-c4af-4e7b-9a4b-53684791b4fd'

# Initiate instance of language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
# Set URL
language_translator.set_service_url(url)

def englishToFrench(text):
    """
    Returns the Frech translation of the English phrase in text

    Parameters
    - - - - - -
    text : str
    English text to be translated

    Returns
    - - - -
    str
    French translation
    """
    if text:
        translation = language_translator.translate(text, model_id='en-fr').get_result()
        return translation['translations'][0]['translation']
    return ""

def frenchToEnglish(text):
    """
    Returns the English translation of the French phrase in text

    Parameters
    - - - - - -
    text : str
    Frech text to be translated

    Returns
    - - - -
    str
    English translation
    """
    if text:
        translation = language_translator.translate(text, model_id='fr-en').get_result()
        return translation['translations'][0]['translation']
    return ""


