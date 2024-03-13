import random # Used to generate randomized lost packets
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign the IP address and port number to the socket
serverSocket.bind(('', 12000))
print('Server is running...')

while True:

    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the client address
    message, address = serverSocket.recvfrom(1024)

    # Capitalize the message from the client
    message = message.decode().upper()

    # Drop a packet by randomness
    if (rand < 4):
        continue

    # Send the response
    serverSocket.sendto(message.encode(), address)