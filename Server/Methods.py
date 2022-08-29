import json
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

def search(data, list):
    info = json.loads(data)
    return [user for user in list if user._mac_address == info["_mac_address"]]


def status(stored_pc,status):
    if status == "Online": 
        return type(stored_pc).connection_status.fset(stored_pc,"Online")
    return type(stored_pc).connection_status.fset(stored_pc,"Offline")


def write_log(info,arq):
    pass

def read_log(info,arq):
    pass


def print_item(online):
    [print("------------------\nClient ID:%d"%item._id, item, end = "\n\n") for item in online if item._connection_status == "Online"]
    
    