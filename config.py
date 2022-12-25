import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

ATTACHMENT_PATH = os.path.join(os.getcwd(), 'attachments')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
IMAP_SERVER = os.getenv('IMAP_SERVER', 'imap.gmail.com')

