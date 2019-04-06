import socket
import threading

def sendData(dataToSend, serverIp, serverPort):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((serverIp, serverPort)) #connect to server
        print("Data sent to server: " + dataToSend)
        s.sendall(dataToSend.encode()) # send all the data
        data = s.recv(1024).decode()
        print("Data returned from server: " + data)
        s.close() #close connection to server

def recieveData(serverIp, serverPort):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((serverIp, serverPort))  # server attaches itself to the port
        s.listen(5)  # listening for connections from client
        while True:
            c, addr = s.accept()  # wait for a connection and accept
            dataRecieved = c.recv(1024).decode()  # recieve the data sent
            print("Data recieved from client:" + dataRecieved)
            dataToSendBack = "Thank you for connecting"
            print("Data send back to client: " + dataToSendBack)
            c.send(dataToSendBack.encode())
            c.close()  # close the connection


threading.Thread(target=recieveData, args=('206.87.3.92', 65432)).start() #insert your ip

