# Szperacz 2022
# Main repo: https://github.com/vendral/szperacz
import json
import sys

from flask import Flask, render_template

from szperacz.utils import get_files, get_files_with_gps, get_file_by_id
from tests import get_test_data_path

TEST_RUN_ARG = '-t'
TEST_RUN_PARAM = '--test-run'

HEADFUL_ARG = '-h'
HEADFUL_PARAM = '--headful'

app = Flask(__name__)
search_path = None


# region Routes
@app.route('/')
def index():
    # Debug magic number
    fid = 7

    files = get_files(search_path)
    files_with_gps = get_files_with_gps(files)
    file_with_id = get_file_by_id(files, fid)

    return render_template('index.html',
                           files_size=len(files),
                           files=files,
                           files_with_gps_size=len(files_with_gps),
                           files_with_gps=files_with_gps,
                           file_with_id=file_with_id)
# endregion


# region Logging
def log_to_console(files):
    print(f'Images found: {len(files)}')
    if len(files) > 0:
        print('---')
    for i in files:
        print(f'{i}')


def log_to_file(files):
    with open('data.json', 'w') as json_file:
        json.dump(files, json_file)
# endregion


# region UI
def headless(search_path):
    files = get_files(search_path)
    log_to_console(files)
    log_to_file(files)


def headful(app):
    app.secret_key = 'SZPERACZ_KEY'
    app.run()
# endregion


if __name__ == '__main__':

    args = sys.argv[1:]

    if TEST_RUN_ARG in args or TEST_RUN_PARAM in args:
        search_path = get_test_data_path()

    if HEADFUL_ARG in args or HEADFUL_PARAM in args:
        headful(app)
    else:
        headless(search_path)
