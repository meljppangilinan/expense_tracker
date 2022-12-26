import os.path

from imap_tools import MailBox, MailMessage, BaseMailBox
from progressbar import progressbar

from config import PASSWORD, EMAIL, IMAP_SERVER, ATTACHMENT_PATH, BANK_CONFIG, BANK


def fetch_emails(mailbox: BaseMailBox):
    filters = BANK_CONFIG["filter"]
    return mailbox.fetch(filters)

def save_attachment_to_local(email: MailMessage):
    for att in email.attachments:
        unique_filename = f"{BANK.lower()}-{email.date.strftime('%m-%d-%Y')}.pdf"
        filepath = os.path.join(ATTACHMENT_PATH, unique_filename)
        with open(filepath, 'wb') as file:
            file.write(att.payload)


def get_email_attachments():
    with MailBox(IMAP_SERVER).login(EMAIL, PASSWORD) as mailbox:
        for email in progressbar(fetch_emails(mailbox)):
            save_attachment_to_local(email)
