#################################################
#    Test developed for using with pytest.      #
#################################################

import json
import os

# Get system paths separator.
if os.name == 'nt':
    system_sep = '\\'
else:
    system_sep = '/'

# Settings.
allow_values_for_api_key: list = ['TOKEN', '', 0]
cwd = os.getcwd().split(system_sep)
if cwd[-1] == 'Test':
    filename: str = '../settings.json'
else:
    filename: str = 'settings.json'


def test_json_api_key():
    with open(filename, 'r', encoding='utf-8') as f:
        parsed_json = json.load(f)
        if parsed_json['api_key'] in allow_values_for_api_key:
            assert True
        else:
            assert False
