import json, socket, platform, re, uuid, time

from Methods import _recv, _send

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
    def __init__(self):
        self._platform = platform.system()
        self._platform_release=platform.release()
        self._platform_version = platform.version()
        self._architecture = platform.machine()
        self._hostname = socket.gethostname()
        self._ip_address = socket.gethostbyname(socket.gethostname())
        self._mac_address =':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self._processor = platform.processor()
        self.name = None
        self._sector = None
        super().__init__()
    
    def __str__(self):
        date = super().__str__()
        return ("\n\nComputer: {}\nSector: {}\nPlatform: {} {}, version: {}\nArchitecture: {}\nProcessor: {}\nHostname {}\nIP: {}, mac: {}\n{}\nStatus: {}" 
            .format
            (
                self.name, self._sector, self._platform, self._platform_release, self._platform_version, self._architecture,
                self._processor, self._hostname, self._ip_address, self._mac_address, date, self._connection_status
            )
        )

   
   
    
    def Compare_time(self):
        time_stamp = time.localtime()
        if(self.year<time_stamp[0] | self.month<time_stamp[1] | self.day<time_stamp[2]
        | (self.hour*60< + self.min <  time_stamp[3]*60 + time_stamp[4])
        ):
            self.connection_status("Offline")
        else:self.connection_status("Online")
    
class Client(object):
    """
    A JSON socket client used to communicate with a JSON socket server. All the
    data is serialized in JSON. How to use it:

    data = {
    'name': 'Patrick Jane',
    'age': 45,
    'children': ['Susie', 'Mike', 'Philip']
    }
    client = Client()
    client.connect(host, port)
    client.send(data)
    response = client.recv()
    # or in one line:
    response = Client().connect(host, port).send(data).recv()
    """

    socket = None        
    def __del__(self):
        self.close()

    def connect(self, host, port):
        self.socket = socket.socket()
        self.socket.connect((host, port))
        return self

    def send(self, data):
        if not self.socket:
            raise Exception('You have to connect first before sending data')
        _send(self.socket, data)
        return self

    def recv(self):
        if not self.socket:
            raise Exception('You have to connect first before receiving data')
        return _recv(self.socket)

    def recv_and_close(self):
        data = self.recv()
        self.close()
        return data

    def close(self):
        if self.socket:
            self.socket.close()
            self.socket = None

