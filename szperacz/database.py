import sqlite3
from logger import Logger

logger = Logger()


class Database:

    def __init__(self):
        self.name = "szperacz.db"
        self.connection = None
        self.cursor = None
        self.entry = "Photos"

    def connect(self):
        self.connection = sqlite3.connect(self.name)

        if self.connection:
            logger.debug(f"Database: {self.name}, connected!")
            self.cursor = self.connection.cursor()
            logger.debug(f"Database: {self.name}, cursor created!")
            self.create(self.entry)
        # TODO: Handle no connection

    def close(self):
        self.connection.close()

    def create(self, entry):

        exist_tab = self.cursor.execute("SELECT name FROM sqlite_master")
        if exist_tab.fetchone() is None:
            self.cursor.execute("CREATE TABLE Photos(path, gps_lo, gps_la, creation_time)")
            logger.debug(f"Database: {self.name}, create: {entry}")

    def read(self):
        read = None

    def update(self, image):
        if self.connection and self.cursor:
            gps_lo = "".join(map(str, image['gps_lo']))
            gps_la = "".join(map(str, image['gps_la']))

            self.cursor.execute("""INSERT INTO Photos(path, gps_lo, gps_la, creation_time) 
                           VALUES (?,?,?,?);""", (image['path'], gps_lo, gps_la, image['creation_time']))
            self.connection.commit()
        else:
            logger.debug("No connection or cursor")

    def delete(self):
        delete = None
