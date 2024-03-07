import pandas as pd
import os
import re

def record(date):
    home = os.getcwd()
    dir = os.path.join(home, 'details')
    dic = {
        'Tick': None,
        'Tick Data Structure': None,
        'Trade Cancellation': None,
        'Trade Cancellation Data Structure': None
    }

    tracker = None

    for dir, subd, file in os.walk(dir):
        for f in file:
            m = re.search('.+\.parquet', f)
            if m == None:
                continue

            tracker = m.group()

    if tracker == None:
        pd.DataFrame(dic, index=date).to_parquet(os.path.join(home, 'details/') + 'tracker.parquet')
    else:
        tracker = pd.read_parquet(os.path.join(home, 'details/') + tracker)
        curr = pd.DataFrame(dic, index=date)
        pd.concat([tracker, curr]).to_parquet(os.path.join(home, 'details/') + 'tracker.parquet')

    return tracker

if __name__ == '__main__':
    print(record(['20240312']))
