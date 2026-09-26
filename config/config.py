import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base config"""

    DEBUG = False

    SEED_DATA = False


class ProductionConfig(Config):
    """production config"""


class DevelopmentConfig(Config):
    """development config"""

    DEBUG = True
    SEED_DATA = True
