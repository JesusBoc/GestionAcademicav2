class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'