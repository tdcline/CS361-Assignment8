README
# CS361-Assignment8
Microservice for PurpleAir API call through Python sockets
------------------------------------------------------------------------------
HOW TO REQUEST DATA
Data requests through this microservice are performed through Python Sockets.
1. The client should import the socket module
2. The socket host is 'localhost' and the port number is '5050'.
3. Create a new socket and use the connect function to open a socket connection with the microservice at the given host and port.
4. Identify the sensor ID to send to the microservice as a string of integers.
5. Send the sensor ID through the socket using the encode and send functions.

Example code:

import socket

newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 5050

newSocket.connect((host, port))

sensor = "11111"

newSocket.send(sensor.encode())
------------------------------------------------------------------------------

HOW TO RECEIVE DATA
Data is received from the microservice sequentially using the same socket with which requests are made. Thus, in order to receive data, a request must be made first.
1. Use the decode and recv functions of the socket module to receive data after sending a sensor ID to the microservice.
2. The receiving data will be a string in the form of the PM2.5 data received from the PurpleAir API. For example: '5.1'. 
3. Close the socket after receiving data since the microservice closes it's end after data is requested and sent.

Example code:

pmData = newSocket.recv(1024).decode()

newSocket.close()
