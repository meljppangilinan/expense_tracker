from email_parser import get_email_attachments
from project import setup_project


def main():
    setup_project()
    get_email_attachments()
    print('---- DONE ----')


if __name__ == '__main__':
    main()
