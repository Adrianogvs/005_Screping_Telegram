import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = os.getenv('API_ID')
    API_HASH = os.getenv('API_HASH')
    PHONE_NUMBER = os.getenv('PHONE_NUMBER')
    USERNAME = os.getenv('USERNAME')
    START_DATE = os.getenv('START_DATE')
    END_DATE = os.getenv('END_DATE')
    GROUP_URL = os.getenv('GROUP_URL')
