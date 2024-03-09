import logging
from datetime import datetime
import os

def get_daily_log(level):
    format = '%(levelname)s\t%(asctime)s: %(message)s'
    # level = logging.DEBUG
    date = datetime.now().strftime('%Y%m%d')
    filename = os.path.join(os.getcwd(), 'details/') + date
    logging.basicConfig(format=format, level=level, filename=f"{filename}.log")
    return logging.getLogger(f"{date}")
