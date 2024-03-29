from decouple import config


class Config:
    TESTING = False
    MAIL_SERVER = config('MAIL_SERVER')
    MAIL_PORT = config('MAIL_PORT')
    MAIL_USE_SSL = config('MAIL_USE_SSL')
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = config('MAIL_DEFAULT_SENDER')
    # MAIL_DEBUG = config('MAIL_DEBUG')


class DevConfig(Config):
    DB_HOST = config('MONGODB_URI'),
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    CELERY_BROKER_URL = config('CELERY_BROKER_URL')
    RESULT_BACKEND = config('RESULT_BACKEND')


class ProdConfig(Config):
    DB_HOST = config('MONGODB_URI'),
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    DEBUG = False


class TestConfig(Config):
    TESTING = True
    DB_HOST = config('LOCAL_DB')
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    CELERY_BROKER_URL = config('CELERY_BROKER_URL')
    RESULT_BACKEND = config('RESULT_BACKEND')


config_dict = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}
