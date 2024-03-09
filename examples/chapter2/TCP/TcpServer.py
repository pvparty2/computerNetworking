from socket import *

# Assign a port number to the server socket
serverPort = 12000

# Create the server socket that listens for connection requests
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server IP address (local host) and port number to the socket 
serverSocket.bind(('', serverPort))

# The maximum number of queued connections is 1
serverSocket.listen(1)
print('The server socket is ready to receive on Port: ' + str(serverSocket.getsockname()[1]))

while True:

    # Accept any client connections
    connectionSocket, address = serverSocket.accept()
    
    # Print the client's IP address and port number
    clientIp = connectionSocket.getpeername()[0]
    clientPort = connectionSocket.getpeername()[1]
    print('Accepted connection request from: ' + str(clientIp) + ':' + str(clientPort))

    # Get the client's message from TCP 
    sentence = connectionSocket.recv(1024).decode()

    # Perform server-side operation
    capitalizedSentence = sentence.upper()

    # Send the modified message to the client
    connectionSocket.send(capitalizedSentence.encode())

    # Close the TCP connection
    connectionSocket.close()