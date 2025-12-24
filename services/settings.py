import os

from dotenv import load_dotenv

load_dotenv()
agora_app_id = os.getenv('AGORA_APP_ID')
agora_app_certificate = os.getenv('AGORA_APP_CERTIFICATE')