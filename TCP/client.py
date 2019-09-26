from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input("enter the file name")
clientSocket.send(sentence.encode())
fileContent=clientSocket.recv(1024).decode()
print("fileContent:",fileContent)
clientSocket.close()
