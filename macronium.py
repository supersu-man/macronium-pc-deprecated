from helper import helper_string
from qr import makeQRCode
import socket
from pynput.keyboard import Controller, Key
import threading
from kivy.config import Config

Config.set('kivy', 'window_icon', 'ICON.ico')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'multisamples', '0')

from kivy.lang import Builder
from kivymd.app import MDApp


class Macronium(MDApp):
    thread = threading.Thread()

    def build(self):
        makeQRCode()
        return Builder.load_string(helper_string)

    def on_start(self):
        self.root.ids.img.source = 'myqr.png'
        self.thread = threading.Thread(target=self.startListening, daemon=True)
        self.thread.start()

    def startListening(self):
        while True:
            self.root.ids.label.title = "Waiting for connection..."
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('', 6969))
            s.listen(5)
            conn, addr = s.accept()
            v = 'Connected by ' + str(addr[0])
            self.root.ids.label.title = v
            print(v)
            while True:
                data = conn.recv(1024)
                request_string = data.decode("utf-8")
                if not data:
                    self.root.ids.label.title = "Waiting for connection..."
                    break
                if 'Macronium-key' in request_string:
                    key = request_string.split('<')[1].split('>')[0]
                    print(key + ' pressed')
                    self.pressKey(key)
                print(request_string)
            s.close()

    def pressKey(self, key):
        keyboard = Controller()
        if '+' not in key:
            if 'Key' in key:
                exec('keyboard.press(' + key + ')')
                exec('keyboard.release(' + key + ')')
            else:
                exec('keyboard.press(\'' + key + '\')')
                exec('keyboard.release(\'' + key + '\')')

        else:
            keys = key.split('+')
            for i in keys:
                if 'Key' in i:
                    exec('keyboard.press(' + i + ')')
                else:
                    exec('keyboard.press(\'' + i + '\')')
            keys.reverse()
            for i in keys:
                if 'Key' in i:
                    exec('keyboard.release(' + i + ')')
                else:
                    exec('keyboard.release(\'' + i + '\')')


Macronium().run()
