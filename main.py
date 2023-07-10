from ppadb.client import Client

adb = Client(host="127.0.0.1", port=5037)
device = adb.device("emulator-5554")
if device is None:
    print("no device")
    quit()

while True:
    device.shell(f'input touchscreen swipe 540 1700 540 1300 100')
