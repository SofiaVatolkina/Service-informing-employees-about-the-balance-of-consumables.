import re

class Processing:
    """
    Class with static functions for processing any data, or any service functions.
    """

    # Function for receive data from tgConnector.
    @staticmethod
    def tg_callback(message):
        return Processing.temp_db_processing(message)

    # temp db
    @staticmethod
    def temp_db_processing(data):
        with open('.test', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if re.match(data.text, line):
                    # parse line if matched.
                    result = line.split(':')
                    return f'На складе осталось {result[1]} штук {result[0]}'
