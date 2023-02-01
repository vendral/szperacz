

class Logger:

    def debug(self, msg_d):
        return print(f'{DEBUG} {msg_d}')

    def info(self, msg_i):
        return print(f'{INFO} {msg_i}')

    def error(self, msg_e):
        return print(f'{ERROR} {msg_e}')


DEBUG = '[DEBUG]'
INFO = '[INFO]'
ERROR = '[ERROR]'

logger = Logger()
