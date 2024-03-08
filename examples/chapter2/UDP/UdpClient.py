from socket import *

# Server information
# Replace 'hostname' with the IP address or host-name of the host that is running UdpServer.py
serverName = 'hostname'
serverPort = 12000

# Initialize client's socket
# AF_INET - IPv4
# SOCK_DGRAM - UDP socket
# Note: not specifying a port number; the OS will handle that
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Message
message = input('Input lowercase sentence: ')

# Send the message to the server
# Client's IP address is attached automatically to the message
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Get the server's response and IP address
# Client waits to receive the data
serverResponse, serverAddress = clientSocket.recvfrom(2048)

# Print the server's message
print(serverResponse.decode())

# Close the client's socket
clientSocket.close()