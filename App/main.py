# Application for controlling Relay box 4 channel
# THT5HC

import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import datetime
import configparser
# GUI FILE
from ui_main import Ui_MainWindow
# IMPORT FUNCTIONS
from relay_func import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.port = 'COM9'
        self.readSetting()
         ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        

        self.show()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateUI)
        self.timer.start()

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        # SETTING
        self.ui.settingsTopBtn.clicked.connect(lambda:self.showDiaglog())

        # MOVE WINDOW
        self.ui.title_bar.mouseMoveEvent = self.moveWindow
        try:
            com = Relay_Serial(self.port)
            com.open()
            com.send('VOFF\n')
        except Exception as e:
            print(e)
            pass

        # RELAY FUNCTION
        self.ui.relay1.stateChanged.connect(lambda: self.turn_on(1 if self.ui.relay1.isChecked() else 0))
        self.ui.relay2.stateChanged.connect(lambda: self.turn_on(2 if self.ui.relay2.isChecked() else 0))
        self.ui.relay3.stateChanged.connect(lambda: self.turn_on(3 if self.ui.relay3.isChecked() else 0))
        self.ui.relay4.stateChanged.connect(lambda: self.turn_on(4 if self.ui.relay4.isChecked() else 0))

        #SAVE NOTES
        self.ui.note1.mousePressEvent = self.Changed
        self.ui.note2.mousePressEvent = self.Changed
        self.ui.note3.mousePressEvent = self.Changed
        self.ui.note4.mousePressEvent = self.Changed

    def updateUI(self):
        self.ui.label_time.setText(datetime.datetime.now().strftime("%I:%M:%S %p"))
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    
    def turn_on(self, channel):
        print('RELAY: %s'%channel)
        try: 
            com = Relay_Serial(self.port)
            com.open()
            com.send('VSET%s\n'%channel)
        except Exception as e:
            print(e)
            pass

    def close(self) -> bool:
        com = Relay_Serial(self.port)
        com.open()
        com.send('VOFF\n')
        return super().close()

    def showDiaglog(self):
        import serial.tools.list_ports
        ports = [p.device for p in serial.tools.list_ports.comports()]
        port, ok = QInputDialog.getItem(self, "COMPORT", "SELECT COMPORT", ports, 0, True)
        if ok:
            self.port = str(port).strip()
            config = configparser.ConfigParser()
            config.read('AppSettings.ini')
            with open('AppSettings.ini', 'w') as configfile:
                config.set('User', 'port', self.port)
                # config['User'] = {"port" : "%s"%self.port}
                config['Modified'] = {'datetime':'%s'%datetime.datetime.now()}
                config.write(configfile)
    
    def readSetting(self):
        config = configparser.ConfigParser()
        settings_file = os.path.dirname(os.path.realpath(__file__))+ os.sep + "AppSettings.ini"
        if not os.path.exists(settings_file) or os.stat(settings_file).st_size == 0:
           with open('AppSettings.ini', 'w') as configfile:
               config['DATE'] = {'Init Date':'%s'%datetime.datetime.now()}               
               config['User'] = {"port" : "COM1", "note1" : "Note1:", "note2" : "Note3:", "note3" : "Note3:", "note4" : "Note4:"}
               config['Modified'] = {'User: ':'', 'datetime':'%s'%datetime.datetime.now()}
               config.write(configfile)
        config.read('AppSettings.ini')
        try:
            self.port=config.get('User','port')
            self.ui.note1.setText(config.get('User', 'note1'))
            self.ui.note2.setText(config.get('User', 'note2'))
            self.ui.note3.setText(config.get('User', 'note3'))
            self.ui.note4.setText(config.get('User', 'note4'))
        except Exception as e:
            print(e)
        
    def Changed(self, event):
        config = configparser.ConfigParser()
        config.read('AppSettings.ini')
        with open('AppSettings.ini', 'w') as configfile:
            config['User'] = {"port" : "%s"%self.port, "note1" : "%s"%self.ui.note1.text(), "note2" : "%s"%self.ui.note2.text(), "note3" : "%s"%self.ui.note3.text(), "note4" : "%s"%self.ui.note4.text()}
            config['Modified'] = {'datetime':'%s'%datetime.datetime.now()}
            config.write(configfile)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())