import json

import tgConnector
import dbConnector

# Variable for store

# Function for receive data from tgConnector.
def tg_callback(message):
    print(message)

# import settings from file on the server.
filename = 'settings.json'
settingsFile = open(filename, 'r', encoding='utf-8')
parsedJson = json.load(settingsFile)
api_key = parsedJson['api_key']
list_of_consumables_btn = parsedJson['list_of_consumables_btn']
list_of_service_btn = parsedJson['list_of_service_btn']
settingsFile.close

# init bot.
TG = tgConnector.TG(
    api_key=api_key,
    consumables_list=list_of_consumables_btn,
    service_list=list_of_service_btn,
    callback_function=tg_callback)
# run bot.
tgConnector.TG.bot_start()

# init db.