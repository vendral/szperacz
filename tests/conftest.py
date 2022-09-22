import os

import pytest

from tests import create_files, remove_files, get_test_data_path


@pytest.fixture
def temp_files(request):
    files = request.param

    create_files(files)
    yield files
    remove_files(files)


@pytest.fixture
def test_files():
    return [file for file in os.listdir(get_test_data_path())]
