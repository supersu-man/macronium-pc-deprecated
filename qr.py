import subprocess
import pyqrcode


def getIPAddress():
    result = subprocess.run('ipconfig', stdout=subprocess.PIPE, text=True).stdout.lower()
    scan = 0
    for i in result.split('\n'):
        if 'wireless' in i: scan = 1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()


def makeQRCode():
    qr = getIPAddress()
    if qr is not None:
        url = pyqrcode.create(qr)
        url.png('myqr.png', scale=10, quiet_zone=3)
