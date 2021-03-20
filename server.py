import socket
import sys
import json
import re
# import threading
import _thread
from db import SQL

def sendCommand(conn):
    while True:
        recvdata = json.loads(str(conn.recv(1024), "utf-8"))
        print(recvdata)
        try:
            # Invalid key value pairs in recieved data
            if recvdata['flag']:
                with SQL() as s:
                    s.execute(f"SELECT * FROM shops WHERE LOWER(area) LIKE '%{recvdata['message'].lower()}%' OR LOWER(name) LIKE '%{recvdata['message'].lower()}%'")
                    # data = [dict(i) for i in s.fetchall()]
                    initialData = s.fetchall()
                    data = list()
                    for i in initialData:
                        data.append(dict(i))
                # for items in mydb:
                #     if items['area'].lower().startswith(recvdata['message'].lower()):
                #         data.append(items)
                senddata = {'flag' : True if data else False, 'result' : data if data else list()}
                conn.send(str.encode(json.dumps(senddata)))
            else:
                conn.close()
                sys.exit()
        except Exception as e:
            senddata = {'flag' : False, 'result' : str(e)}
            print(json.dumps(senddata))
            conn.send(str.encode(json.dumps(senddata)))
        
     
        
# def abort(haha):
#     input("Abort? ")
#     s.close()
#     sys.exit()

host = "0.0.0.0"
port = 9999
s = socket.socket()
try:
    s.bind((host, port))    
    s.listen(5)
except socket.error as er:
    print("Data is not bound")

# _thread.start_new_thread(abort, (1,))
while True:
    try:
        conn, add = s.accept()
        print("Connection has been made \n IP:" + add[0]+"\nPort:"+str(add[1]))
        _thread.start_new_thread(sendCommand, (conn,))
    except socket.error as er:
        print("Not able to Connect")
s.close()