import time
import datetime as dt
import glob
import requests


domain = '127.0.0.1:8002'
domain = '172.17.0.2'
mockjson = 'mockjson.json'
mockjson_content = '{}'
logfile = 'processing.log'
hostname_path = '/etc/hostname'
input_path = '/code/input/video/'
output_path = '/code/output/'
containerId = '0000000'


def getUrl(dom='camino-restapi', cId=''):
    return f'http://{dom}/events/{cId}/before_start'


def setMessage(msg = ""):
    return {"msg": msg }

def writeLog(action = "", txt = ""):
    msg = '{"action": "'+ action +'", "containerId": "' + containerId + '", "response": "'+ txt +'", "time": "' + str(dt.datetime.now()) + '"}'
    with open(output_path + logfile, "a+") as f:
        f.write(msg + '\n')

with open(mockjson, "r") as file:
    mockjson_content = file.read()

with open(hostname_path, "r") as file:
    containerId = file.read().strip()

print("Begin")

writeLog("url_compose", getUrl(domain, containerId))

before_start_response = requests.post(getUrl(domain, containerId), json = setMessage('before ann start') )

writeLog("before_start", before_start_response.text)

# читаем файлы из директории video
filesPaths = glob.glob(input_path + '*')
for fpath in filesPaths :
    fname = fpath.replace(input_path, '').replace('.mp4', '.json')
    with open(output_path + fname, "w+") as f:
        f.write(mockjson_content)
        writeLog("procceed", "filename: "+fname)
        time.sleep(3)

writeLog("before_end", "success")
print("End")