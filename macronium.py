from helper import helper_string
from qr import makeQRCode
import socket
from pynput.keyboard import Controller, Key
import threading
from kivy.config import Config
from update import get_latest, isInternet
import webbrowser

version = "1.2"
url = "https://github.com/supersu-man/Macronium-PC/releases/latest"

Config.set('kivy', 'window_icon', 'ICON.ico')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'multisamples', '0')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class Macronium(MDApp):
    dialog = None

    def build(self):
        makeQRCode()
        return Builder.load_string(helper_string)

    def on_start(self):
        self.root.ids.img.source = 'myqr.png'
        thread = threading.Thread(target=self.startListening, daemon=True)
        thread2 = threading.Thread(target=self.check_forUpdate, daemon=True)
        thread.start()
        if isInternet():
            thread2.start()

    def check_forUpdate(self):
        if get_latest(url) != version:
            self.dialog = MDDialog(
                title="New update found!!",
                text="Would you like to download the latest version?",

                buttons=[
                    MDFlatButton(
                        text="CANCEL", theme_text_color="Custom",
                        text_color=[0.5294117647, 0.50588235294, 0.74117647058, 1],
                        on_release=self.dismissDialog
                    ),
                    MDFlatButton(
                        text="OPEN", theme_text_color="Custom",
                        text_color=[0.5294117647, 0.50588235294, 0.74117647058, 1],
                        on_release=self.openLink
                    ),
                ],
            )

            self.dialog.open()

    def openLink(self, obj):
        webbrowser.open(url)
        self.dismissDialog(obj)

    def dismissDialog(self, obj):
        self.dialog.dismiss(force=True)

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
                    self.pressKey(key)
                if 'Macronium-link' in request_string:
                    link = request_string.split('<')[1].split('>')[0]
                    webbrowser.open(link)
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
