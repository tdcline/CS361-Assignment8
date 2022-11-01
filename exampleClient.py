""" Test client that sends an example sensor ID as the hams program would to
    the Hannah's Microservice.py program."""
import socket

# create socket
newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 5050

# establish connection
newSocket.connect((host, port))

sensor = "163811"

# per assignment show data to send
print("Sending sensor ID: " + sensor)

# send new sensor ID through socket
newSocket.send(sensor.encode())

# receive pm2.5 data
pmData = newSocket.recv(1024).decode()

# print data to terminal for assignment
print("Received pm2.5 data: " + pmData)

# terminate connection
newSocket.close()