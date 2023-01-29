import json

import rsa

# Load Config File
with open("./server.json") as f:
    config = json.loads(f.read())
    if config['role'] == 'Server':
        source_config = config
        server_hostname = config['hostname']
        server_port = config['Port']
        server_publickey = rsa.PublicKey.load_pkcs1(config['ServerConfig']['ServerPublicKey'])
        server_privatekey = rsa.PrivateKey.load_pkcs1(config['ServerConfig']['ServerPrivateKey'])
        server_database = config['ServerConfig']['DatabasePath']
        server_name = config['ServerConfig']['ServerName']
        HeartTime = config['DevicePolicy']['HeartTime']
        InactiveStopTime = config['DevicePolicy']['InactiveStopTime']
        AESReplaceTime = config['DevicePolicy']['AESReplaceTime']
    elif config['role'] == 'Client':
        raise Exception('Are u kidding me? I`m a server, not a client!')
    else:
        raise Exception(f'Hmm mm....I want to know who is {config["role"]}')

device_list = []
# device_list is a list that contains all the devices that have been connected to the server
