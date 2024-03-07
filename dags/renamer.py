import os
import re
from datetime import datetime

def rename_downloads():
    dl_dir = os.path.join(os.getcwd(), 'diels')
    print(dl_dir)

    for dir, subd, file in os.walk(dl_dir):
        for f in file:
            m = re.search('(?P<fn>TickData_structure|TC_structure)\.dat', f)
            filename = m.group('fn')
            date = datetime.now()
            strdate = date.strftime('%Y%m%d')
            new_fn = f"{filename}_{strdate}"
            os.rename(f"{dl_dir}/{filename}.dat", f"{dl_dir}/{new_fn}.dat")


if __name__ == '__main__':
    rename_downloads()

# python3 dags/renamer.py
