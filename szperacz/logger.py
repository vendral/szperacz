

class Logger:
    global log_level
    log_level = 0
    level = log_level
    DEBUG = '[DEBUG]'
    INFO = '[INFO]'
    ERROR = '[ERROR]'

    error = open("error_log.txt", mode='w')

    def set_log_level(self):
        pass

    def get_log_level(self):
        return print(f'Logging level: {self.level}')

    def debug(self, msg):
        if log_level == 0:
            return print(f'{self.DEBUG} {msg}')

    def info(self, msg):
        if log_level <= 1:
            return print(f'{self.INFO} {msg}')

    def error(self, msg):
        if log_level <= 2:
            error = open("error_log.txt", mode='a')
            er = f'{self.ERROR} {msg}' '\n'
            error.writelines(er)
            error.close()
            return print(f'{self.ERROR} {msg}')


logger = Logger()
