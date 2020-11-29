import socket
import os
from _thread import *

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8888
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

    filename = input(str("Enter filename of the file :"))
    file = open(filename, 'rb')
    file_data = file.read(1024)
    Client.send(file_data)
    print("file transferred successfully")

#    filename = input(str("Enter file name to save :"))
#    file = open(filename, 'wb')
#    file_data = ServerSocket.recv(1024)
#    file.write(file_data)
#    file.close()
#    print('file has been received successfully')

ServerSocket.close()
