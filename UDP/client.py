from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
sentence=input("enter the file name")
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))
fileContent,serverAddress=clientSocket.recvfrom(2048)
print("fileContent:",fileContent)
clientSocket.close()
