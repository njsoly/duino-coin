import sys
from configparser import ConfigParser
from datetime import datetime
from hashlib import sha1
from json import load as jsonload
from os import path, system
from os import system as ossystem
from pathlib import Path
from platform import system as plsystem
from subprocess import DEVNULL, Popen, check_call
from threading import Thread as thrThread
from time import ctime, sleep, strptime, time

print('do this do that' + str(5) + ' aosnetuh')
jobs = 'snthsnthxsnthsnthxsnthsnth'
jobsList = jobs.split('x')
print('jobsList: ' + str(jobsList))

jobsList = jobs.split(',')
print('jobsList: ' + str(jobsList))

result = None
if result is not None:
    print("Thread "
        + str(0)
        + ": result found: "
        + str(result[0]))