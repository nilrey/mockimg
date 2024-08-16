import time
import datetime as dt
import glob
import requests


hostname_path = '/etc/hostname'
output_path = "" # "/code/output/"
input_path = '/code/input/'

def getContainerId(containerId = 0):
    with open(hostname_path, "r") as file:
        containerId = file.read().strip()
    return containerId

containerId = getContainerId()
url = f'http://127.0.0.1:8002/events/{containerId}/before_start'
myobj = {"msg": "before ann start", "details": "" }
before_start_response = requests.post(url, json = myobj)


with open(output_path + "before_start.txt", "w+") as f:
    f.write('{"action": "before_start", "containerId": "' + containerId + '", "time": "' + str(dt.datetime.now()) + '", "response": ' + before_start_response.text + '}')

# filesPaths = glob.glob(input_path + '*')
# for fpath in filesPaths :
#     fname = fpath.replace(input_path, '').replace('.mp4', '.json')
#     time.sleep(3)
#     with open(output_path + fname, "w+") as f:
#         f.write('{"filename": "' + fname + '", "hostname": "' + hostname + '", "time": "' + str(dt.datetime.now()) + '"}')
