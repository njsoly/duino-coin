# test library for import?

import sys
from configparser import ConfigParser
from datetime import datetime
from json import load as jsonload
from locale import LC_ALL, getdefaultlocale, getlocale, setlocale
from os import _exit, execl, mkdir, rmdir
from os import name as osname
from os import path
from os import system as ossystem
from platform import machine as osprocessor
from pathlib import Path
from platform import system
from re import sub
from signal import SIGINT, signal
from socket import socket
from subprocess import DEVNULL, Popen, check_call, call
from threading import Thread as thrThread
from threading import Lock
from time import ctime, sleep, strptime, time
from statistics import mean
from random import choice
import select
import pip
from pathlib import Path

def getDateTime_pretty():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getDateTime_pretty_path():
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")

def getDateTime_path():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def getDate_path():
    return datetime.now().strftime("%Y%m%d")

def getTime_path():
    return datetime.now().strftime("%H%M%S")

def logLines(lines):
    with open(logFileName, "at") as log:
        log.writelines(lines)

def log(line):
    with open(logFileName, "at") as log:
        log.write(line)

def getPwd():
    pwd = Path(".").absolute()
    return pwd

logFileName = "tester_" + getDate_path() + ".log"
