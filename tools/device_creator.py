import hashlib
import json
import random
import sqlite3

f = open("../server.json", 'r')
db = sqlite3.connect("../device_data.db")
config = json.loads(f.read())
del config['ServerConfig']['ServerPrivateKey']
del config['ServerConfig']['DatabasePath']
device_id = input('Please input a device id')
loginkey = hashlib.md5(str(random.randint(1, 100000000)).encode('utf-8')).hexdigest()
try:
    db.execute(f'INSERT INTO DEVICES (DEVICEID, LOGINKEY) VALUES ({device_id}, \'{loginkey}\');')
    db.commit()
except:
    print('Device ID already exists')
    exit()

config['role'] = 'Client'
config['ClientConfig']['DeviceID'] = device_id
config['ClientConfig']['LoginKey'] = loginkey
config['DevicePolicy']['HeartTime'] -= 1
# Reduce the heartbeat duration of the client appropriately
del config['DevicePolicy']['InactiveStopTime']
del config['DevicePolicy']['AESReplaceTime']

with open(f'./config_{device_id}_{config["ServerConfig"]["ServerName"]}.json', 'w+') as f:
    f.write(json.dumps(config))
print(f'Device Config File Generated,Please Copy It To The Device And Run It')
