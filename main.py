import time
time.sleep(10)
f = open("/code/buffer/neuroresult.txt", "w+")
f.write('{"name": "neuroresult-example", "start": 0, "end": 12345678}')
f.close()

time.sleep(60)