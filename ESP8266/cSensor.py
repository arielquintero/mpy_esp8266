import dht
from machine import Pin

class sensors():
    def __init__(self):
        self.dht11 = dht.DHT11(Pin(14))

    def read_dht(self):
        self.dht11.measure()
        return [
            self.dht11.temperature(),
            self.dht11.humidity()
        ]
