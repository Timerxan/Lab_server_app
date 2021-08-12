import socket

svr_sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_sct.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
svr_sct.bind(('localhost', 666))
svr_sct.listen(1)

while True:
    try:
        clt_sct, addr = svr_sct.accept()
        print('Connection from', addr)
        response = 'You are connected\n'.encode()
        clt_sct.send(response)
        file = open('test2.txt', 'wb')

        request = clt_sct.recv(256)
        while request != b'':

            file.write(request)
            request = clt_sct.recv(256)

    except:
        print('Something wrong')
    finally:
        print('Done')
        file.close()