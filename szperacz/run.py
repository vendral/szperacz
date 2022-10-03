# Szperacz 2022
# Main repo: https://github.com/vendral/szperacz
import sys

from szperacz.files import discover_files
from tests import get_test_data_path

TEST_RUN_ARG = '-t'
TEST_RUN_PARAM = '--test-run'

if __name__ == '__main__':

    path = None
    args = sys.argv[1:]

    if TEST_RUN_ARG in args or TEST_RUN_PARAM in args:
        path = get_test_data_path()

    files = discover_files(path)


def log_to_console(files):
    print(f'Images found: {len(files)}\n---')
    for i in files:
        print(f'{i}')

    return '---'


print(log_to_console(files))
