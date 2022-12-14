# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'date.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import datetime
from PyQt5.QtWidgets import QMessageBox
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(212, 143)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(20, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color: rgb(49, 99, 148);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Office")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 99, 148);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Choose Date"))
        self.dateEdit.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
        self.label.setText(_translate("Form", "Choose Date"))
        self.pushButton.setText(_translate("Form", "Check Attendance"))
        
        self.pushButton.clicked.connect(self.call)
        self.pushButton.clicked.connect(Form.close)


    def call(self):
        e=self.dateEdit.date()
        b=e.toPyDate()
        try:
            from dt import date
            date(str(b))
        except:
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Invalid Date Selected or No Records Found")
                msgBox.setWindowTitle("Warning")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
            except Exception as e:
                print(e)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
