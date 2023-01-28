import hashlib
import random
import sqlite3

from functions import Device
from functions.device_processer import *
from functions.global_variable import *
from tools.threading_stopper import *


def device_register(sock, addr):
    database = sqlite3.connect(server_database)
    inactive_stop_t = threading.Thread(target=inactive_stop, args=(threading.current_thread(), sock, 10))
    inactive_stop_t.start()
    # It can close the sock object and stop the thread object if the device is inactive for 10 seconds
    session_id = 123456
    hello_message = f'{server_name}-{session_id}'
    hello_sign = rsa.sign(hello_message.encode('utf-8'), server_privatekey, 'MD5')
    sock.send(f'ServerHello {hello_message} {hello_sign.hex()}'.encode('utf-8'))
    # Try to handshaking with the device
    data = sock.recv(1024).decode('utf-8')
    if data.startswith('ClientHello'):
        stop_thread(inactive_stop_t)
        data = data.split(" ")
        device_id = data[1]
        device_key = data[2]

        # Check the device id and device key
        true_device_login_key = \
            database.execute(f'SELECT LOGINKEY FROM DEVICES WHERE DEVICEID = {device_id}').fetchone()[0]
        true_device_key = hashlib.md5(f'{session_id}{device_id}{true_device_login_key}'.encode('utf-8')).hexdigest()

        # Successfully registered
        if device_key == true_device_key:
            device_object = Device(sock, device_id, addr, time.time())
            device_object.init()
            database.close()
        else:
            sock.close()
            database.close()
    else:
        database.close()
        sock.close()


def heart_check():
    """
    :return: None Auto check the heartbeat of the device and automatically disconnect the device if the heartbeat is
    not received for 10 seconds
    **For a thread**
    """
    while True:
        for i in device_list:
            if time.time() - i.time > 10:
                print(f'Device {i.device_id} has been disconnected')
                i.kill()
            if i.key_effective_time >= 10:
                i.update_device_aes_key()
                i.key_effective_time = 0
        time.sleep(1)


def get_device(device_id):
    """
    :param device_id: The Device`s ID you want to get
    :return: The Device Object
    The function can get a device object by device id
    """
    for i in device_list:
        if i.device_id == device_id:
            return i


def inactive_stop(thread, sock, inactive_time):
    """
    :param inactive_time: The time to stop the thread
    :param thread:  object responsible for managing device registration
    :param sock: The sock object to connect to device
    :return: None

    This functions will close the sock object and stop the thread object if the device is inactive for a certain time
    **For a thread**
    """
    time.sleep(inactive_time)
    stop_thread(thread)
    sock.send(b'TimeOut')
    sock.close()


heart_checker = threading.Thread(target=heart_check)
heart_checker.start()
