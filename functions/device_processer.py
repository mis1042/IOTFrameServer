import threading
import time
import rsa


def process(device):
    """
    Main device process function
    """
    print(f'Accept new connection from {device.addr} Device ID:{device.device_id}')
    while True:
        data = device.sock.recv(1024).decode('utf-8')
        if data == 'heart':
            device.time = time.time()
            device.key_effective_time += 1
            print(f'Heart from {device.device_id} has been received')
        elif data.startswith('PrivateMessage'):
            encrypt_data = data.split(' ')[1]
            message = rsa.decrypt(encrypt_data, device.private_key)
            t = threading.Thread(target=private_process, args=(device, message))
            t.start()
            t.join(1000)
        else:
            t = threading.Thread(target=normal_process, args=(device, data))
            t.start()
            t.join(1000)


def normal_process(device, message):
    """
    Process common device messages
    """
    pass


def private_process(device, message):
    """
    Process encrypted device messages
    """
    pass
