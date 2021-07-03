from ppadb.client import Client as AdbClient
from pynput.keyboard import Controller, Key

keyboard = Controller()
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]


def keyLog(v):
    key = v.split('<')[1].split('>')[0]
    print(key+' pressed')
    exec('keyboard.press(Key.' + key + ')')
    exec('keyboard.release(Key.' + key + ')')


def dump_logcat(connection):
    while True:
        data = connection.read(1024)
        if not data:
            break
        v = data.decode('utf-8').strip()
        if "Macronium-key" in v:
            keyLog(v)

    connection.close()


device.shell("logcat", handler=dump_logcat)
