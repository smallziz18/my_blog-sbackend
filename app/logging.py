import os
from loguru import logger
from app.core.config import settings

# Reset default logger
logger.remove()

# Logs directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")

LOG_FORMAT = (
    "{time:YYYY-MM-DD HH:mm:ss} | "
    "{level: <8} | "
    "{name}:{function}:{line} - "
    "{message}"
)

# Debug / Info logs
logger.add(
    sink=os.path.join(LOG_DIR, "debug.log"),
    format=LOG_FORMAT,
    level="DEBUG" if settings.ENVIRONMENT == "dev" else "INFO",
    filter=lambda record: record["level"].no <= logger.level("WARNING").no,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
)

# Error logs
logger.add(
    sink=os.path.join(LOG_DIR, "error.log"),
    format=LOG_FORMAT,
    level="ERROR",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    backtrace=True,
    diagnose=True,
)

def get_logger():
    return logger
