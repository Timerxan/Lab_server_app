import socket

svr_sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_sct.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
svr_sct.bind(('localhost', 666))
svr_sct.listen(1)

while True:
    try:
        clt_sct, addr = svr_sct.accept()
        print('Connection from', addr)


        while True:
            request = clt_sct.recv(256)
            print(request.decode())
            response = 'You are connected\n'.encode()
            clt_sct.send(response)
    except:
        print('Something wrong.')