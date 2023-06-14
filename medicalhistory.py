# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medicalhistory.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(1100, 600))
        MainWindow.setBaseSize(QtCore.QSize(1100, 600))
        MainWindow.setStyleSheet("/* Стили для фона */\n"
"QFrame#backgroundFrame {\n"
"    background-color: #f1f1f1;\n"
"}\n"
"font-family: \"Roboto\", Arial, sans-serif;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 230, 1051, 341))
        self.tableWidget.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Dell = QtWidgets.QPushButton(self.centralwidget)
        self.Dell.setGeometry(QtCore.QRect(20, 10, 121, 41))
        self.Dell.setStyleSheet("/* Стили для обычной кнопки */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для кнопки при наведении */\n"
"QPushButton:hover {\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"/* Стили для кнопки при нажатии */\n"
"QPushButton:pressed {\n"
"    background-color: #1f2b36;\n"
"}\n"
"")
        self.Dell.setObjectName("Dell")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(20, 60, 121, 41))
        self.Add.setStyleSheet("/* Стили для обычной кнопки */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для кнопки при наведении */\n"
"QPushButton:hover {\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"/* Стили для кнопки при нажатии */\n"
"QPushButton:pressed {\n"
"    background-color: #1f2b36;\n"
"}\n"
"")
        self.Add.setObjectName("Add")
        self.Change = QtWidgets.QPushButton(self.centralwidget)
        self.Change.setGeometry(QtCore.QRect(20, 110, 121, 41))
        self.Change.setStyleSheet("/* Стили для обычной кнопки */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для кнопки при наведении */\n"
"QPushButton:hover {\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"/* Стили для кнопки при нажатии */\n"
"QPushButton:pressed {\n"
"    background-color: #1f2b36;\n"
"}\n"
"")
        self.Change.setObjectName("Change")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(20, 160, 121, 41))
        self.Open.setStyleSheet("/* Стили для обычной кнопки */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для кнопки при наведении */\n"
"QPushButton:hover {\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"/* Стили для кнопки при нажатии */\n"
"QPushButton:pressed {\n"
"    background-color: #1f2b36;\n"
"}\n"
"")
        self.Open.setObjectName("Open")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(960, 0, 141, 51))
        self.Back.setStyleSheet("/* Стили для обычной кнопки */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для кнопки при наведении */\n"
"QPushButton:hover {\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"/* Стили для кнопки при нажатии */\n"
"QPushButton:pressed {\n"
"    background-color: #1f2b36;\n"
"}\n"
"")
        self.Back.setObjectName("Back")
        self.DellLine = QtWidgets.QLineEdit(self.centralwidget)
        self.DellLine.setGeometry(QtCore.QRect(150, 10, 101, 41))
        self.DellLine.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.DellLine.setText("")
        self.DellLine.setObjectName("DellLine")
        self.AddLine = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine.setGeometry(QtCore.QRect(150, 60, 101, 41))
        self.AddLine.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.AddLine.setObjectName("AddLine")
        self.AddLine_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_1.setGeometry(QtCore.QRect(260, 60, 101, 41))
        self.AddLine_1.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.AddLine_1.setObjectName("AddLine_1")
        self.AddLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_2.setGeometry(QtCore.QRect(370, 60, 101, 41))
        self.AddLine_2.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.AddLine_2.setObjectName("AddLine_2")
        self.AddLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_3.setGeometry(QtCore.QRect(480, 60, 101, 41))
        self.AddLine_3.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.AddLine_3.setObjectName("AddLine_3")
        self.ChangeLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_4.setGeometry(QtCore.QRect(590, 110, 101, 41))
        self.ChangeLine_4.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.ChangeLine_4.setObjectName("ChangeLine_4")
        self.ChangeLine_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_1.setGeometry(QtCore.QRect(260, 110, 101, 41))
        self.ChangeLine_1.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.ChangeLine_1.setObjectName("ChangeLine_1")
        self.ChangeLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_2.setGeometry(QtCore.QRect(370, 110, 101, 41))
        self.ChangeLine_2.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.ChangeLine_2.setObjectName("ChangeLine_2")
        self.ChangeLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_3.setGeometry(QtCore.QRect(480, 110, 101, 41))
        self.ChangeLine_3.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.ChangeLine_3.setObjectName("ChangeLine_3")
        self.ChangeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine.setGeometry(QtCore.QRect(150, 110, 101, 41))
        self.ChangeLine.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.ChangeLine.setObjectName("ChangeLine")
        self.AddLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_4.setGeometry(QtCore.QRect(590, 60, 101, 41))
        self.AddLine_4.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.AddLine_4.setObjectName("AddLine_4")
        self.AddLine_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_5.setGeometry(QtCore.QRect(700, 60, 101, 41))
        self.AddLine_5.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.AddLine_5.setObjectName("AddLine_5")
        self.ChangeLine_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_5.setGeometry(QtCore.QRect(700, 110, 101, 41))
        self.ChangeLine_5.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.ChangeLine_5.setObjectName("ChangeLine_5")
        self.ChangeLine_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_6.setGeometry(QtCore.QRect(810, 110, 101, 41))
        self.ChangeLine_6.setStyleSheet("/* Стили для поля ввода */\n"
"QLineEdit {\n"
"    border: 2px solid #2c3e50;\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* Стили для поля ввода при получении фокуса */\n"
"QLineEdit:focus {\n"
"    border-color: #34495e;\n"
"}\n"
"")
        self.ChangeLine_6.setObjectName("ChangeLine_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "drivers"))
        self.Dell.setText(_translate("MainWindow", "Удалить"))
        self.Add.setText(_translate("MainWindow", "Добавить"))
        self.Change.setText(_translate("MainWindow", "Изменить"))
        self.Open.setText(_translate("MainWindow", "Открыть"))
        self.Back.setText(_translate("MainWindow", "Назад"))
