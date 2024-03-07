import pandas as pd
import os
import re

def save_parq(df):
    home = os.getcwd()
    df.to_parquet(os.path.join(home, 'details/') + 'tracker.parquet')

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
        save_parq(pd.DataFrame(dic, index=date))
    else:
        tracker = pd.read_parquet(os.path.join(home, 'details/') + tracker)
        curr = pd.DataFrame(dic, index=date)
        save_parq(pd.concat([tracker, curr]))

    return tracker

if __name__ == '__main__':
    print(record(['20240312']))
