import time
import datetime as dt
import glob
import requests
import json


#domain = '127.0.0.1:8002'
domain = '172.17.0.2'
#domain = 'camino-restapi'
mockjson = 'mockjson.json'
mockjson_content = '{}'
logfile = 'processing.log'
hostname_path = '/etc/hostname'
input_path = '/code/input/'
output_path = '/code/output/'
containerId = '0000000'


def getUrl(dom='camino-restapi', cId='', ep_name='before_start'):
    return f'http://{dom}/events/{cId}/{ep_name}'


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

writeLog("url_compose", getUrl(domain, containerId))

# send request to camino-restapi
before_start_response = requests.post(getUrl(domain, containerId, 'before_start'), json = setMessage('before ann start') )

writeLog("before_start", before_start_response.text)

# читаем файлы из директории input
filesPaths = glob.glob(input_path + '*')
for fpath in filesPaths :
    fname = fpath.replace(input_path, '').replace('.mp4', '.json')
    if(fname):
        with open(output_path + fname, "w+") as f:
            f.write(mockjson_content)
            # send request on_progress to camino-restapi
            proceed_response = requests.post(getUrl(domain, containerId, 'on_progress'), json = setMessage(fname) )
            writeLog("procceed", proceed_response.text )
            time.sleep(3)
        
end_response = requests.post(getUrl(domain, containerId, 'before_end'), json = setMessage('before_end ') )
writeLog("before_end", end_response.text)
time.sleep(30)
