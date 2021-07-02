# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 450)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.Main_frame = QFrame(self.centralwidget)
        self.Main_frame.setObjectName(u"Main_frame")
        self.Main_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(51, 80, 160, 255), stop:0.86828 rgba(33, 108, 194, 255));\n"
"border-radius:7px;")
        self.Main_frame.setFrameShape(QFrame.NoFrame)
        self.Main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.Main_frame)
        self.title_bar.setObjectName(u"title_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setMinimumSize(QSize(0, 60))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setBold(True)
        self.title_bar.setFont(font)
        self.title_bar.setLayoutDirection(Qt.LeftToRight)
        self.title_bar.setAutoFillBackground(False)
        self.title_bar.setStyleSheet(u"background-color:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setStyleSheet(u"border:none;")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 9, -1, -1)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_title)

        self.label_time = QLabel(self.frame_title)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(0, 0))
        self.label_time.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setFamily(u"Microsoft JhengHei")
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_time.setFont(font2)
        self.label_time.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_time)

        self.rightButtons = QFrame(self.frame_title)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setMaximumSize(QSize(130, 16777215))
        self.rightButtons.setLayoutDirection(Qt.LeftToRight)
        self.rightButtons.setStyleSheet(u"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(235, 245, 225); border-style: solid; border-radius: 4px; }")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.closeAppBtn)


        self.horizontalLayout_7.addWidget(self.rightButtons)


        self.horizontalLayout.addWidget(self.frame_title)


        self.verticalLayout.addWidget(self.title_bar)

        self.frame = QFrame(self.Main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_CN1 = QFrame(self.frame)
        self.frame_CN1.setObjectName(u"frame_CN1")
        self.frame_CN1.setAutoFillBackground(False)
        self.frame_CN1.setStyleSheet(u"background-color: rgba(255, 225, 255, 10);")
        self.frame_CN1.setFrameShape(QFrame.StyledPanel)
        self.frame_CN1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_CN1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 10)
        self.frame_3 = QFrame(self.frame_CN1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_title_2 = QLabel(self.frame_3)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Verdana")
        font3.setPointSize(14)
        font3.setBold(False)
        self.label_title_2.setFont(font3)
        self.label_title_2.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_title_2)

        self.note1 = QLineEdit(self.frame_3)
        self.note1.setObjectName(u"note1")
        font4 = QFont()
        font4.setFamily(u"Verdana")
        font4.setPointSize(14)
        self.note1.setFont(font4)
        self.note1.setAutoFillBackground(False)
        self.note1.setStyleSheet(u"QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")

        self.verticalLayout_3.addWidget(self.note1)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.relay1 = QCheckBox(self.frame_CN1)
        self.relay1.setObjectName(u"relay1")
        self.relay1.setMaximumSize(QSize(120, 50))
        self.relay1.setLayoutDirection(Qt.RightToLeft)
        self.relay1.setStyleSheet(u"QCheckBox{\n"
"background-color: none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	width: 100px;\n"
"	height: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(\"on.png\");\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	image: url(\"off.png\");\n"
"}")

        self.horizontalLayout_2.addWidget(self.relay1)


        self.verticalLayout_7.addWidget(self.frame_CN1)

        self.frame_CN2 = QFrame(self.frame)
        self.frame_CN2.setObjectName(u"frame_CN2")
        self.frame_CN2.setAutoFillBackground(False)
        self.frame_CN2.setStyleSheet(u"background-color: rgba(255, 225, 255, 10);")
        self.frame_CN2.setFrameShape(QFrame.StyledPanel)
        self.frame_CN2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_CN2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, 10)
        self.frame_5 = QFrame(self.frame_CN2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: none")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_title_10 = QLabel(self.frame_5)
        self.label_title_10.setObjectName(u"label_title_10")
        self.label_title_10.setMinimumSize(QSize(0, 0))
        self.label_title_10.setFont(font3)
        self.label_title_10.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_title_10)

        self.note2 = QLineEdit(self.frame_5)
        self.note2.setObjectName(u"note2")
        self.note2.setFont(font4)
        self.note2.setAutoFillBackground(False)
        self.note2.setStyleSheet(u"QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")

        self.verticalLayout_4.addWidget(self.note2)


        self.horizontalLayout_10.addWidget(self.frame_5)

        self.relay2 = QCheckBox(self.frame_CN2)
        self.relay2.setObjectName(u"relay2")
        self.relay2.setMaximumSize(QSize(120, 50))
        self.relay2.setLayoutDirection(Qt.RightToLeft)
        self.relay2.setStyleSheet(u"QCheckBox{\n"
"background-color: none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	width: 100px;\n"
"	height: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(\"on.png\");\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	image: url(\"off.png\");\n"
"}")

        self.horizontalLayout_10.addWidget(self.relay2)


        self.verticalLayout_7.addWidget(self.frame_CN2)

        self.frame_CN3 = QFrame(self.frame)
        self.frame_CN3.setObjectName(u"frame_CN3")
        self.frame_CN3.setAutoFillBackground(False)
        self.frame_CN3.setStyleSheet(u"background-color: rgba(255, 225, 255, 10);")
        self.frame_CN3.setFrameShape(QFrame.StyledPanel)
        self.frame_CN3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_CN3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 0, 20, 10)
        self.frame_9 = QFrame(self.frame_CN3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: none")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_title_14 = QLabel(self.frame_9)
        self.label_title_14.setObjectName(u"label_title_14")
        self.label_title_14.setMinimumSize(QSize(0, 0))
        self.label_title_14.setFont(font3)
        self.label_title_14.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_title_14)

        self.note3 = QLineEdit(self.frame_9)
        self.note3.setObjectName(u"note3")
        self.note3.setFont(font4)
        self.note3.setAutoFillBackground(False)
        self.note3.setStyleSheet(u"QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")

        self.verticalLayout_6.addWidget(self.note3)


        self.horizontalLayout_12.addWidget(self.frame_9)

        self.relay3 = QCheckBox(self.frame_CN3)
        self.relay3.setObjectName(u"relay3")
        self.relay3.setMaximumSize(QSize(120, 50))
        self.relay3.setLayoutDirection(Qt.RightToLeft)
        self.relay3.setStyleSheet(u"QCheckBox{\n"
"background-color: none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	width: 100px;\n"
"	height: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(\"on.png\");\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	image: url(\"off.png\");\n"
"}")

        self.horizontalLayout_12.addWidget(self.relay3)


        self.verticalLayout_7.addWidget(self.frame_CN3)

        self.frame_CN4 = QFrame(self.frame)
        self.frame_CN4.setObjectName(u"frame_CN4")
        self.frame_CN4.setAutoFillBackground(False)
        self.frame_CN4.setStyleSheet(u"background-color: rgba(255, 225, 255, 10);")
        self.frame_CN4.setFrameShape(QFrame.StyledPanel)
        self.frame_CN4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_CN4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, 0, 20, 10)
        self.frame_7 = QFrame(self.frame_CN4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: none")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_title_12 = QLabel(self.frame_7)
        self.label_title_12.setObjectName(u"label_title_12")
        self.label_title_12.setMinimumSize(QSize(0, 0))
        self.label_title_12.setFont(font3)
        self.label_title_12.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_title_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_title_12)

        self.note4 = QLineEdit(self.frame_7)
        self.note4.setObjectName(u"note4")
        self.note4.setFont(font4)
        self.note4.setAutoFillBackground(False)
        self.note4.setStyleSheet(u"QLineEdit{\n"
"color: rgb(8, 255, 206);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}")

        self.verticalLayout_5.addWidget(self.note4)


        self.horizontalLayout_11.addWidget(self.frame_7)

        self.relay4 = QCheckBox(self.frame_CN4)
        self.relay4.setObjectName(u"relay4")
        self.relay4.setMaximumSize(QSize(120, 50))
        self.relay4.setLayoutDirection(Qt.RightToLeft)
        self.relay4.setStyleSheet(u"QCheckBox{\n"
"background-color: none;\n"
"}\n"
"QCheckBox::indicator{\n"
"	width: 100px;\n"
"	height: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(\"on.png\");\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"	image: url(\"off.png\");\n"
"}")

        self.horizontalLayout_11.addWidget(self.relay4)


        self.verticalLayout_7.addWidget(self.frame_CN4)

        self.frame_credit = QFrame(self.frame)
        self.frame_credit.setObjectName(u"frame_credit")
        self.frame_credit.setMaximumSize(QSize(16777215, 20))
        self.frame_credit.setFrameShape(QFrame.StyledPanel)
        self.frame_credit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_credit)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_credit = QLabel(self.frame_credit)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setItalic(True)
        self.label_credit.setFont(font5)
        self.label_credit.setStyleSheet(u"color: rgba(7, 0, 86, 120);")
        self.label_credit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credit.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_credit)


        self.verticalLayout_7.addWidget(self.frame_credit)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.Main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"RELAY BOX 4 CHANNELS", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TIME", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"Channel 1:", None))
        self.note1.setInputMask("")
        self.note1.setText(QCoreApplication.translate("MainWindow", u"Note 1:", None))
        self.relay1.setText("")
        self.label_title_10.setText(QCoreApplication.translate("MainWindow", u"Channel 2:", None))
        self.note2.setInputMask("")
        self.note2.setText(QCoreApplication.translate("MainWindow", u"Note 2:", None))
        self.relay2.setText("")
        self.label_title_14.setText(QCoreApplication.translate("MainWindow", u"Channel 3:", None))
        self.note3.setInputMask("")
        self.note3.setText(QCoreApplication.translate("MainWindow", u"Note 3:", None))
        self.relay3.setText("")
        self.label_title_12.setText(QCoreApplication.translate("MainWindow", u"Channel 4:", None))
        self.note4.setInputMask("")
        self.note4.setText(QCoreApplication.translate("MainWindow", u"Note 4:", None))
        self.relay4.setText("")
        self.label_credit.setText(QCoreApplication.translate("MainWindow", u"#v21.01  #tht5hc  ", None))
    # retranslateUi

