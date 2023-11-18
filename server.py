import os
import socket


print("starting server program...")
print(os.getcwd())
os.chdir("./Server")
print(os.getcwd())
#Prompting user to enter the port number where the server should run
portN = input("Enter the port to start the server on: ")

#Creating a socket object and binding it to the loopback address
# and the port the user provided as an input
socketobject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketobject.bind(("127.0.0.1",int(portN)))

#Start listening on the port for any client connections
socketobject.listen()

#Accept a incomming connections from the client
clientsocket , clientdetails = socketobject.accept()
print("Accepted connection: "+ str(clientdetails))

#create an empty byte object for saving the data sent by the client
data = b""

while True:
    dataR = clientsocket.recv(1024)
    if len(dataR) ==0:
        break
    else:
        data = data + dataR
    print("data sent by the client is : " + dataR.decode("utf-8"))

