#program untuk server

import socket

listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

listenerSocket.bind((serverIP,serverPort))
listenerSocket.listen(0)

while True:
    handlerSocket, addr = listenerSocket.accept()
    print 'Sebuah client baru telah terkoneski dengan alamat : ',addr
    while True:
        message = raw_input("Masukkan pesan anda : ")
        handlerSocket.send(message)
        message = handlerSocket.recv(1024)
        print 'Pesan dari client : ',message
        pass
    pass
