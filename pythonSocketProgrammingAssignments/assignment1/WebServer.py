import sys # Used to terminate the web server
import threading
from socket import *

from WebServerUtility import *

def main():
    # Create the server socket
    # AF_INET - IPv4 address family
    # SOCK_STREAM - TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Server port number
    serverPort = 12000
    serverSocket.bind(('', serverPort))

    # Queue up incoming client requests
    counter = 0
    serverSocket.listen(5) # Max queue of 1 request

    while True:

        print('The server socket is listening...')
        connectionSocket, clientAddress = serverSocket.accept()

        counter += 1
        print(f'Accepted request {counter}')
        threading.Thread(target=handleRequestAt, args=(connectionSocket, clientAddress, counter)).start()

if __name__ == '__main__':
    main()

