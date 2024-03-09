import logging
from datetime import datetime
import os

def get_daily_log(level=logging.INFO):
    format = '%(levelname)s %(asctime)s: %(message)s'
    date = datetime.now().strftime('%Y%m%d')
    logging.basicConfig(format=format, level=level)
    return logging.getLogger(f"{date}")
