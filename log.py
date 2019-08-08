import sys
import logging

from config import APP_ENV


logging.basicConfig(level=config.LOG_LEVEL)
LOG = logging.getLogger("API")
LOG.propagate = False

INFO_FORMAT = "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
DEBUG_FORMAT = "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s [in %(pathname)s:%(lineno)d]"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S %z"

if APP_ENV == "live":
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler("logs/app.log", "a", 1 * 1024 * 1024, 10)
    formatter = logging.Formatter(INFO_FORMAT, TIMESTAMP_FORMAT)
    file_handler.setFormatter(formatter)
    LOG.addHandler(file_handler)

if APP_ENV == "dev" or APP_ENV == "local":
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT)
    stream_handler.setFormatter(formatter)
    LOG.addHandler(stream_handler)


def get_logger():
    return LOG
