# NLP-Project
In this repository, three NLP models that are commonly used and required in the industry are integrated
 
## Setting Up
To use the translation model, we must first establish a RapidAPI account: https://rapidapi.com/auth/sign-up
We will eventually need to subscribe to Microsoft Translator Text and Google Translate
https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/microsoft-translator-text/
https://rapidapi.com/googlecloud/api/google-translate1/

Once the account has been formed and subscribed to the appropriate translators, we must generate an.env file with the API key *(the key is found in the code snipets of the translators and is the same for both)*
```
key="APIKEY"
```
Finally, in order to install all of the required libraries and run the code we need to run the following lines:
```
.\nlpproject\Scripts\activate
```
 ```
 pip install -r requirements.txt && python run.py
 ```


## Authors
Diego Armando Ulibarri Hernández
