
# Watson speech to text translator

# In this program, we will convert an audio file of an English speaker to text using a Speech to Text API.
# Then, will translate the English version to a Spanish version using a Language Translator API.

# WE will need a following library
 pip install ibm_watson wget

# First we import SpeechToTextV1 from ibm_watson

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# For this, we need an IBM Cloud account and create an instance of IBM Speech to Text and IBM Language Translator and obtain their respective API Keys.

url_s2t = " "
iam_apikey_s2t = " "

# Create speech to text adapter object
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# Download the audio file 
wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3


filename='PolynomialRegressionandPipelines.mp3'

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

response.result

from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)

# Import language translator from ibm watson

from ibm_watson import LanguageTranslatorV3
url_lt= ' '
apikey_lt= ' '
version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

translation=translation_response.get_result()
translation

spanish_translation =translation['translations'][0]['translation']
spanish_translation 

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_eng