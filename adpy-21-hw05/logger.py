import hashlib
from datetime import datetime

LOGFILE = 'log.txt'


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


# @datelogger           # Задание 1
@loggertofile(LOGFILE)  # Задание 2
def md5gen(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode('utf-8')).hexdigest()


if __name__ == '__main__':
    for md5 in md5gen('main.py'):
        print(md5)
