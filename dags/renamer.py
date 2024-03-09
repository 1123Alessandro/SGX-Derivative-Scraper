import os
import re
from datetime import datetime
from dataframer import read_parq, save_parq
import logging
from logs import *
logger = get_daily_log()

def rename_downloads():
    logger.info('renaming downloads')
    dl_dir = os.path.join(os.getcwd(), 'diels')
    tracker = read_parq()
    rec = tracker[tracker.isna().any(axis=1)]
    if rec.shape[0] == 0:
        return None
    strdate = rec.index[0]

    for dir, subd, file in os.walk(dl_dir):
        for f in file:
            m = re.search('(?P<fn>TickData_structure|TC_structure)\.dat', f)
            if m == None:
                continue
            filename = m.group('fn')
            new_fn = f"{filename}_{strdate}"
            os.rename(f"{dl_dir}/{filename}.dat", f"{dl_dir}/{new_fn}.dat")

    for i in ['Tick', 'Tick Data Structure', 'Trade Cancellation', 'Trade Cancellation Data Structure']:
        rec[i] = 'Okay'
    tracker.loc[rec.index] = rec
    save_parq(tracker)

def move_downloads():
    logger.info('moving downloads')
    dl_dir = os.path.join(os.getcwd(), 'diels')
    archive_dir = os.path.join(os.getcwd(), 'archive')

    for dir, subd, file in os.walk(dl_dir):
        for f in file:
            m = re.search('.+\..+', f)
            filename = m.group()

            os.rename(f"{dl_dir}/{filename}", f"{archive_dir}/{filename}")

if __name__ == '__main__':
    move_downloads()
    # rename_downloads()

# python3 dags/renamer.py
