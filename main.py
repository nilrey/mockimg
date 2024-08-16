import time
import datetime as dt
import glob
import requests


domain = '127.0.0.1:8002'
hostname_path = '/etc/hostname'
input_path = '/code/input/'
output_path = ""#"/code/output/"
containerId = 0


def getUrl():
    return f'http://{domain}/events/{containerId}/before_start'


def setMessage(msg = ""):
    return {"msg": msg }


with open(hostname_path, "r") as file:
    containerId = file.read().strip()

before_start_response = requests.post(getUrl(), json = setMessage('before ann start') )

# вывод response от camino-restapi в сторонний файл, размещен на хосте в соответствующей папке output данного проекта
with open(output_path + "before_start.txt", "w+") as f:
    f.write('{"action": "before_start", "containerId": "' + containerId + 
            '", "time": "' + str(dt.datetime.now()) +
            '", "response": ' + before_start_response.text + '}')


# filesPaths = glob.glob(input_path + '*')
# for fpath in filesPaths :
#     fname = fpath.replace(input_path, '').replace('.mp4', '.json')
#     time.sleep(3)
#     with open(output_path + fname, "w+") as f:
#         f.write('{"filename": "' + fname + '", "hostname": "' + hostname + '", "time": "' + str(dt.datetime.now()) + '"}')
