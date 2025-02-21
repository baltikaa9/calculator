# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_expression = QLineEdit(self.groupBox)
        self.lineEdit_expression.setObjectName(u"lineEdit_expression")

        self.verticalLayout_3.addWidget(self.lineEdit_expression)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit_result = QLineEdit(self.groupBox_2)
        self.lineEdit_result.setObjectName(u"lineEdit_result")
        self.lineEdit_result.setAutoFillBackground(False)
        self.lineEdit_result.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.lineEdit_result)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_multiply = QPushButton(self.widget_2)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_multiply, 2, 3, 1, 1)

        self.pushButton_plus = QPushButton(self.widget_2)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_plus, 1, 3, 1, 1)

        self.pushButton_minus = QPushButton(self.widget_2)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_minus, 3, 3, 1, 1)

        self.pushButton_devide = QPushButton(self.widget_2)
        self.pushButton_devide.setObjectName(u"pushButton_devide")
        self.pushButton_devide.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_devide, 4, 3, 1, 1)

        self.pushButton_eval = QPushButton(self.widget_2)
        self.pushButton_eval.setObjectName(u"pushButton_eval")
        self.pushButton_eval.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_eval, 5, 3, 1, 1)

        self.pushButton_point = QPushButton(self.widget_2)
        self.pushButton_point.setObjectName(u"pushButton_point")
        self.pushButton_point.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_point, 5, 2, 1, 1)

        self.pushButton_0 = QPushButton(self.widget_2)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_0, 5, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.widget_2)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_back = QPushButton(self.widget_2)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_back, 1, 2, 1, 1)

        self.pushButton_c = QPushButton(self.widget_2)
        self.pushButton_c.setObjectName(u"pushButton_c")
        self.pushButton_c.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_c, 1, 1, 1, 1)

        self.pushButton_percent = QPushButton(self.widget_2)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        self.pushButton_percent.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.pushButton_percent, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_devide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_eval.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_back.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
    # retranslateUi

