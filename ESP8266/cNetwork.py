import network
from umqtt.simple import MQTTClient
try:
    import urequests as requests
except ImportError:
    import requests

## HTTP REQUEST
HOST = "URL"
PATH = ""
PORT = 3000
## MQTT REQUIREDD
CLIENT_ID = "saksang"
BROKER = "test.mosquitto.org"
SUBSCRIBE = "" #subscribe path

class Networks():
    def __init__(self):
        self.initWifi()

    def initWifi(self):
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('* connecting to network...')
            sta_if.active(True)
            sta_if.connect('ssid', 'pass')
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

    def parse_data(self, raw_data):
        import ujson
        print(raw_data)
        return ujson.loads(raw_data)

    def req_setup(self):
        print("* Requesting setup data..")
        r = requests.get("http://%s:%s/%s" % (HOST, PORT, PATH))
        import ujson
        data = ujson.loads(r.json())    #still has to be parsed again
        r.close()
        return data['setup_time']
