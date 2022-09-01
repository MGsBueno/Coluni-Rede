import json, time, os, time, constant

def _send(socket, data):
    try:
        serialized = json.dumps(data)
    except (TypeError, ValueError):
        raise Exception('You can only send JSON-serializable data')
    # send the length of the serialized data first
    socket.send(('%d\n' % len(serialized)).encode())
    # send the serialized data
    socket.sendall(serialized.encode())

def _recv(socket):
# read the length of the data, letter by letter until we reach EOL
    length_str = ''
    char = socket.recv(1).decode()
    while char != '\n':
        length_str += char
        char = socket.recv(1).decode()
        total = int(length_str)
# use a memoryview to receive the data chunk by chunk efficiently
    view = memoryview(bytearray(total))
    next_offset = 0
    while total - next_offset > 0:
        recv_size = socket.recv_into(view[next_offset:], total - next_offset)
        next_offset += recv_size
    try:
        deserialized = json.loads(view.tobytes())
    except (TypeError, ValueError):
        raise Exception('Data received was not in JSON format')
    return deserialized

def catch_error(err):
    print(err)
    instant = time.localtime()
    error = ("Error: {}, {}"
    .format(err,err))

    msg_err = ("{}/{}/{} - {}:{}:{} - " 
    .format(
        instant[2],instant[1],instant[0],   #date
        instant[3],instant[4],instant[5])   #time
        )
        

    f = open(constant.LOGS+"\\log.txt","a")
    print("saving log")
    f.write(str(msg_err)+" Server Unavailable "+"\n")        
    f.close()

def create_directory(address):
    try: 
        os.mkdir(address)
        print("Directory created")
    except FileExistsError:
        print("directory already exists!\n")

def save_dns_address(date,hour, minute):
    logs = constant.LOGS+"\\"+date+"\\"+str(hour)+"h-"+str(minute)+"min"
    os.system(' cmd /c ipconfig /displaydns > %s.txt' %logs)

def get_date():
    time_stamp = time.localtime()
    day = str(time_stamp.tm_mday)
    month = str(time_stamp.tm_mon)
    year= str(time_stamp.tm_year)
    today=day+'-'+month+'-'+year
    return today

def get_hour():
    time_stamp = time.localtime()
    hour= str(time_stamp.tm_hour)
    minute= str(time_stamp.tm_min)
    hour_min = hour+"-"+minute
    return hour_min

