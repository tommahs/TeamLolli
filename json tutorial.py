import json

json_string = {
    "name": "name_tweeter",
    "date":"date_tweeter",
    "message":"message_tweeter"
    }

with open('filename.json') as data_file:
    data = json.load(data_file)

## load data from a .json file ^^


