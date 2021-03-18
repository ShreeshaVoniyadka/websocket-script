import json
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host ip address here
host = "localhost" 

# Port in the host where the application is running
port = 9999

# Connect to the server
s.connect((host, port))

while True:
    msg = input("Message: ")
    if msg.lower() == 'quit':
        data = {
            'flag' : False,
            "message" : ""
        }
        s.send(str.encode(json.dumps(data)))
        break
    else:
        data = {
            'flag' : True,
            "message" : msg
        }
        s.send(str.encode(json.dumps(data)))
        recvdata = json.loads(s.recv(1024).decode("utf-8"))
        print(recvdata['result'])