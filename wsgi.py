import config
from app import create_app
from app.utility.logger import logger

app = create_app(config=config.config_dict['development'])
logger.info('Flask server instantiated and configured successfully')


if __name__ == "__main__":
    app.run()
