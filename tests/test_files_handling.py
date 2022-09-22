import pytest

from tests import check_jpeg_files_only


@pytest.mark.parametrize("temp_files", [
    [],
    ["test_file_long_name_with_numbers12345", "test_file_long_name_with_numbers12345.jpeg"],
    ["test", "test.jpg", "1234.jpg", "test.bmp"],
    ["1.jpg", "2.jpg", "3.jpg", "jpg.jpg.bmp", "bmp.jpg.jpg"]
], indirect=True)
def test_file_discovery_jpeg_only_temp(temp_files):
    check_jpeg_files_only(temp_files, False)


def test_file_discovery_jpeg_only_test(test_files):
    check_jpeg_files_only(test_files)
