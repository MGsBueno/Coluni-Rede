import json, time, constant
from Class import Client, PC_Info
from Methods import *

def main():
    time_stamp = time.localtime()
    target = constant.LOGS+"\\"+daily_hitory
    print(target)
    create_directory(target)
    

    hour = time_stamp.tm_hour
    minute= time_stamp.tm_min
    #operate time
    i = 0
    response = None
    while (7 <= hour) and (hour < 18):
        client = Client()
        pc = PC_Info()
        try:
            client.connect(constant.HOST, constant.PORT)
            #client.connect('localhost', constant.PORT)
            client.send(json.dumps(pc.__dict__))
            response = client.recv()
            client.send()
            print(response)
            
        
        except Exception as err:
            print("Server Offline")
            catch_error(err)
        client.close()
        
        if i==0  or  i%12: #every hour 
            today_folder=get_date()
            save_dns_address(today_folder,hour,minute)
            print("dns stored")
            print("step %d"%i)
            i+=1
           
        time.sleep(300) #wait 5 minutes
        
if __name__ == "__main__":
        time_stamp = time.localtime()
        daily_hitory = get_date()
        main()

    