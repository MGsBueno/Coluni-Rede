import json, time, constant
from Class import Client, PC_Info
from Methods import catch_error
from threading import Thread

def main():
    time_stamp = time.localtime()
    hour = time_stamp.tm_hour
    #operate time
    while (7 <= hour) and (hour < 18):
        client = Client()
        pc = PC_Info()
        try:
            client.connect(constant.HOST, constant.PORT)
            #client.connect('localhost', constant.PORT)
            if client:
                client.send(json.dumps(pc.__dict__))

            response = client.recv()
            print(response)
            
        
        except Exception as err:
            print("Server Offline")
            catch_error(err)
        client.close()
        time.sleep(300) #wait 5 minutes
        
if __name__ == "__main__":
        main()
    