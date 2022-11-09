from szperacz.files import FileHandler


def get_files(search_path):
    file_handler = FileHandler()
    return file_handler.process_files(search_path)


def get_files_with_gps(files):
    def has_gps(file):
        if file['gps_lo'] != (0, 0, 0) and file['gps_lo'] is not None and \
                file['gps_la'] != (0, 0, 0) and file['gps_la'] is not None:
            return True
        else:
            return False

    return [file for file in files if has_gps(file)]


def get_file_by_id(files, fid):
    return next(file for file in files if file["id"] == fid)
