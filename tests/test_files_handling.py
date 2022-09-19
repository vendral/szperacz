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


def filter_only_jpeg(mock_files):
    file_filter = ['jpg', 'jpeg']
    return [file for file in mock_files if file[-3:] in file_filter ]


@pytest.mark.parametrize("mock_files", [
    [],
    ["test_file_long_name_with_numbers12345", "test_file_long_name_with_numbers12345.jpeg"],
    ["test", "test.jpg", "1234.jpg", "test.bmp"],
    ["1.jpg", "2.jpg", "3.jpg", "jpg.jpg.bmp", "bmp.jpg.jpg"]
], indirect=True)
def test_file_discovery_jpeg_only(mock_files):
    actual_files = discover_files(get_test_data_path())
    jpeg_files = filter_only_jpeg(mock_files)

    assert isinstance(actual_files, list)
    assert Counter(jpeg_files) == Counter(actual_files)
