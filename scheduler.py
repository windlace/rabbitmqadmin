#!/usr/bin/python
import schedule
import time
import sys
import subprocess as sp

period = sys.argv[1]
command = sys.argv[2]

def job():
    sp.call(command, shell=True)

schedule.every(int(period)).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)
