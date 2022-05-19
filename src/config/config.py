from decouple import config


class Config:
    TESTING = False


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


config_dict = {
    'development': DevConfig,
    'production': ProdConfig
}
