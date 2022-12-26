import os.path

from imap_tools import MailBox, AND

from config import PASSWORD, EMAIL, IMAP_SERVER, ATTACHMENT_PATH


def fetch_emails(mailbox):
    # TODO: IMPORT FROM 
    # filters = AND(from_='statement@emiratesnbd.com', subject='Emirates NBD E-Statement for CURRENT ACCOUNT')
    filters = AND(from_='estatement@bankfab.com')
    for msg in mailbox.fetch(filters):
        yield msg


def save_attachment_to_local(email):
    for att in email.attachments:
        filepath = os.path.join(ATTACHMENT_PATH, att.filename)
        with open(filepath, 'wb') as file:
            file.write(att.payload)


def get_email_attachments():
    with MailBox(IMAP_SERVER).login(EMAIL, PASSWORD) as mailbox:
        for email in fetch_emails(mailbox):
            save_attachment_to_local(email)
