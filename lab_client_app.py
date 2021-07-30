import socket

svr_sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_sct.connect(('localhost', 666))
svr_sct.send(b'Ok')
response = svr_sct.recv(256)
print(response.decode())


try:
    file = open('test.txt', 'rb')
    file_part = file.read(256)
    print(len(file_part))
    while file_part != b'':
        print(len(file_part))
        svr_sct.send(file_part)
        file_part = file.read(256)

except:
    print('Something going wrong\n')

finally:
    file.close()
    svr_sct.close()
