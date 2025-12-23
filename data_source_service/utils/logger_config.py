

import logging
import os
import sys
from logging.handlers import RotatingFileHandler


def get_logger(name: str = 'data-source-service'):

    logger = logging.getLogger(name)
    if not logger.handlers:

        # 1. setup console handler
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s'))
        logger.addHandler(console_handler)

        # 2. setup file handler with rotation (max 5MB, keep 3 backup)
        os.makedirs(name='DSS_logs', exist_ok=True)
        file_handler = RotatingFileHandler('./DSS_logs/data_source.log', maxBytes=5242880, backupCount=3)
        file_handler.setFormatter(logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s'))
        logger.addHandler(file_handler)

        logger.setLevel(level=logging.INFO)

    return logger

log = get_logger()
