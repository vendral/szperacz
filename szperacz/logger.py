import configparser


class Logger:
    log_level = None
    DEBUG = '[DEBUG]'
    INFO = '[INFO]'
    ERROR = '[ERROR]'
    LOG_LEVEL_DEBUG = 0
    LOG_LEVEL_INFO = 1
    LOG_LEVEL_ERROR = 2

    def __init__(self):
        self.set_log_level()

    def set_log_level(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        level = config.get('Setup', 'LOG_LEVEL')
        level = int(level)
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


logger = Logger()
