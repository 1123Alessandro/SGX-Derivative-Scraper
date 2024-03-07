import pandas as pd
import os
import re

def save_parq(df):
    home = os.getcwd()
    df.to_parquet(os.path.join(home, 'details/') + 'tracker.parquet')

def read_parq():
    home = os.getcwd()
    return pd.read_parquet(os.path.join(home, 'details/') + 'tracker.parquet')

def tracker_exists():
    home = os.getcwd()
    dir = os.path.join(home, 'details')
    for dir, subd, file in os.walk(dir):
        for f in file:
            m = re.search('.+\.parquet', f)
            if m != None:
                return True
    return False

def record(date, notfound, dd):
    home = os.getcwd()
    dir = os.path.join(home, 'details')
    val = -1 if notfound else None
    dic = {
        'Tick': val,
        'Tick Data Structure': val,
        'Trade Cancellation': val,
        'Trade Cancellation Data Structure': val,
        'String Date': dd
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
        if tracker[tracker.index == date].shape[0] > 0:
            tracker.loc[date] = curr
        else:
            save_parq(pd.concat([tracker, curr]))

    return tracker

if __name__ == '__main__':
    # print(record(['20240312']))
    print(tracker_exists())
