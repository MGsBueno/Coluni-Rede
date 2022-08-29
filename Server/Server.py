from asyncio import constants
from Class import Server, PC_Info, Date
from Methods import *
import time, constant

time_stamp_instant ={"hour":7, "minute":30} #work time/ to be updated every 30min
time_stamp = time.localtime()


def _online_routine(server, data,online,i):
    
    if online == [] or search(data,online) == []:
        #creating a new object client
        if len(online)==0:
            id = 1
        else:
            id = len(online)+1

        label = {"name" : "default_user", "sector" :"default"}
        stored_pc = PC_Info(data,id,label)
        online.append(stored_pc)
        print_item(online)
           
    else:
        stored = search(data,online)
        stored[0].update_time_stats()
        #print online itens on list
        print_item(online)
    i+=1
    [status(item,"Offline") for item in online if ((item.day<time_stamp[2]) or ((item.hour*60+item.minute)<((time_stamp[3]*60+time_stamp[4])/2)))]
    date = Date()
    server.send("Conected and stored data, " + str(date))
    return i

def _storing_routine(online, i):
    f = open("logs\log.txt","a")
    print("saving log")        
    f.write("----------  Beginning of the Iteration ----------\n")
    f.write("Iteration nº %d, Current Online Users: \n" %i)
    [f.write(str(client)) for client in online if online !=[]]
    f.write("\n----------  End of the Iteration ----------\n")
    f.close()

def main():
    server = Server(constant.HOST, constant.PORT)
    #server = Server('localhost', constant.PORT)
    online = [] #list of clients online -> todo: Using a database to store
    i=0
    time_stamp_instant ={"hour":7, "minute":30} #work time/ to be updated every 30min 

    while True:
        time_stamp = time.localtime()
        server.accept()
        data = server.recv()
        if not data:
            print("closed connections \n")
            break
        #server.send({"response":data})
        i = _online_routine(server,data,online,i)
        
        if  (time_stamp.tm_hour*60+time_stamp.tm_min) - (time_stamp_instant["hour"]*60+ time_stamp_instant["minute"]>=30): #30 min range
            _storing_routine(online, i)#generating a log
            online = []
            time_stamp_instant["hour"] = time_stamp.tm_hour
            time_stamp_instant["minute"] = time_stamp.tm_min
    server.close()
    _storing_routine(online, i)

if __name__ == "__main__":
        main()