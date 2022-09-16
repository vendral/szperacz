from collections import Counter

import pytest

from szperacz.files import discover_files
from tests import create_files, remove_files, get_test_data_path


@pytest.fixture
def mock_files(request):
    files = request.param

    create_files(files)
    yield files
    remove_files(files)


@pytest.mark.parametrize("mock_files", [
    [],
    ["test_file_long_name_with_numbers12345"],
    ["test", "test.jpg", "1234.jpg"]
], indirect=True)
def test_file_discovery(mock_files):
    assert Counter(mock_files) == Counter(discover_files(get_test_data_path()))
