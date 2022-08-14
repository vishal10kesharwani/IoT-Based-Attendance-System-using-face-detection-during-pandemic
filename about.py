# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutus.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1457, 775)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 20, 881, 71))
        font = QtGui.QFont()
        font.setFamily("Office")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:30px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 1061, 101))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(980, 210, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Office")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0.0199005 rgba(234, 11, 11, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.079602 rgba(239, 236, 55, 255), stop:0.208955 rgba(244, 70, 5, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.86 rgba(255, 136, 0, 255));\n"
"background-color: rgb(235, 235, 235);\n"
"border-radius:10")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(980, 410, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Office")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(221, 0, 110);\n"
"background-color: rgb(235, 235, 235);\n"
"border-radius:10")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(980, 360, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Office")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(204, 68, 0);\n"
"background-color: rgb(235, 235, 235);\n"
"border-radius:10")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(980, 310, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Office")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(85, 0, 255);\n"
"background-color: rgb(235, 235, 235);\n"
"border-radius:10")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(980, 260, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Office")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(69, 138, 207);\n"
"background-color: rgb(235, 235, 235);\n"
"border-radius:10")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(50, 210, 911, 491))
        self.graphicsView.setStyleSheet("border-image: url(:/QLabel/group.png);\n"
"border-radius:30")
        self.graphicsView.setObjectName("graphicsView")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(1090, 460, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(990, 620, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(1060, 500, 221, 131))
        self.graphicsView_2.setStyleSheet("border-image: url(:/QLabel/logo.png);")
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About US"))
        self.label.setText(_translate("Form", "IoT Based Attendance System Using Face Detection"))
        self.label_2.setText(_translate("Form", "This IoT Based Project Is Created By Students of Government Polytechnic, Gondia              under Computer Engineering department, Capstone Project Planning & Execution Subject followed by the students below:"))
        self.label_3.setText(_translate("Form", "Vishal S Kesharwani [CO6I]"))
        self.label_4.setText(_translate("Form", "Pankaj K Maudekar [CO6I]"))
        self.label_5.setText(_translate("Form", "Kunal T Harinkhede [CO6I]"))
        self.label_6.setText(_translate("Form", "Shardaprasad S Kawle [CO6I]"))
        self.label_7.setText(_translate("Form", "Oditya A Katre [CO6I]"))
        self.label_8.setText(_translate("Form", "Under The Guidance Of"))
        self.label_9.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#00aaff;\">   Mr. P S Thakre Sir</span><span style=\" font-weight:600; color:#00aaff;\">     </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#3e7cba;\">Lecturer, Computer Engg. Dept</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#5500ff;\">Governement Polytechnic, Gondia</span></p></body></html>"))
import service


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())