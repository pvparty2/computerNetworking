import threading
from socket import *

def get():

    # Specify the server name / IP address and server port number
    serverName = 'serverName'
    serverPort = 12000

    # Client request message
    sentence = 'GET /HelloWorld.html HTTP/1.1'

    # Create the client socket
    # AF_INET - IPv4 
    # SOCK_STREAM - TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Create a TCP connection with the server
    clientSocket.connect((serverName, serverPort))

    # Send the encoded message through the client's socket over the TCP connection
    clientSocket.send(sentence.encode())

    # Get the server's encoded response
    modifiedSentence = clientSocket.recv(1024).decode()

    # Close the client's socket
    clientSocket.close()

def test():
    TOTAL = 10
    
    print(f'Sending {TOTAL} client requests to the web server...')
    
    for i in range(TOTAL):
        threading.Thread(target=get).start()

    print(f'All {TOTAL} client requests have been sent. Please check your web server standard output stream.')    

if __name__ == '__main__':
    test()

