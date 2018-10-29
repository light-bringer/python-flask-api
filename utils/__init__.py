import json
import ast



def readJSONtoDict(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

readJSONtoDict('/home/lightbringer/Desktop/python-flask-api/data/imdb.json')