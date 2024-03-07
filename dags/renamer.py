import os
import re

def rename_downloads():
    dl_dir = os.path.join(os.getcwd(), 'diels')
    print(dl_dir)

    for dir, subd, file in os.walk(dl_dir):
        for f in file:
            m = re.search('(?P<fn>TickData_structure|TC_structure)\.dat', f)
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAA ==================================================')
            print(m.group('fn'))


if __name__ == '__main__':
    rename_downloads()

# python3 dags/renamer.py
