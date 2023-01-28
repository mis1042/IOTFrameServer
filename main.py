import socket

from functions.device_functions import *


def start_listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_hostname, server_port))
    s.listen(100)
    print(f'Waiting for connection... Port{str(s.getsockname()[1])}')
    while True:
        sock, addr = s.accept()
        device_register_t = threading.Thread(target=device_register, args=(sock, addr))
        device_register_t.start()


if __name__ == '__main__':
    start_listen()
