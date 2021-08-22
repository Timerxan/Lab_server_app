import socket


def connect_to_server(ip_addr, port):
    try:
        svr_sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        svr_sct.connect((ip_addr, port))
        response = svr_sct.recv(256)
        print(response.decode())
        return svr_sct
    except:
        print('Connection failed!')
        return -1


def send_file_info(svr_sct, file_path_with_name):

    pass


def send_file(svr_sct, file_path_with_name):
    try:
        file = open(file_path_with_name, 'rb')
        file_part = file.read(256)

        while file_part != b'':
            svr_sct.send(file_part)
            file_part = file.read(256)

        print('Done')
        file.close()

    except:
        print('Error while reading and sending file')

    finally:
        svr_sct.close()


srv_sct = connect_to_server('localhost', 666)
if srv_sct != -1:
    send_file(srv_sct, 'test.txt')