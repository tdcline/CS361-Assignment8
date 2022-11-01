# Hannah's PurpleAir Puller Microservice

# import modules
import socket
import requests

# setup api key
PURPLE_KEY = "868AB5A4-011D-11EC-BAD6-42010A800017"

# create socket
purpleSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
host = 'localhost'
port = 5050

# bind socket
purpleSocket.bind((host, port))

# listen for hams
purpleSocket.listen(5)

while True:
    # establish socket connection with hams
    hams, addr = purpleSocket.accept()
    
    # receive sensor ID
    sensor = hams.recv(1024).decode()
    
    # per assignment show microservice receiving data
    print("Received sensor ID from client: " + sensor)

    # grab sensor pm2.5 data from PurpleAir
    response = requests.get(f'https://api.purpleair.com/v1/sensors/{sensor}', headers={'X-API-KEY': PURPLE_KEY})
    data = response.json()['sensor']['stats']['pm2.5']

    # per assignment show pm2.5 data being sent back to client
    print("PM2.5 data being sent to client: " + str(data))
    
    # create string and send back to hams
    pmTwoFive = "{}".format(data).encode()
    hams.send(pmTwoFive)
    
    # end socket connection
    hams.close()
    break