# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 660)
        MainWindow.setMinimumSize(QSize(550, 660))
        MainWindow.setMaximumSize(QSize(550, 660))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(	255, 0, 0, 255), stop:0.427447 rgba(139, 0, 0, 125), stop:1 rgba(155, 79, 165, 255));\n"
"font-famaly: Roboto Flex;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgba(225,255,255,100);\n"
"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.RANEPA_png = QLabel(self.centralwidget)
        self.RANEPA_png.setObjectName(u"RANEPA_png")
        self.RANEPA_png.setGeometry(QRect(150, 10, 281, 151))
        self.RANEPA_png.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border: 0px solid rgba(0,0,0,0);")
        self.RANEPA_png.setPixmap(QPixmap(u":/icons/icon/\u0420\u0438\u0441\u0443\u043d\u043e\u043a1.png"))
        self.Balance_frame = QFrame(self.centralwidget)
        self.Balance_frame.setObjectName(u"Balance_frame")
        self.Balance_frame.setGeometry(QRect(180, 190, 211, 301))
        self.Balance_frame.setStyleSheet(u"background-color:rgba(255,255,255,100)")
        self.verticalLayout = QVBoxLayout(self.Balance_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Login = QLabel(self.Balance_frame)
        self.Login.setObjectName(u"Login")
        self.Login.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.Login)

        self.lineEditLog = QLineEdit(self.Balance_frame)
        self.lineEditLog.setObjectName(u"lineEditLog")

        self.verticalLayout.addWidget(self.lineEditLog)

        self.Password = QLabel(self.Balance_frame)
        self.Password.setObjectName(u"Password")
        self.Password.setEnabled(True)

        self.verticalLayout.addWidget(self.Password)

        self.lineEditPass = QLineEdit(self.Balance_frame)
        self.lineEditPass.setObjectName(u"lineEditPass")

        self.verticalLayout.addWidget(self.lineEditPass)

        self.reg_and_log = QFrame(self.Balance_frame)
        self.reg_and_log.setObjectName(u"reg_and_log")
        self.reg_and_log.setStyleSheet(u"background-color:rgba(225,255,255,0);\n"
"border: 0px  solid rgba(225,255,255,40);")
        self.horizontalLayout = QHBoxLayout(self.reg_and_log)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_login = QPushButton(self.reg_and_log)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setEnabled(True)
        self.btn_login.setMaximumSize(QSize(100, 60))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"color:black;\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/login_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_login.setIcon(icon)
        self.btn_login.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_login)

        self.btn_register = QPushButton(self.reg_and_log)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMaximumSize(QSize(400, 60))
        self.btn_register.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgba(255,255,255,40)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,60)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/key_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_register.setIcon(icon1)
        self.btn_register.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_register)


        self.verticalLayout.addWidget(self.reg_and_log)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.RANEPA_png.setText("")
        self.Login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.Password.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

