import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)

import Main_Window
import doctors
import blezni
import login
import patients
import medicalhistory
import reg
import os

current_dir = os.getcwd()

filename = "nadya.db"
filepath = os.path.join(current_dir, filename)


class Expample(QtWidgets.QMainWindow, Main_Window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

class Registration(QtWidgets.QMainWindow, reg.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.register)

        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()

    def register(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username and password:
    
            query = "SELECT COUNT(*) AS count FROM users WHERE username = ?;"
            self.cursor.execute(query, (username,))
            result = self.cursor.fetchone()
            count = result[0]

            if count == 0:

                insert_query = "INSERT INTO users (username, password) VALUES (?, ?);"
                self.cursor.execute(insert_query, (username, password))
                self.connection.commit()

                QtWidgets.QMessageBox.information(self, "Успех", "Регистрация успешно выполнена.")
                self.close()
            else:
                QtWidgets.QMessageBox.warning(self, "Ошибка", "Пользователь с таким именем уже существует.")
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")




class Login(QtWidgets.QMainWindow, login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login1)
        self.pushButton_2.clicked.connect(self.register)


        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()

    def login1(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()


        query = "SELECT COUNT(*) AS count FROM users WHERE username = ? AND password = ?;"
        self.cursor.execute(query, (login, password))
        result = self.cursor.fetchone()
        count = result[0]

        if count == 1:
            self.example = MainWindow()
            self.example.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неправильный логин или пароль")

    def register(self):
        self.registration_window = Registration()
        self.registration_window.show()




class Accidents(QtWidgets.QMainWindow,doctors.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellAccidents)
        self.Add.clicked.connect(self.AddAccidents)
        
        self.Change.clicked.connect(self.ChangeAccidents)

    def test(self):

        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Doctors'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellAccidents(self):
           
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Doctors' WHERE DoctorID = ?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Doctors'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def AddAccidents(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Doctors' (Lastname,Firstname,Specialization) VALUES(?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),))
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Doctors'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()


    def ChangeAccidents(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Doctors' SET Lastname='{self.ChangeLine_1.text()}', Firstname='{self.ChangeLine_2.text()}', Specialization='{self.ChangeLine_3.text()}' WHERE DoctorID='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Doctors'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

class Drivers(QtWidgets.QMainWindow,patients.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellDrivers)
        self.Add.clicked.connect(self.AddDrivers)

        self.Change.clicked.connect(self.ChangeDrivers)
        
        
    
    def test(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Patients'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellDrivers(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Patients' WHERE PatientID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Patients'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    def AddDrivers(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Patients' ('Lastname', 'Firstname', 'MiddleName', 'Gender', 'DateOfBirth',Address,PhoneNumber) VALUES (?, ?, ?, ?, ?,?,?)",
                       (self.AddLine.text(), self.AddLine_1.text(), self.AddLine_2.text(), self.AddLine_3.text(), self.AddLine_4.text(),self.AddLine_5.text(),self.AddLine_6.text()))
                           
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Patients'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()


    def ChangeDrivers(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Patients' SET Lastname='{self.ChangeLine_1.text()}', Firstname='{self.ChangeLine_2.text()}', MiddleName='{self.ChangeLine_3.text()}', Gender='{self.ChangeLine_4.text()}', DateOfBirth='{self.ChangeLine_5.text()}', Address='{self.ChangeLine_6.text()}', PhoneNumber={self.ChangeLine_7.text()} WHERE PatientID='{self.ChangeLine.text()}'")
        
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Patients'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

class Fuel(QtWidgets.QMainWindow,medicalhistory.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellFuel)
        self.Add.clicked.connect(self.AddFuel)

        self.Change.clicked.connect(self.ChangeFuel)
        

    def test(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'MedicalHistory'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellFuel(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'MedicalHistory' WHERE RecordID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'MedicalHistory'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def AddFuel(self):

        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'MedicalHistory' (PatientID,AdmissionDate,DischargeDate,Diagnosis,Treatment,DoctorInfo) VALUES(?,?,?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),self.AddLine_5.text()))
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'MedicalHistory'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()


    def ChangeFuel(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'MedicalHistory' SET PatientID='{self.ChangeLine_1.text()}', AdmissionDate='{self.ChangeLine_2.text()}', DischargeDate='{self.ChangeLine_3.text()}', Diagnosis='{self.ChangeLine_4.text()}', Treatment='{self.ChangeLine_5.text()}', DoctorInfo='{self.ChangeLine_5.text()}' WHERE RecordID='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'MedicalHistory'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()


class Inspection(QtWidgets.QMainWindow,blezni.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Dell.clicked.connect(self.DellInspection)
        self.Add.clicked.connect(self.AddInspection)
        self.Change.clicked.connect(self.ChangeInspection)


    def test1(self):
        
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Diagnoses'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellInspection(self):
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Diagnoses' WHERE DiagnosisID =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Diagnoses'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()


    def AddInspection(self):

        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Diagnoses' (Name) VALUES(?)", (self.AddLine.text(),))
        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Diagnoses'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeInspection(self):
        
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Diagnoses' SET Name='{self.ChangeLine_1.text()}' WHERE DiagnosisID='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()
        self.connection = sqlite3.connect(filepath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Diagnoses'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()






class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Expample()
        self.accidents = Accidents()
        self.drivers = Drivers()
        self.fuel = Fuel()
        self.inspection = Inspection()

        
        

        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.accidents)
        self.stacked_widget.addWidget(self.drivers)
        self.stacked_widget.addWidget(self.fuel)
        self.stacked_widget.addWidget(self.inspection)

        
    

        self.example.AccidentsBtn.clicked.connect(self.show_accidents)
        self.accidents.Back.clicked.connect(self.show_example)
        self.example.DriversBtn.clicked.connect(self.show_drivers)
        self.drivers.Back.clicked.connect(self.show_example)
        self.example.FuelBtn.clicked.connect(self.show_fuel)
        self.fuel.Back.clicked.connect(self.show_example)
        self.example.InspectionsBtn.clicked.connect(self.show_inspection)
        self.inspection.Back.clicked.connect(self.show_example)

        
        
        

    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)

    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    def show_drivers(self):
        self.stacked_widget.setCurrentWidget(self.drivers)
    
    def show_fuel(self):
        self.stacked_widget.setCurrentWidget(self.fuel)

    def show_inspection(self):
        self.stacked_widget.setCurrentWidget(self.inspection)
    




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())