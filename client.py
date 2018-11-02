#program untuk client

import socket

handlerSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 2222

handlerSocket.connect((serverIP,serverPort))
print 'terkoneski ke server'

while True:
    message = handlerSocket.recv(1024)
    print 'Pesan dari server : ',message
    message = raw_input("Masukkan pesan anda : ")
    handlerSocket.send(message)

    pass
