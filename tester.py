import testerlib as njs
from os import mkdir, path, rmdir
from pathlib import Path
from time import sleep
from datetime import datetime


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

now = datetime.now()
print(now)
print(now.date())
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print("******** testing date/time functions *********")
print("getDateTime_pretty(): " + njs.getDateTime_pretty())
print("getDateTime_pretty_path(): " + njs.getDateTime_pretty_path())
print("getDateTime_path(): " + njs.getDateTime_path())
print("getDate_path(): " + njs.getDate_path())
print("getTime_path(): " + njs.getTime_path())
print("******** end testing date/time functions *********")

def test_makeAndRemoveDirectoryX():
    # Create resources folder if it doesn't exist
    if not path.exists("directory_x"):
        mkdir("directory_x")
        sleep(5)
        rmdir("directory_x")



def test_listPwd():
    pwd = njs.getPwd()
    print("absolute path of PWD: " + str(pwd))
    pwdList = Path.cwd().iterdir()
    cnt = 0
    for i in pwdList:
        cnt += 1
        print(i)
    print("files in " + str(pwd) + ": " + str(cnt))
    print("PWD list: " + str(pwdList))

test_listPwd()
DEBUG = False

# def makeLogFile():
#     if DEBUG and not Path(logFileName).is_file():
#         print(logFileName + " does not already exist.  It will be created.")
    
#     with open(logFileName, 'at') as f:
#         f.writelines(["uaoeu\n"])
    
#     if DEBUG: print("log file: " + logFileName)


# def logLines(lines):
#     with open(logFileName, "at") as log:
#         log.writelines(lines)

# def log(line):
#     with open(logFileName, "at") as log:
#         log.write(line)

njs.log("snthsnthstnh")
