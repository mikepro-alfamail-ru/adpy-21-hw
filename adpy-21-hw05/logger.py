import hashlib
from datetime import datetime

LOGFILE = 'log.txt'


def datelogger(function):
    def _func(*args, **kwargs):
        print(datetime.now())
        result = function(*args, **kwargs)
        return result
    return _func


def loggertofile(logfile):
    def logger(function):
        def _func(*args, **kwargs):
            nonlocal logfile
            now = datetime.now()
            with open(logfile, 'a', encoding='utf-8') as log:
                log.write(f'Вызов функции {function.__name__}, время - {now}\n')
            result = function(*args, **kwargs)
            return result
        return _func
    return logger


'''
Как ни странно, но работает еще и в таком виде:

def datelogger(function):
    print(datetime.now())
    return function


def loggertofile(logfile):
    def logger(function):
        nonlocal logfile
        now = datetime.now()
        with open(logfile, 'a', encoding='utf-8') as log:
            log.write(f'Вызов функции {function.__name__}, время - {now}\n')
        return function
    return logger
'''


# @datelogger           # Задание 1
@loggertofile(LOGFILE)  # Задание 2
def md5gen(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode('utf-8')).hexdigest()


if __name__ == '__main__':
    for md5 in md5gen('main2.py'):
        print(md5)
