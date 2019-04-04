import socket

def sendData(data, IP, server):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, server))
        s.sendall(data.encode())
        s.close()

def receiveData(IP, server):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP, server))
        s.listen(5)
        while True:
            c, addr = s.accept()
            dataTaken = c.recv(1024).decode()
            c.close()
        return dataTaken