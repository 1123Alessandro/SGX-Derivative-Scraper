import os
import re
from datetime import datetime
from dataframer import read_parq, save_parq

def rename_downloads():
    dl_dir = os.path.join(os.getcwd(), 'diels')
    print(dl_dir)
    tracker = read_parq()
    rec = tracker[tracker.isna().any(axis=1)]
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
        rec[i] = 1
    tracker.loc[rec.index] = rec
    save_parq(tracker)

if __name__ == '__main__':
    rename_downloads()

# python3 dags/renamer.py
