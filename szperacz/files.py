import os
from exif import Image


class FileHandler:

    def __init__(self):
        self.path = None
        self.images = []
        self.data = []

    def _build_structures(self):
        for idx, img in enumerate(self.images):
            image = {'id': idx, 'path': self.path + img, 'gps_lo': 0, 'gps_la': 0}
            self.data.append(image)

    def _discover_files(self):
        self.images = [file for file in os.listdir(self.path) if file.endswith('.jpg') or file.endswith('.jpeg')]

    def _get_gps_data(self, data, image):
        try:
            data['gps_lo'] = image.gps_longitude
            data['gps_la'] = image.gps_latitude
        except AttributeError:
            data['gps_lo'] = None
            data['gps_la'] = None

    def _extract_exif(self):
        for idx, data in enumerate(self.data):
            with open(data['path'], "rb") as img:
                image = Image(img)
                if image.has_exif:
                    self._get_gps_data(data, image)

    def process_files(self, path=None):
        self.path = path
        if not self.images:
            self._discover_files()
            self._build_structures()
            self._extract_exif()
        return self.data
