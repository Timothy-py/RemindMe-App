from decouple import config


class Config:
    TESTING = False


class DevConfig(Config):
    MONGODB_SETTINGS = {
        'host': config('MONGODB_URI'),
        'connect': False
    }


class ProdConfig(Config):
    MONGODB_SETTINGS = {
        'host': config('MONGODB_URI'),
        'connect': False
    }


config_dict = {
    'development': DevConfig,
    'production': ProdConfig
}
