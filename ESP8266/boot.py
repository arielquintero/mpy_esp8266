import esp
esp.osdebug(None)

import gc
gc.collect()

import machine
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('* woke from a deep sleep')
else:
    print('* power on or hard reset')

gc.collect()
