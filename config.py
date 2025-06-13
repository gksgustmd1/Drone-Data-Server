import os

class Config:
    #python code path define
    DIR_PATH = os.path.abspath(os.path.dirname(__file__))

    #DB path define
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DIR_PATH, 'license.db')

    #sql performance improve
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Flask secret-key
    SECRET_KEY = 'ekdrneo402'

if __name__ == '__main__':
    print(f"DIR_PATH: {Config.DIR_PATH}")
    print(f"SQLALCHEMY_DATABASE_URI: {Config.SQLALCHEMY_DATABASE_URI}")
    print(f"SQLALCHEMY_TRACK_MODIFICATIONS: {Config.SQLALCHEMY_TRACK_MODIFICATIONS}")
    print(f"SECRET_KEY: {Config.SECRET_KEY}")
