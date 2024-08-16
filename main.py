import time
import datetime as dt
import glob
import requests


file_path = '/etc/hostname'
hostname = 'undefined'
with open(file_path, "r") as file:
    hostname = file.read().strip()

# path = "/code/output/"
# with open("api_get_hostname.txt", "w+") as f:
#     f.write('{"name": "' + hostname + '", "time": "' + str(dt.datetime.now()) + '"}')
# time.sleep(60)


folder_path = '/code/input/'
filesPaths = glob.glob(folder_path + '*')
for fpath in filesPaths :
    fname = fpath.replace(folder_path, '').replace('.mp4', '.json')
    time.sleep(3)
    path = "/code/output/"
    # path = ""
    with open(path + fname, "w+") as f:
        f.write('{"filename": "' + fname + '", "hostname": "' + hostname + '", "time": "' + str(dt.datetime.now()) + '"}')


    print(x.text)



print("Finish")