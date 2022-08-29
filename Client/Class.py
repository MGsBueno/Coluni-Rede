import json, socket, platform, re, uuid

from Methods import _recv, _send

class PC_Info ():
    def __init__(self):
        self._platform = platform.system()
        self._platform_release=platform.release()
        self._platform_version = platform.version()
        self._architecture = platform.machine()
        self._hostname = socket.gethostname()
        self._ip_address = socket.gethostbyname(socket.gethostname())
        self._mac_address =':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self._processor = platform.processor()
    
    def __str__(self):
        return ("\n\nComputer: {}\nSector: {}\nPlatform: {} {}, version: {}\nArchitecture: {}\nProcessor: {}\nHostname {}\nIP: {}, mac: {}\n" 
            .format
            (
                self.name, self._sector, self._platform, self._platform_release, self._platform_version, self._architecture,
                self._processor, self._hostname, self._ip_address, self._mac_address)
        )
   
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
        try:
            self.socket = socket.socket()
            self.socket.connect((host, port))
            return self
        except InterruptedError: return None



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

