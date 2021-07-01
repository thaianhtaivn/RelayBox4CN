# Application for controlling Relay box 4 channel
# THT5HC

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import datetime
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
        from serial.tools.list_ports import comports
        ports = [p.name for p in comports()]
        port, ok = QInputDialog.getItem(self, "SELECT COMPORT", "COM", ports, 0, False)
        if ok:
                self.port = str(port).strip()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())