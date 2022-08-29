import socket, time, json
from Methods import _recv, _send

class Server(object):

    """
    A JSON socket server used to communicate with a JSON socket client. All the
    data is serialized in JSON. How to use it:

    server = Server(host, port)
    while True:
    server.accept()
    data = server.recv()
    # shortcut: data = server.accept().recv()
    server.send({'status': 'ok'})
    """

    backlog = 5
    client = None

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(self.backlog)
        
    
    def __del__(self):
        self.close()

    def accept(self):
        # if a client is alreadyp    connected, disconnect it
        if self.client:
            self.client.close()
        self.client, self.client_addr = self.socket.accept()
        return self

    def send(self, info):
        if not self.client:
            raise Exception('Cannot send data, no client is connected')
        _send(self.client, info)
        return self

    def recv(self):
        if not self.client:
            raise Exception('Cannot receive data, no client is connected')
        return _recv(self.client)

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
        if self.socket:
            self.socket.close()
        self.socket = None

class Date():   
    def __init__(self):
            time_stamp = time.localtime()
            self.year = time_stamp[0]  
            self.month = time_stamp[1]
            self.day = time_stamp[2]
            self.hour = time_stamp[3]
            self.minute = time_stamp[4]
            self.second = time_stamp[5]
                   
    def __str__(self):
            #Inicial data
            return("Online at: {}/{}/{} , {}:{}:{}" 
                .format(
                    self.day,self.month, self.year, 
                    self.hour, self.minute, self.second
                )
            )
            
    def update_stats(self):
        self.year = time.localtime([0])
        self.month = time.localtime([1])
        self.day = time.localtime([2])
        self.hour = time.localtime([3])
        self.minute = time.localtime([4])
        self.initial_second = time.localtime([5])

class PC_Info (Date):
    def __init__(self,data,id,label):
        info = json.loads(data)
        self._platform = info["_platform"]
        self._platform_release=info["_platform_release"]
        self._platform_version = info["_platform_release"]
        self._architecture = info["_architecture"]
        self._hostname = info["_hostname"]
        self._ip_address = info["_ip_address"]
        self._mac_address =info["_mac_address"]
        self._processor = info["_processor"]
        self._name = label["name"]
        self._sector = label["sector"]
        self._id = id
        self._connection_status = "Online"
        super().__init__()
    
    def __str__(self):
        date = super().__str__()
        return ("\n\nComputer: {}\nSector: {}\nPlatform: {} {}, version: {}\nArchitecture: {}\nProcessor: {}\nHostname {}\nIP: {}, mac: {}\n{}\nStatus: {}" 
            .format
            (
                self._name, self._sector, self._platform, self._platform_release, self._platform_version, self._architecture,
                self._processor, self._hostname, self._ip_address, self._mac_address, date, self._connection_status
            )
        )
            
    @property
    def connection_status(self): #getting method of status
        return self._connection_status
    
    
    #setter method status
    @connection_status.setter
    def connection_status(self, status):
        self._connection_status = status

    
            
    def update_time_stats(self):
        time_stamp = time.localtime()
        self.year = time_stamp[0]  
        self.month = time_stamp[1]
        self.day = time_stamp[2]
        self.hour = time_stamp[3]
        self.minute = time_stamp[4]
        self.second = time_stamp[5]
