import subprocess
import io
import qrcode

def getIPAddress():
    result = subprocess.run('ipconfig', stdout=subprocess.PIPE, text=True).stdout.lower()
    scan = 0
    for i in result.split('\n'):
        if 'wireless' in i: scan = 1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()

def makeQRCode():
    qr_text = getIPAddress()
    if qr_text is not None:
        imgIO = io.BytesIO()
        qr = qrcode.make(qr_text)
        qr.save(imgIO, ext='png')
        imgIO.seek(0)
        imgData = io.BytesIO(imgIO.read())
        return imgData