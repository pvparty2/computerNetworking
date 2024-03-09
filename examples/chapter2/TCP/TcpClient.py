from socket import *

# Specify the server name / IP address and server port number
serverName = '192.168.1.105'
serverPort = 12000

# Create the client socket
# AF_INET - IPv4 
# SOCK_STREAM - TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Create a TCP connection with the server
clientSocket.connect((serverName, serverPort))

# Print the client socket port number assigned by OS to this process
print('Client Port Number: ' + str(clientSocket.getsockname()[1]))
print('Server Port Number: ' + str(clientSocket.getpeername()[1]))

# Get the message from the user
sentence = input('Input lowercase sentence: ')

# Send the encoded message through the client's socket over the TCP connection
clientSocket.send(sentence.encode())

# Get the server's encoded response
modifiedSentence = clientSocket.recv(1024)

print('From Server: ' + modifiedSentence.decode())

# Close the client's socket
clientSocket.close()
