import socket
import sys
import json
import re

mydb = [
    {
        'area' : 'Mattikere',
        'id' : 2,
        'name' : 'jhfdjknfsd'
    },
    {
        'area' : 'matthhsjh',
        'id' : 3,
        'name' : 'fghfghcvncgfh'
    },
    {
        'area' : 'mjgsdjkfsfd',
        'id' : 4,
        'name' : 'hfgcvfghf'
    },
    {
        'area' : 'mahjgadjksnsmfn',
        'id' : 5,
        'name' : 'dhfgfhfth'
    },
    {
        'area' : 'hgsfjhdfjk',
        'id' : 6,
        'name' : 'dhghfth'
    },
    {
        'area' : 'Mattikere',
        'id' : 2,
        'name' : 'jhfdjknfsd'
    }
]

def sendCommand(conn):
    while True:
        recvdata = json.loads(str(conn.recv(1024), "utf-8"))
        print(recvdata)
        if recvdata['flag']:
            data = []
            for items in mydb:
                if items['area'].lower().startswith(recvdata['message'].lower()):
                    data.append(items)
            senddata = {'flag' : True if data else False, 'result' : data if data else list()}
            print(data, senddata)
            conn.send(str.encode(json.dumps(senddata)))

        else:
            conn.close()
            s.close()
            sys.exit()

host = "0.0.0.0"
port = 9999
s = socket.socket()

s.bind((host, port))
s.listen(5)

conn, add = s.accept()
print("Connection has been made \n IP:" + add[0]+"\nPort:"+str(add[1]))
sendCommand(conn)

conn.close()

