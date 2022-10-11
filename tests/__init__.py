import os
from collections import Counter

from szperacz.files import FileHandler

# region Global variables
TEST_DATA_PATH = 'test_data/'
# endregion

file_handler = FileHandler()


# region Points of Control
def get_tests_dir():
    return os.path.abspath(__file__).rstrip("__init__.py")


def get_test_data_path():
    return get_tests_dir() + TEST_DATA_PATH


# region Points of Observation
def filter_only_jpeg(test_files):
    file_filter = ['jpg', 'jpeg']
    return [file for file in test_files if file[-3:] in file_filter or file[-4:] in file_filter]


def check_jpeg_files_only(test_files):
    file_handler.process_files(get_test_data_path())
    actual_files = file_handler.images
    expected_files = filter_only_jpeg(test_files)

    assert isinstance(actual_files, list)
    assert Counter(expected_files) == Counter(actual_files)
# endregion
