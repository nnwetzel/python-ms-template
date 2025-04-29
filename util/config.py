from os import environ
from dotenv import load_dotenv

load_dotenv()

class LocalDevelopmentConfig:
    NLP_SERVICE_HOST = '0.0.0.0'
    NLP_SERVICE_PORT = environ.get('NLP_SERVICE_PORT', '4000')

def get_config():
    return LocalDevelopmentConfig()