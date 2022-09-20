import os


def discover_files(path=None):
    return [file for file in os.listdir(path) if file.endswith('.jpg') or file.endswith('.jpeg')]
