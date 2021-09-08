from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import os
import pickle
import _locale
_locale._getdefaultlocale = (lambda *args: ['ru', 'cp866']) # декодировка полученных данных из ipconfig



Form, Window = uic.loadUiType("G:\\1234\\Lenivka\\un1.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click_ipconfig():
    form.textBrowser_3.clear() #очистка рабочего поля
    result = os.popen('ipconfig /all')
    for line in result.readlines():
        #print(line)
        form.textBrowser_3.append(line)
        result.close()
    # def on_click_ipconfig_save():
    #     form.pushButton_19.clicked.connect()
    #     #print(a)
    #     file1 = open('C:\\1\\ipconfig.txt', "wb")
    #     pickle.dump(result.readlines, file1)
    #     print(result.readlines)
    #     file1.close()
# def on_click_ipconfig_save():
#     dsave = {''}
#     file1 = open('C:\\1\\ipconfig.txt', "a")
#     pickle.dump(form.textBrowser_3, file1)
#     file1.close()



def on_click_cmd(): # окно CMD
    cmd = os.startfile("C:\Windows\System32\cmd.exe")


def on_click_rebot(): # reboot
    rebot = os.popen("shutdown -r -f -t 5")
    print(rebot)

def on_click_rebot_ot(): # отмена reboot
    rebot_ot = os.popen("shutdown /a")
    print(rebot_ot)


def on_click_netstat(): # команда netstat
    form.textBrowser_3.clear()
    result = os.popen('netstat -na')
    for line in result.readlines():
        #print(line)
        form.textBrowser_3.append(line)
    result.close()
   
def on_click_ping(): # команда ping
    form.textBrowser_3.clear()
    ip_adress1 = form.plainTextEdit.toPlainText()
    result = os.popen('ping ' + ip_adress1)  # эта функция пинг
    for line in result.readlines():
        form.textBrowser_3.append(line)
        print(ip_adress1)
    result.close()


# def on_click_telnet(): # команда telnet
#     form.textBrowser_3.clear()
#     ip_adress1 = form.plainTextEdit.toPlainText()
#     tel_net = form.plainTextEdit_2.toPlainText()
#     #cmd = os.startfile("C:\Windows\System32\cmd.exe" + ip_adress1 + tel_net)
#     result = os.popen('telnet' + ip_adress1 + tel_net)  # эта функция пинг
#     for line in result.readlines():
#         form.textBrowser_3.append(line)
#         print(result)
#     #result.close()


form.pushButton.clicked.connect(on_click_ipconfig)
#form.pushButton_19.clicked.connect(on_click_ipconfig_save)
form.pushButton_2.clicked.connect(on_click_cmd)
form.pushButton_3.clicked.connect(on_click_rebot)
form.pushButton_21.clicked.connect(on_click_rebot_ot)
form.pushButton_4.clicked.connect(on_click_netstat)
form.pushButton_18.clicked.connect(on_click_ping)
# form.pushButton_17.clicked.connect(on_click_telnet)

app.exec_()


