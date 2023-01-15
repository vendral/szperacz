from szperacz.files import FileHandler


def get_files(search_path):
    file_handler = FileHandler()
    return file_handler.process_files(search_path)


def get_creation_time(files):
    file_date_option = []
    for i in files:
        date = i.get("creation_time")[0:10].replace(':', '-')
        if date not in file_date_option:
            file_date_option.append(date)

    return file_date_option


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
