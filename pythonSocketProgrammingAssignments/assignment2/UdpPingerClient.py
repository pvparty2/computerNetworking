import datetime
from socket import *

# Set the server details
serverName = 'serverNameHere'
serverPort = 12000


for i in range(10):
    # Create the client UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Create the timeout for the socket to 1 second
    clientSocket.settimeout(1)

    # Create the message
    message = f'ping {i + 1}'

    # Ping the server
    time1 = datetime.datetime.now()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    # Try to get the server response
    try:
        
        # Get the response from the server
        response, address = clientSocket.recvfrom(1024)

        # Calculate the time delta
        time2 = datetime.datetime.now()
        deltaMicroseconds = f'{(time2.second - time1.second) * 100 + (time2.microsecond - time1.microsecond) / 10000}ms'
        print(f'{response.decode()} ({deltaMicroseconds})')

    except TimeoutError:
        print('REQUEST TIMED OUT')

