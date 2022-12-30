import os
from dotenv import load_dotenv
from imap_tools import AND

load_dotenv()  # take environment variables from .env.

ATTACHMENT_PATH = os.path.join(os.getcwd(), 'attachments')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
IMAP_SERVER = os.getenv('IMAP_SERVER', 'imap.gmail.com')
# supported banks: RAK, ENBD, FAB, CBD
BANK = 'CBD'


BANK_CONFIGS = {
    'FAB': {
        'filter': AND(from_='estatement@bankfab.com')
    },
    'ENBD': {
        'filter': AND(from_='statement@emiratesnbd.com', subject='Emirates NBD E-Statement for CURRENT ACCOUNT')
    },
    'RAK': {
        'filter': AND(from_='estatement@rakbank.ae')
    },
    'CBD': {
        'filter': AND(from_='estatements@cbdstatements.ae')
    }
}

BANK_CONFIG = BANK_CONFIGS[BANK]