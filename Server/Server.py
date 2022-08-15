from Class import Server, PC_Info
from Methods import _send, _recv, _search
import json




host = 'LOCALHOST'
port = 8080
online = []
server = Server(host, port)
i=0


while True:
    server.accept()
    data = server.recv()
    if not data:
        print("closed connections \n")
        break
    server.send({"response":data})
    
    if online == [] or _search(json.loads(data),online) == []:
        #creating a new object client
        if len(online)==0:
            id = 0
        else:
            id = len(online)
        
       
        student = json.loads(data)
        print(student)

        #online.append(client)
        
        
        """client = Client()
        online.append(data)
        tam = len(online)
        online[tam-1].id = tam
        print(online)"""
    i+=1
server.close()

