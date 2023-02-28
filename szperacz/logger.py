

class Logger:
    log_level = None
    DEBUG = '[DEBUG]'
    INFO = '[INFO]'
    ERROR = '[ERROR]'
    LOG_LEVEL_DEBUG = 0
    LOG_LEVEL_INFO = 1
    LOG_LEVEL_ERROR = 2

    def __init__(self, level):
        self.log_level = self.set_log_level(level)

    def set_log_level(self, level):
        log_levels = [
            self.LOG_LEVEL_DEBUG,
            self.LOG_LEVEL_INFO,
            self.LOG_LEVEL_ERROR
            ]

        if level not in log_levels:
            raise Exception(f'Expected log level {level} is out of range {log_levels}')
        else:
            self.log_level = level

    def get_log_level(self):
        print(f'Logging level: {self.log_level}')
        return self.log_level

    def debug(self, msg):
        if self.log_level == self.LOG_LEVEL_DEBUG:
            print(f'{self.DEBUG} {msg}')

    def info(self, msg):
        if self.log_level <= self.LOG_LEVEL_INFO:
            print(f'{self.INFO} {msg}')

    def error(self, msg):
        if self.log_level <= self.LOG_LEVEL_ERROR:
            with open("error_log.txt", mode='a') as error_log:
                er = f'{self.ERROR} {msg}' '\n'
                error_log.write(er)
            print(f'{self.ERROR} {msg}')


Logger(Logger.LOG_LEVEL_DEBUG)
logger = Logger
