from decouple import config


class Config:
    TESTING = False


class DevConfig(Config):
    MONGODB_SETTINGS = {
        'host': config('MONGODB_URI'),
        'connect': False
    }
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    MAIL_SERVER = config('MAIL_SERVER')
    MAIL_PORT = config('MAIL_PORT')
    MAIL_USE_TLS = config('MAIL_USE_TLS')
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    # MAIL_DEBUG = config('MAIL_DEBUG')


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
