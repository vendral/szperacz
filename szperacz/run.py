# Szperacz 2022
# Main repo: https://github.com/vendral/szperacz
import sys

from szperacz.files import FileHandler
from tests import get_test_data_path

import json


TEST_RUN_ARG = '-t'
TEST_RUN_PARAM = '--test-run'


def log_to_console(files):
    print(f'Images found: {len(files)}')
    if len(files) > 0:
        print('---')
    for i in files:
        print(f'{i}')


def print_to_json_file(files):
    file = open('output.txt', 'w')
    app = json.dumps(files)
    print(app, file=file)
    file.close()


if __name__ == '__main__':

    path = None
    args = sys.argv[1:]

    file_handler = FileHandler()

    if TEST_RUN_ARG in args or TEST_RUN_PARAM in args:
        path = get_test_data_path()

    files = file_handler.process_files(path)
    log_to_console(files)
    print_to_json_file(files)
