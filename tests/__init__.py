import os
from collections import Counter
from datetime import datetime

# from szperacz.files import discover_files

# region Global variables
TEMP_DATA_PATH = 'temp_data/'
TEST_DATA_PATH = 'test_data/'
# endregion


# region Points of Control
def get_tests_dir():
    return os.path.abspath(__file__).rstrip("__init__.py")


def get_temp_data_path():
    return get_tests_dir() + TEMP_DATA_PATH


def get_test_data_path():
    return get_tests_dir() + TEST_DATA_PATH


def create_temp_data_dir():
    try:
        os.mkdir(get_temp_data_path())
    except FileExistsError:
        print('Test data folder exists')


def remove_temp_data_dir():
    os.rmdir(get_temp_data_path())


def create_files(files):
    create_temp_data_dir()
    for file in files:
        file = get_temp_data_path() + file
        try:
            with open(file, 'x') as f:
                f.write('Mock file created: %'.format(datetime.now()))
        except FileExistsError:
            print('Mock file exists: '.format(file))


def remove_files(files):
    for file in files:
        file = get_temp_data_path() + file
        if os.path.exists(file):
            os.remove(file)
    remove_temp_data_dir()
# endregion


# region Points of Observation
def filter_only_jpeg(test_files):
    file_filter = ['jpg', 'jpeg']
    return [file for file in test_files if file[-3:] in file_filter or file[-4:] in file_filter]


def check_jpeg_files_only(test_files, test_run=True):
    if test_run:
        # Test run in test_data/
        actual_files = discover_files(get_test_data_path())
    else:
        # Temp run in generated temp_data/
        actual_files = discover_files(get_temp_data_path())
    expected_files = filter_only_jpeg(test_files)

    assert isinstance(actual_files, list)
    assert Counter(expected_files) == Counter(actual_files)
# endregion
