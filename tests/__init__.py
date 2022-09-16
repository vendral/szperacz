import os
from datetime import datetime


TEST_DATA_PATH = 'test_data/'


def get_test_data_path():
    return os.path.abspath(__file__) + TEST_DATA_PATH


def create_test_data_dir():
    try:
        os.mkdir(get_test_data_path())
    except FileExistsError:
        print('Test data folder exists')


def remove_test_data_dir():
    os.rmdir(get_test_data_path())


def create_files(files):
    create_test_data_dir()
    for file in files:
        file = get_test_data_path() + file
        try:
            with open(file, 'x') as f:
                f.write('Mock file created: %'.format(datetime.now()))
        except FileExistsError:
            print('Mock file exists: '.format(file))


def remove_files(files):
    for file in files:
        file = get_test_data_path() + file
        if os.path.exists(file):
            os.remove(file)
    remove_test_data_dir()
