from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Add button                                                                                                     
        self.btn = QPushButton('Show Input Dialog', self)
        self.btn.move(30, 20)
        self.btn.clicked.connect(self.showDialog)

	# Add label                                                                                                      
        self.le = QLabel(self)
        self.le.move(30, 62)
        self.le.resize(400,22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog 123')
        self.show()


    def showDialog(self, port):
        items = ('port','COM1')
		
        item, ok = QInputDialog.getItem(self, "SELECT COMPORT", "COM", items, 0, False)
        if ok:
                self.le.setText(str(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())