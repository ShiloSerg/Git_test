import time
from datetime import datetime


def user_create(unix_time: float, user_format: str) -> str:
    user_format = user_format.lower()
    rep1 = user_format.replace('dd', datetime.utcfromtimestamp(unix_time).strftime('%d'))
    rep2 = rep1.replace('mm', datetime.utcfromtimestamp(unix_time).strftime('%m'))
    rep3 = rep2.replace('yyyy', datetime.utcfromtimestamp(unix_time).strftime('%Y'))
    print(rep3)
    return rep3


if __name__ == '__main__':
    user_create(time.time(), "yyyy-mm-dd")
