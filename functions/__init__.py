import threading

import rsa.randnum

from functions.device_processer import process
from functions.global_variable import *
from tools import AES
from tools.threading_stopper import *


class Device:
    def __init__(self, sock, device_id, addr, times):
        self.sock = sock  # socket
        self.device_id = device_id  # device id
        self.addr = addr  # device address
        self.time = times  # The last time that server received heart from the device
        self.proc = None  # The threading of the device
        self.pubkey = None  # The Public key of the device
        self.aes_key = None  # The AES key of the device
        self.key_effective_time = 0  # The AES Key effective time

    def init(self):
        """
        Initiating Device
        """
        database = sqlite3.connect(server_database)
        pubkey = database.execute(f'SELECT PUBKEY FROM DEVICES WHERE DEVICEID = {self.device_id}').fetchone()[0]
        self.pubkey = rsa.PublicKey.load_pkcs1(pubkey)
        self.proc = threading.Thread(target=process, args=(self,))
        self.proc.start()
        self.update_device_aes_key()
        device_list.append(self)
        database.close()

    def update_device_aes_key(self):
        self.aes_key = rsa.randnum.read_random_bits(128)
        self.sock.send(f'AES {rsa.encrypt(self.aes_key, self.pubkey).hex()}'.encode('utf-8'))

    def private_send(self, data):
        """
        Send Message to device in privacy
        """
        self.sock.send(AES.encrypt(data, self.aes_key))

    def kill(self):
        """
        Just Kill The Device,If you like
        """
        stop_thread(self.proc)
        device_list.remove(self)
        self.sock.close()
