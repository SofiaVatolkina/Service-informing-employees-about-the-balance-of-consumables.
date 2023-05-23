import json

import tgConnector
import dbConnector

# import settings from file on the server.
filename = 'settings.json'
settingsFile = open(filename, 'r', encoding='utf-8')
parsedJson = json.load(settingsFile)
api_key = parsedJson['api_key']
list_of_consumables_btn = parsedJson['list_of_consumables_btn']
list_of_service_btn = parsedJson['list_of_service_btn']
settingsFile.close

# init bot.
tgConnector.TG(api_key=api_key, consumables_list=list_of_consumables_btn, service_list=list_of_service_btn)

# init db.