# Szperacz 2022
# Main repo: https://github.com/vendral/szperacz
import json
import sys

from flask import Flask, render_template
from flask_cors import CORS

from utils import get_files, get_files_with_gps, get_file_by_id, get_creation_time
from logger import logger
from tests import get_test_data_path

TEST_RUN_ARG = '-t'
TEST_RUN_PARAM = '--test-run'

HEADFUL_ARG = '-h'
HEADFUL_PARAM = '--headful'

app = Flask(__name__)
CORS(app)
search_path = None


# region Routes
@app.route('/')
def index():
    # Debug magic number
    fid = 7

    files = get_files(search_path)
    files_with_gps = get_files_with_gps(files)
    file_with_id = get_file_by_id(files, fid)
    files_date_options = get_creation_time(files)
    files_dict_keys = list(files[0].keys())

    return render_template('index.html',
                           files_size=len(files),
                           files=files,
                           files_dict_keys=files_dict_keys,
                           files_with_gps_size=len(files_with_gps),
                           files_with_gps=files_with_gps,
                           files_date_options=files_date_options,
                           file_with_id=file_with_id)

@app.route('/getPoints')
def getPoints():
    files = get_files(search_path)

    def dms_to_long_lat(dms, dir):
        deg = dms[0]
        min = dms[1]
        sec = dms[2]

        return (float(deg) + float(min)/60 + float(sec)/(60*60)) * (-1 if dir in ['W', 'S'] else 1)

    def get_coordinates(file):
        gps_lo = dms_to_long_lat(file["gps_lo"], 'N')  #TODO: Get 'N' dynamically
        gps_la = dms_to_long_lat(file["gps_la"], 'E')  #TODO: Get 'E' dynamically

        return [gps_lo, gps_la]

    files_long_lat = map(get_coordinates, files)

    return list(files_long_lat)
# endregion


# region Logging
def log_to_console(files):
    logger.debug('Szperacz finds images')
    print(f'Images found: {len(files)}')
    if len(files) > 0:
        print('---')
    if len(files) == 0:
        logger.error('No images found')
    for i in files:
        print(f'{i}')

def log_to_file(files):
    with open('data.json', 'w') as json_file:
        json.dump(files, json_file)
# endregion


# region UI
def headless(search_path):
    logger.info('Szperacz in headless form')
    files = get_files(search_path)
    log_to_console(files)
    log_to_file(files)
    logger.get_log_level()


def headful(app):
    app.secret_key = 'SZPERACZ_KEY'
    app.run()
# endregion


if __name__ == '__main__':

    args = sys.argv[1:]

    logger.info('Szperacz is running')
    if TEST_RUN_ARG in args or TEST_RUN_PARAM in args:
        search_path = get_test_data_path()

    if HEADFUL_ARG in args or HEADFUL_PARAM in args:
        headful(app)
    else:
        headless(search_path)
