import os

import pytest

from tests import get_test_data_path


@pytest.fixture
def test_files():
    return [file for file in os.listdir(get_test_data_path())]
