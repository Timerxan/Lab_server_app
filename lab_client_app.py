import socket
from os import stat
from time import localtime, strftime
from pathlib import Path

def connect_to_server(ip_addr, port):
    try:
        svr_sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        svr_sct.connect((ip_addr, port))
        response = svr_sct.recv(256)
        print(response.decode())
        return svr_sct
    except Exception as ex:
        print('Connection failed!', ex)
        return -1


def send_file_info(svr_sct, file_path):
    info = stat(file_path)
    file_info = f'{socket.gethostname()}\n' \
                f'{Path(file_path).resolve()}\n' \
                f'{strftime("%Y-%m-%d %H:%M:%S", localtime(info.st_ctime))}\n' \
                f'{info.st_size}'
    print('file_info:\n', file_info)

    try:
        svr_sct.send(file_info.encode())

    except Exception as ex:
        print('Error while sending file_info', ex)


def send_file(svr_sct, file_path_with_name):
    try:
        file = open(file_path_with_name, 'rb')
        file_part = file.read(256)

        while file_part != b'':
            svr_sct.send(file_part)
            file_part = file.read(256)

        print('Done')
        file.close()

    except Exception as ex:
        print('Error while reading and sending file', ex)

    finally:
        svr_sct.close()


srv_sct = connect_to_server('localhost', 666)
if srv_sct != -1:
    send_file_info(srv_sct, 'test.txt')
    send_file(srv_sct, 'test.txt')

