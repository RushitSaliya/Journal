# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DeleteRecordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteRecordDialog(object):
    def setupUi(self, DeleteRecordDialog):
        DeleteRecordDialog.setObjectName("DeleteRecordDialog")
        DeleteRecordDialog.resize(208, 98)
        self.gridLayout = QtWidgets.QGridLayout(DeleteRecordDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line_edit_index = QtWidgets.QLineEdit(DeleteRecordDialog)
        self.line_edit_index.setObjectName("line_edit_index")
        self.gridLayout.addWidget(self.line_edit_index, 0, 1, 1, 1)
        self.lbl_index = QtWidgets.QLabel(DeleteRecordDialog)
        self.lbl_index.setObjectName("lbl_index")
        self.gridLayout.addWidget(self.lbl_index, 0, 0, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(DeleteRecordDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Delete_record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 2, 1, 1, 1)

        self.retranslateUi(DeleteRecordDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteRecordDialog)

    def retranslateUi(self, DeleteRecordDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteRecordDialog.setWindowTitle(_translate("DeleteRecordDialog", "Delete Record"))
        self.lbl_index.setText(_translate("DeleteRecordDialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Index:</span></p></body></html>"))
        self.btn_delete.setText(_translate("DeleteRecordDialog", "Delete"))

from icons import icons_rc
