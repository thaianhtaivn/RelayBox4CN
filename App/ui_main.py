# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 450)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Main_frame = QtWidgets.QFrame(self.centralwidget)
        self.Main_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(51, 80, 160, 255), stop:0.86828 rgba(33, 108, 194, 255));\n"
"border-radius:7px;")
        self.Main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_frame.setObjectName("Main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.Main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setMinimumSize(QtCore.QSize(0, 60))
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.title_bar.setFont(font)
        self.title_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_bar.setAutoFillBackground(False)
        self.title_bar.setStyleSheet("background-color:none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(5, 0, -1, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_logo = QtWidgets.QLabel(self.title_bar)
        self.label_logo.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_logo.setStyleSheet("image: url(\"images/icon.png\");")
        self.label_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_logo.setText("")
        self.label_logo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout.addWidget(self.label_logo)
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setStyleSheet("border:none;")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_intro = QtWidgets.QFrame(self.frame_title)
        self.frame_intro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_intro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_intro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_intro.setObjectName("frame_intro")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_intro)
        self.verticalLayout_8.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_title = QtWidgets.QLabel(self.frame_intro)
        self.label_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_8.addWidget(self.label_title)
        self.label_time = QtWidgets.QLabel(self.frame_intro)
        self.label_time.setMinimumSize(QtCore.QSize(0, 0))
        self.label_time.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.verticalLayout_8.addWidget(self.label_time)
        self.horizontalLayout_7.addWidget(self.frame_intro)
        self.rightButtons = QtWidgets.QFrame(self.frame_title)
        self.rightButtons.setMinimumSize(QtCore.QSize(0, 28))
        self.rightButtons.setMaximumSize(QtCore.QSize(130, 16777215))
        self.rightButtons.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rightButtons.setStyleSheet("/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(235, 245, 225); border-style: solid; border-radius: 4px; }")
        self.rightButtons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightButtons.setObjectName("rightButtons")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.rightButtons)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.settingsTopBtn = QtWidgets.QPushButton(self.rightButtons)
        self.settingsTopBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.settingsTopBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsTopBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QtCore.QSize(20, 20))
        self.settingsTopBtn.setObjectName("settingsTopBtn")
        self.horizontalLayout_13.addWidget(self.settingsTopBtn)
        self.minimizeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.minimizeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeAppBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon_minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.minimizeAppBtn.setObjectName("minimizeAppBtn")
        self.horizontalLayout_13.addWidget(self.minimizeAppBtn)
        self.closeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.closeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeAppBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeAppBtn.setObjectName("closeAppBtn")
        self.horizontalLayout_13.addWidget(self.closeAppBtn)
        self.horizontalLayout_7.addWidget(self.rightButtons)
        self.horizontalLayout.addWidget(self.frame_title)
        self.verticalLayout.addWidget(self.title_bar)
        self.frame = QtWidgets.QFrame(self.Main_frame)
        self.frame.setStyleSheet("background-color: none")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_CN1 = QtWidgets.QFrame(self.frame)
        self.frame_CN1.setAutoFillBackground(False)
        self.frame_CN1.setStyleSheet("background-color: rgba(255, 225, 255, 10);")
        self.frame_CN1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CN1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CN1.setObjectName("frame_CN1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_CN1)
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_CN1)
        self.frame_3.setStyleSheet("background-color: none")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title_2 = QtWidgets.QLabel(self.frame_3)
        self.label_title_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(False)
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet("QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title_2.setObjectName("label_title_2")
        self.verticalLayout_3.addWidget(self.label_title_2)
        self.note1 = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.note1.setFont(font)
        self.note1.setAutoFillBackground(False)
        self.note1.setStyleSheet("QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")
        self.note1.setInputMask("")
        self.note1.setObjectName("note1")
        self.verticalLayout_3.addWidget(self.note1)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.relay1 = QtWidgets.QCheckBox(self.frame_CN1)
        self.relay1.setMaximumSize(QtCore.QSize(120, 50))
        self.relay1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.relay1.setStyleSheet("QCheckBox {background-color: none;}\n"
"QCheckBox::indicator {width: 100px; height: 100px;}\n"
"QCheckBox::indicator:checked {image: url(\"images/on.png\");}\n"
"QCheckBox::indicator:unchecked {image: url(\"images/off.png\");}")
        self.relay1.setText("")
        self.relay1.setObjectName("relay1")
        self.horizontalLayout_2.addWidget(self.relay1)
        self.verticalLayout_7.addWidget(self.frame_CN1)
        self.frame_CN2 = QtWidgets.QFrame(self.frame)
        self.frame_CN2.setAutoFillBackground(False)
        self.frame_CN2.setStyleSheet("background-color: rgba(255, 225, 255, 10);")
        self.frame_CN2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CN2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CN2.setObjectName("frame_CN2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_CN2)
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, 10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_5 = QtWidgets.QFrame(self.frame_CN2)
        self.frame_5.setStyleSheet("background-color: none")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_title_10 = QtWidgets.QLabel(self.frame_5)
        self.label_title_10.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(False)
        self.label_title_10.setFont(font)
        self.label_title_10.setStyleSheet("QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title_10.setObjectName("label_title_10")
        self.verticalLayout_4.addWidget(self.label_title_10)
        self.note2 = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.note2.setFont(font)
        self.note2.setAutoFillBackground(False)
        self.note2.setStyleSheet("QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")
        self.note2.setInputMask("")
        self.note2.setObjectName("note2")
        self.verticalLayout_4.addWidget(self.note2)
        self.horizontalLayout_10.addWidget(self.frame_5)
        self.relay2 = QtWidgets.QCheckBox(self.frame_CN2)
        self.relay2.setMaximumSize(QtCore.QSize(120, 50))
        self.relay2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.relay2.setStyleSheet("QCheckBox {background-color: none;}\n"
"QCheckBox::indicator {width: 100px; height: 100px;}\n"
"QCheckBox::indicator:checked {image: url(\"images/on.png\");}\n"
"QCheckBox::indicator:unchecked {image: url(\"images/off.png\");}")
        self.relay2.setText("")
        self.relay2.setObjectName("relay2")
        self.horizontalLayout_10.addWidget(self.relay2)
        self.verticalLayout_7.addWidget(self.frame_CN2)
        self.frame_CN3 = QtWidgets.QFrame(self.frame)
        self.frame_CN3.setAutoFillBackground(False)
        self.frame_CN3.setStyleSheet("background-color: rgba(255, 225, 255, 10);")
        self.frame_CN3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CN3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CN3.setObjectName("frame_CN3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_CN3)
        self.horizontalLayout_12.setContentsMargins(20, 0, 20, 10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_9 = QtWidgets.QFrame(self.frame_CN3)
        self.frame_9.setStyleSheet("background-color: none")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_title_14 = QtWidgets.QLabel(self.frame_9)
        self.label_title_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(False)
        self.label_title_14.setFont(font)
        self.label_title_14.setStyleSheet("QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title_14.setObjectName("label_title_14")
        self.verticalLayout_6.addWidget(self.label_title_14)
        self.note3 = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.note3.setFont(font)
        self.note3.setAutoFillBackground(False)
        self.note3.setStyleSheet("QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")
        self.note3.setInputMask("")
        self.note3.setObjectName("note3")
        self.verticalLayout_6.addWidget(self.note3)
        self.horizontalLayout_12.addWidget(self.frame_9)
        self.relay3 = QtWidgets.QCheckBox(self.frame_CN3)
        self.relay3.setMaximumSize(QtCore.QSize(120, 50))
        self.relay3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.relay3.setStyleSheet("QCheckBox {background-color: none;}\n"
"QCheckBox::indicator {width: 100px; height: 100px;}\n"
"QCheckBox::indicator:checked {image: url(\"images/on.png\");}\n"
"QCheckBox::indicator:unchecked {image: url(\"images/off.png\");}")
        self.relay3.setText("")
        self.relay3.setObjectName("relay3")
        self.horizontalLayout_12.addWidget(self.relay3)
        self.verticalLayout_7.addWidget(self.frame_CN3)
        self.frame_CN4 = QtWidgets.QFrame(self.frame)
        self.frame_CN4.setAutoFillBackground(False)
        self.frame_CN4.setStyleSheet("background-color: rgba(255, 225, 255, 10);")
        self.frame_CN4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CN4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CN4.setObjectName("frame_CN4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_CN4)
        self.horizontalLayout_11.setContentsMargins(20, 0, 20, 10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_7 = QtWidgets.QFrame(self.frame_CN4)
        self.frame_7.setStyleSheet("background-color: none")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_title_12 = QtWidgets.QLabel(self.frame_7)
        self.label_title_12.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(False)
        self.label_title_12.setFont(font)
        self.label_title_12.setStyleSheet("QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title_12.setObjectName("label_title_12")
        self.verticalLayout_5.addWidget(self.label_title_12)
        self.note4 = QtWidgets.QLineEdit(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setKerning(True)
        self.note4.setFont(font)
        self.note4.setAutoFillBackground(False)
        self.note4.setStyleSheet("QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")
        self.note4.setInputMask("")
        self.note4.setObjectName("note4")
        self.verticalLayout_5.addWidget(self.note4)
        self.horizontalLayout_11.addWidget(self.frame_7)
        self.relay4 = QtWidgets.QCheckBox(self.frame_CN4)
        self.relay4.setMaximumSize(QtCore.QSize(120, 50))
        self.relay4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.relay4.setStyleSheet("QCheckBox {background-color: none;}\n"
"QCheckBox::indicator {width: 100px; height: 100px;}\n"
"QCheckBox::indicator:checked {image: url(\"images/on.png\");}\n"
"QCheckBox::indicator:unchecked {image: url(\"images/off.png\");}")
        self.relay4.setText("")
        self.relay4.setObjectName("relay4")
        self.horizontalLayout_11.addWidget(self.relay4)
        self.verticalLayout_7.addWidget(self.frame_CN4)
        self.frame_credit = QtWidgets.QFrame(self.frame)
        self.frame_credit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_credit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_credit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_credit.setObjectName("frame_credit")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_credit)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_credit)
        self.label.setStyleSheet("color: rgb(255,54,18);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_credit = QtWidgets.QLabel(self.frame_credit)
        self.label_credit.setMinimumSize(QtCore.QSize(0, 0))
        self.label_credit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        self.label_credit.setFont(font)
        self.label_credit.setStyleSheet("color: rgba(7, 0, 86, 120);")
        self.label_credit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credit.setObjectName("label_credit")
        self.horizontalLayout_3.addWidget(self.label_credit)
        self.verticalLayout_7.addWidget(self.frame_credit)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.Main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "RELAY BOX 4 CHANNELS"))
        self.label_time.setText(_translate("MainWindow", "TIME"))
        self.settingsTopBtn.setToolTip(_translate("MainWindow", "Settings"))
        self.minimizeAppBtn.setToolTip(_translate("MainWindow", "Minimize"))
        self.closeAppBtn.setToolTip(_translate("MainWindow", "Close"))
        self.label_title_2.setText(_translate("MainWindow", "Channel 1:"))
        self.note1.setText(_translate("MainWindow", "Note 1:"))
        self.label_title_10.setText(_translate("MainWindow", "Channel 2:"))
        self.note2.setText(_translate("MainWindow", "Note 2:"))
        self.label_title_14.setText(_translate("MainWindow", "Channel 3:"))
        self.note3.setText(_translate("MainWindow", "Note 3:"))
        self.label_title_12.setText(_translate("MainWindow", "Channel 4:"))
        self.note4.setText(_translate("MainWindow", "Note 4:"))
        self.label_credit.setText(_translate("MainWindow", "#v21.01  #tht5hc "))
