import network
from umqtt.simple import MQTTClient
try:
    import usocket as socket
except:
    import socket

## HTTP REQUEST
HOST = "google.com"
PATH = ""
## MQTT REQUIRED
CLIENT_ID = "saksang"
BROKER = "test.mosquitto.org"
SUBSCRIBE = "/mdn/mydht11"

class Networks():
    def __init__(self):
        self.initWifi()

    def initWifi(self):
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('* connecting to network...')
            sta_if.active(True)
            sta_if.connect('bonet', 'Chelseafc231')
            while not sta_if.isconnected():
                pass
        print('* Connected to network')

    def send_data(self, data):
        c = MQTTClient(CLIENT_ID, BROKER)
        c.connect()
        msg = bytes('%s, %s' % (data[0], data[1]), 'utf8')
        subs = bytes('%s' % (SUBSCRIBE), 'utf8')
        c.publish(subs, msg)
        c.disconnect()

    def parse_data(self):
        import ujson
        data = ujson.loads(self.raw_data)
        return data['setup_time']

    def req_setup(self):
        print("* Requesting setup data..")
        s = socket.socket()
        addr = socket.getaddrinfo(HOST, 80)[0][-1]
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\n\r\n' % (PATH), 'utf8'))
        self.raw_data = str(s.recv(1024))
        s.close()
        return self.parse_data()
