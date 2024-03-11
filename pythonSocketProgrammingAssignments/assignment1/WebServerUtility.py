import os

def getFileContent(filename) -> str:
    
    # Read the contents of the file into a String variable
    serverPath = os.path.dirname(os.path.abspath(__file__))
    with open(f'{serverPath}/{filename}') as f:
        outputData = f.read()

    return outputData

def create200Response(body) -> str:
    '''Returns the 200 response message as a string.'''

    # Create the response line
    response = 'HTTP/1.1 200 OK\r\n'

    # Create the response headers
    responseHeaders = {
        'Connection' : 'close',
        'Content-Type': 'text/html',
        'Content-Length': len(body)
    }

    # Add the response headers to the response
    for k, v in responseHeaders.items():
        response += f'{k}: {v}\r\n'
    response += '\r\n'

    # Add the content to the body of the response        
    response += f'{body}\r\n'

    return response

def handleRequestAt(connectionSocket, clientAddress, counter):
    
    try:
        # Get the file name
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1][1:]
        
        # Read the contents of the file into outputData
        outputData = getFileContent(filename)

        # Create the 200 response
        response = create200Response(outputData)
        print(f'Created response for {counter}')

        # Send the response to the client
        connectionSocket.send(response.encode())
        print(f'Sent response for {counter}')

        # Close the TCP connection
        connectionSocket.close()
        print(f'Closed the connection for {counter}')

    except IOError:
        connectionSocket.send('HTTP/1.1 404 File Not Found\r\n'.encode())
        connectionSocket.close()