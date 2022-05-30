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
    MONGODB_SETTINGS = {
        'host': config('MONGODB_URI'),
        'connect': False
    }
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')


class ProdConfig(Config):
    MONGODB_SETTINGS = {
        'host': config('MONGODB_URI'),
        'connect': False
    }
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    DEBUG = False


config_dict = {
    'development': DevConfig,
    'production': ProdConfig
}
