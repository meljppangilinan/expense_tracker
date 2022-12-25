import os

from config import ATTACHMENT_PATH


def create_attachment_folder_if_not_exists(attachment_path):
    if not os.path.isdir(attachment_path):
        os.makedirs(attachment_path, exist_ok=True)


def setup_project():
    create_attachment_folder_if_not_exists(ATTACHMENT_PATH)

