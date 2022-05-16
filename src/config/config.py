from decouple import config


class Config:
    TESTING = False


class DevConfig(Config):
    ATLAS_DB_URI = config('ATLAS_DB_URI')


class ProdConfig(Config):
    ATLAS_DB_URI = config('ATLAS_DB_URI')


config_dict = {
    'development': DevConfig,
    'production': ProdConfig
}
