

class Logger:
    DEBUG = '[DEBUG]'
    INFO = '[INFO]'
    ERROR = '[ERROR]'

    def debug(self, msg):
        return print(f'{self.DEBUG} {msg}')

    def info(self, msg):
        return print(f'{self.INFO} {msg}')

    def error(self, msg):
        return print(f'{self.ERROR} {msg}')


logger = Logger()
