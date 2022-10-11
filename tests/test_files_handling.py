from tests import check_jpeg_files_only


def test_file_discovery_jpeg_only_test(test_files):
    check_jpeg_files_only(test_files)
