# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Admin.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(550, 759)
        Dialog.setMinimumSize(QSize(550, 660))
        Dialog.setMaximumSize(QSize(12312312, 16777215))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(	255, 0, 0, 255), stop:0.427447 rgba(139, 0, 0, 125), stop:1 rgba(155, 79, 165, 255));\n"
"font-famaly: Roboto Flex;")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(10, 0, 531, 741))
        font = QFont()
        font.setFamilies([u"Roboto Flex"])
        font.setHintingPreference(QFont.PreferNoHinting)
        self.widget.setFont(font)
        self.widget.setTabletTracking(False)
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"background-color:rgba(225,255,255,100);\n"
"border: 1px  solid rgba(225,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTibleView{\n"
"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-botton-right-radius:7px;\n"
"border-botton-left-radius:7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color:rgba(53,53,53);\n"
"color:black;\n"
"border:none;\n"
"height:50px;\n"
"font-size:14pt;\n"
"}\n"
"QTibleView::item{\n"
"border-style:none;\n"
"border-botton:rgba(255,255,255,50);\n"
"}\n"
"QTibleVIew::item:selected{\n"
"border:none;\n"
"color:rgba(255,255,255,50);\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0440\u044b\u0439 \u0434\u0435\u043d\u044c Admin", None))
        self.pushButton_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0432\u0430\u0448 \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442 \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432 ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u041e\u0442\u0447\u0435\u0442 \u0432 \u044d\u043a\u0441\u0435\u043b\u044c", None))
    # retranslateUi

