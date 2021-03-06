import socket
import operation_with_mysql as op_msql
import database_config as db_c


def create_server_socket(ip_addr, port):
    try:
        svr_sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        svr_sct.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        svr_sct.bind((ip_addr, port))
        svr_sct.listen(1)
        return svr_sct

    except Exception as ex:
        print('Err: Server not created./n', ex)
        return -1


def accept_client_connection(svr_sct):
    try:
        clt_sct, addr = svr_sct.accept()
        print('Connection from', addr)
        response = 'You are connected\n'.encode()
        clt_sct.send(response)
        return clt_sct

    except Exception as ex:
        print('Client acception failed/n', ex)
        return -1


def load_and_save_file_info_to_mysql_database(clt_sct):
    try:
        file_info = clt_sct.recv(256).decode()
        file_info = file_info.split('\n')
        print('file_info:\n', file_info)
        file_new_name = 'test2.txt'
        op_msql.insert_data_to_mysql_database(file_new_name, file_info, db_c.MYSQL_CONFIG)

    except Exception as ex:
        print('Can not get and save file_info', ex)


def load_and_save_data_to_file(clt_sct, file_path_with_name):
    try:
        file = open(file_path_with_name, 'wb')
        request = clt_sct.recv(256)
        while request != b'':
            file.write(request)
            request = clt_sct.recv(256)
        file.close()
        print('File loaded and saved as ', file_path_with_name)

    except Exception as ex:
        print('Error while loading and saving file/n', ex)


svr_sct = create_server_socket('localhost', 666)
if svr_sct != -1:
    while True:
        clt_sct = accept_client_connection(svr_sct)
        if clt_sct != -1:
            load_and_save_file_info_to_mysql_database(clt_sct)
            load_and_save_data_to_file(clt_sct, 'test2.txt')

