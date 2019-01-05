from django.test import TestCase

import datetime

def get_time():
    now_time = datetime.datetime.now().date()
    print(now_time)

if __name__ == '__main__':
    get_time()