import socket
import os

#Changing CWD and opening the pdf file
#in binary mode to send it over the socket
os.chdir("./Client")
print(os.getcwd())

pdfbinary = open("./RohanMalik.pdf","rb")



hostN= input ("Please enter the host name:")
portN= input ("please enter the port number :")

#creating a socket object 
socketobject = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket to the ip and the port number
socketobject.connect(("127.0.0.1",int(portN)))

print("connection est. successfully!")
while True:
    dataS= input ("Input =>: ")
    socketobject.send(dataS.encode("utf-8"))
    print("sent the data successfully!")
