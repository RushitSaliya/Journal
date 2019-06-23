# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SignInDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignInDialog(object):
    def setupUi(self, SignInDialog):
        SignInDialog.setObjectName("SignInDialog")
        SignInDialog.resize(326, 357)
        self.gridLayout = QtWidgets.QGridLayout(SignInDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_password = QtWidgets.QLabel(SignInDialog)
        self.lbl_password.setObjectName("lbl_password")
        self.gridLayout.addWidget(self.lbl_password, 5, 0, 1, 1)
        self.lbl_username = QtWidgets.QLabel(SignInDialog)
        self.lbl_username.setObjectName("lbl_username")
        self.gridLayout.addWidget(self.lbl_username, 2, 0, 1, 1)
        self.line_edit_password = QtWidgets.QLineEdit(SignInDialog)
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.gridLayout.addWidget(self.line_edit_password, 5, 1, 1, 1)
        self.line_edit_username = QtWidgets.QLineEdit(SignInDialog)
        self.line_edit_username.setObjectName("line_edit_username")
        self.gridLayout.addWidget(self.line_edit_username, 2, 1, 1, 1)
        self.btn_Sign_in = QtWidgets.QPushButton(SignInDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_Sign_in.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sign_in.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Sign_in.setIcon(icon)
        self.btn_Sign_in.setObjectName("btn_Sign_in")
        self.gridLayout.addWidget(self.btn_Sign_in, 7, 1, 1, 1)
        self.lbl_login = QtWidgets.QLabel(SignInDialog)
        self.lbl_login.setObjectName("lbl_login")
        self.gridLayout.addWidget(self.lbl_login, 1, 1, 1, 1)
        self.lbl_password.setBuddy(self.line_edit_password)
        self.lbl_username.setBuddy(self.line_edit_username)

        self.retranslateUi(SignInDialog)
        QtCore.QMetaObject.connectSlotsByName(SignInDialog)
        SignInDialog.setTabOrder(self.line_edit_username, self.line_edit_password)

    def retranslateUi(self, SignInDialog):
        _translate = QtCore.QCoreApplication.translate
        SignInDialog.setWindowTitle(_translate("SignInDialog", "Sign in"))
        self.lbl_password.setText(_translate("SignInDialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Password:</span></p></body></html>"))
        self.lbl_username.setText(_translate("SignInDialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Username:</span></p></body></html>"))
        self.btn_Sign_in.setText(_translate("SignInDialog", "Sign in"))
        self.lbl_login.setText(_translate("SignInDialog", "<html><head/><body><p><span style=\" font-size:24pt;\">Sign in</span></p></body></html>"))

from icons import icons_rc
