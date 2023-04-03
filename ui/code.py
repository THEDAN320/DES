# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'code.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QWidget)
import code_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 360)
        MainWindow.setMinimumSize(QSize(480, 360))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.169, y1:0.380682, x2:0.823955, y2:0.63, stop:0 rgba(0, 0, 0, 255), stop:0.587571 rgba(34, 34, 34, 255), stop:1 rgba(35, 35, 35, 255));\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane{\n"
"	border-top:2px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-radius:1em;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar{\n"
"	left:20px;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"    border: 2px solid rgb(135, 136, 127);\n"
"    border-bottom-color: rgb(135, 136, 127);\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 24ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab::selected{\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(54, 54, 54, 255), stop:1 rgba(122, 122, 122, 255));\n"
"    border: 2px solid rgb(67, 68, 63);\n"
"	border-bottom-color: rgb(67, 68, 63);\n"
"\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.encode_tab = QWidget()
        self.encode_tab.setObjectName(u"encode_tab")
        self.gridLayout_2 = QGridLayout(self.encode_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.password_edit_1 = QLineEdit(self.encode_tab)
        self.password_edit_1.setObjectName(u"password_edit_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_edit_1.sizePolicy().hasHeightForWidth())
        self.password_edit_1.setSizePolicy(sizePolicy)
        self.password_edit_1.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}")
        self.password_edit_1.setMaxLength(8)
        self.password_edit_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.password_edit_1, 0, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 4, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 4, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.encode_btn = QPushButton(self.encode_tab)
        self.encode_btn.setObjectName(u"encode_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.encode_btn.sizePolicy().hasHeightForWidth())
        self.encode_btn.setSizePolicy(sizePolicy1)
        self.encode_btn.setMaximumSize(QSize(1666666, 90))
        self.encode_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.encode_btn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, 	stop:0 rgba(41, 41, 41, 255), stop:1 rgba(124, 124, 124, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, 	 stop:0 rgba(91, 91, 91, 255), stop:1 rgba(178, 178, 178, 255));\n"
"	border-style: inset;\n"
"}")

        self.gridLayout_2.addWidget(self.encode_btn, 5, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)

        self.label = QLabel(self.encode_tab)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setPixmap(QPixmap(u":/tocode/to_code.png"))
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 3)

        self.code_output_edit = QTextEdit(self.encode_tab)
        self.code_output_edit.setObjectName(u"code_output_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.code_output_edit.sizePolicy().hasHeightForWidth())
        self.code_output_edit.setSizePolicy(sizePolicy3)
        self.code_output_edit.setStyleSheet(u"QTextEdit{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}")
        self.code_output_edit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.code_output_edit, 3, 0, 1, 5)

        self.text_input_edit = QTextEdit(self.encode_tab)
        self.text_input_edit.setObjectName(u"text_input_edit")
        sizePolicy3.setHeightForWidth(self.text_input_edit.sizePolicy().hasHeightForWidth())
        self.text_input_edit.setSizePolicy(sizePolicy3)
        self.text_input_edit.setStyleSheet(u"QTextEdit{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}")

        self.gridLayout_2.addWidget(self.text_input_edit, 0, 0, 1, 4)

        self.tabWidget.addTab(self.encode_tab, "")
        self.decode_tab = QWidget()
        self.decode_tab.setObjectName(u"decode_tab")
        self.gridLayout_3 = QGridLayout(self.decode_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.password_edit_2 = QLineEdit(self.decode_tab)
        self.password_edit_2.setObjectName(u"password_edit_2")
        sizePolicy.setHeightForWidth(self.password_edit_2.sizePolicy().hasHeightForWidth())
        self.password_edit_2.setSizePolicy(sizePolicy)
        self.password_edit_2.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}")
        self.password_edit_2.setMaxLength(8)
        self.password_edit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.password_edit_2, 0, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.text_output_edit = QTextEdit(self.decode_tab)
        self.text_output_edit.setObjectName(u"text_output_edit")
        sizePolicy3.setHeightForWidth(self.text_output_edit.sizePolicy().hasHeightForWidth())
        self.text_output_edit.setSizePolicy(sizePolicy3)
        self.text_output_edit.setMaximumSize(QSize(16777215, 16666666))
        self.text_output_edit.setBaseSize(QSize(0, 0))
        self.text_output_edit.setStyleSheet(u"QTextEdit{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}")
        self.text_output_edit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.text_output_edit, 2, 0, 1, 5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 3, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 3, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 3, 0, 1, 1)

        self.decode_btn = QPushButton(self.decode_tab)
        self.decode_btn.setObjectName(u"decode_btn")
        sizePolicy1.setHeightForWidth(self.decode_btn.sizePolicy().hasHeightForWidth())
        self.decode_btn.setSizePolicy(sizePolicy1)
        self.decode_btn.setMaximumSize(QSize(16777215, 90))
        self.decode_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.decode_btn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, 	stop:0 rgba(41, 41, 41, 255), stop:1 rgba(124, 124, 124, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, 	 stop:0 rgba(91, 91, 91, 255), stop:1 rgba(178, 178, 178, 255));\n"
"	border-style: inset;\n"
"}")

        self.gridLayout_3.addWidget(self.decode_btn, 4, 1, 1, 3)

        self.label_2 = QLabel(self.decode_tab)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setPixmap(QPixmap(u":/tocode/text.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 3)

        self.code_input_edit = QTextEdit(self.decode_tab)
        self.code_input_edit.setObjectName(u"code_input_edit")
        sizePolicy3.setHeightForWidth(self.code_input_edit.sizePolicy().hasHeightForWidth())
        self.code_input_edit.setSizePolicy(sizePolicy3)
        self.code_input_edit.setStyleSheet(u"QTextEdit{\n"
"	border: 2px solid rgb(67, 68, 63);\n"
"	border-radius: 1em;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(203, 203, 203, 255));\n"
"	border-style: outset;\n"
"}")

        self.gridLayout_3.addWidget(self.code_input_edit, 0, 0, 1, 4)

        self.tabWidget.addTab(self.decode_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.password_edit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password", None))
        self.encode_btn.setText(QCoreApplication.translate("MainWindow", u"encode text", None))
        self.label.setText("")
        self.text_input_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your message", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encode_tab), QCoreApplication.translate("MainWindow", u"encode", None))
        self.password_edit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password", None))
        self.decode_btn.setText(QCoreApplication.translate("MainWindow", u"decode text", None))
        self.label_2.setText("")
        self.code_input_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your code", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decode_tab), QCoreApplication.translate("MainWindow", u"decode", None))
    # retranslateUi

