import config
from app import create_app

app = create_app(config=config.config_dict['development'])


if __name__ == "__main__":
    app.run()
