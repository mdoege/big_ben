#!/usr/bin/python

# Westminster quarters

import time, os, sys

if len(sys.argv) > 1:
    test = True
else:
    test = False

play = "/usr/bin/play -q"

last = -1

while True:
    tt = time.localtime()
    h, m = tt.tm_hour, tt.tm_min
    if test:
        m = 0
    if m == 15 and last != 15:
        last = 15
        os.system(play + " 15.wav")
    if m == 30 and last != 30:
        last = 30
        os.system(play + " 30.wav")
    if m == 45 and last != 45:
        last = 45
        os.system(play + " 45.wav")
    if m == 0 and last != 0:
        last = 0
        os.system(play + " 00.wav")
        nn = h % 12
        if nn == 0:
            nn = 12
        time.sleep(1)
        for x in range(nn):
            os.system(play + " bigben_oct.wav")
    time.sleep(1)

