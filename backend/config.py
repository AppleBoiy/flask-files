import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    MAX_CONTENT_LENGTH = int(eval(os.getenv('MAX_CONTENT_LENGTH')))
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
