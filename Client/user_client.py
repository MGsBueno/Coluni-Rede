import time, platform, re,uuid,json,logging, socket
from Class import Client, PC_Info


host = 'LOCALHOST'
port = 8080

i=1
data = []
while True:
    client = Client()
    pc = PC_Info()
    client.connect(host, port).send(json.dumps(pc.__dict__))
    i+=1
    response = client.recv()    
    
    client.close()
    time.sleep(10)