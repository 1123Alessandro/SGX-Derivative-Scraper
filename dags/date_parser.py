from datetime import datetime
import re

months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

def parse_date(s):
    m = re.search('(?P<day>[0-9]{2}) (?P<month>[a-zA-Z]{3}) (?P<year>[0-9]{4})', s)
    day = int(m.group('day'))
    month = months[m.group('month')]
    year = int(m.group('year'))
    return datetime(day=day, month=month, year=year)

if __name__ == '__main__':
    parse_date('07 Mar 2023')

# python3 dags/date_parser.py
