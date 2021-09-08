from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import os
import _locale
_locale._getdefaultlocale = (lambda *args: ['ru', 'cp866']) # декодировка полученных данных из ipconfig



Form, Window = uic.loadUiType("G:\\1234\\Лентяйка\\un1.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    global description
    result = os.popen('ipconfig /all')
    for line in result.readlines():
        #print(line)
        form.textBrowser_3.append(line)
    result.close()

def on_click_cmd():
    cmd = os.startfile("C:\Windows\System32\cmd.exe")

#def on_click_reboot():


#def on_click_netstat():
#    netstat -na



form.pushButton.clicked.connect(on_click)
form.pushButton_2.clicked.connect(on_click_cmd)
#description = form.textBrowser_3.toText()

app.exec_()


