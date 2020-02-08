# Vasyl Herman <vasil.german@gmail.com>
import time

start_in = 15
sec = 0


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("\r Time is {1:0=2d} mins : {2:0=2d} sec".format(int(hours), int(mins), sec), end='')


while start_in >= 0:
    print("\rStart in {0:0=2d} sec".format(int(start_in)), end='')
    time.sleep(1)
    start_in -= 1

while True:
    time_convert(sec)
    time.sleep(1)
    sec += 1
