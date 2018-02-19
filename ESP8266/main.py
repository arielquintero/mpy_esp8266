import machine
import cNetwork
import cSensor


def sleep_time(slp):
    print('Time to sleep..')
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, slp)
    machine.deepsleep()


if __name__ == '__main__':
    net = cNetwork.Networks()
    dht = cSensor.sensors()
    values = dht.read_dht()
    print("values: ", values)
    net.send_data(values)
    setup_time = net.req_setup()
    print(setup_time)
    sleep_time(setup_time)
