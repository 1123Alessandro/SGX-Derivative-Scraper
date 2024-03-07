import json
import os

def to_dict(filename):
    home = os.getcwd()
    dir = os.path.join(home, 'details/')
    jsarr = ''
    with open(dir + filename) as file:
        jsarr = file.readlines()

    jsraw = ''.join(jsarr)
    return json.loads(jsraw)

if __name__ == '__main__':
    print(to_dict('config.json'))
