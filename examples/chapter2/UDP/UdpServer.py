from socket import *

# Initialize the server socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# Print the status of the server
print("The server is ready to receive.")

while True:

    # Get the client's message and IP address
    message, clientAddress = serverSocket.recvfrom(2048)

    # Convert the message to upper case
    modifiedMessage = message.decode().upper()

    # Send the modified message back to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)