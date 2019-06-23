# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AddRecordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddRecordDialog(object):
    def setupUi(self, AddRecordDialog):
        AddRecordDialog.setObjectName("AddRecordDialog")
        AddRecordDialog.resize(488, 359)
        self.gridLayout = QtWidgets.QGridLayout(AddRecordDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_description = QtWidgets.QLabel(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_description.setFont(font)
        self.lbl_description.setObjectName("lbl_description")
        self.gridLayout.addWidget(self.lbl_description, 7, 0, 1, 1)
        self.lbl_price_per_unit = QtWidgets.QLabel(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_price_per_unit.setFont(font)
        self.lbl_price_per_unit.setObjectName("lbl_price_per_unit")
        self.gridLayout.addWidget(self.lbl_price_per_unit, 6, 0, 1, 1)
        self.lbl_name_of_product = QtWidgets.QLabel(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_name_of_product.setFont(font)
        self.lbl_name_of_product.setObjectName("lbl_name_of_product")
        self.gridLayout.addWidget(self.lbl_name_of_product, 4, 0, 1, 1)
        self.line_edit_name_of_product = QtWidgets.QLineEdit(AddRecordDialog)
        self.line_edit_name_of_product.setObjectName("line_edit_name_of_product")
        self.gridLayout.addWidget(self.line_edit_name_of_product, 4, 1, 1, 2)
        self.line_edit_price_per_unit = QtWidgets.QLineEdit(AddRecordDialog)
        self.line_edit_price_per_unit.setObjectName("line_edit_price_per_unit")
        self.gridLayout.addWidget(self.line_edit_price_per_unit, 6, 1, 1, 2)
        self.radio_btn_sell = QtWidgets.QRadioButton(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_btn_sell.setFont(font)
        self.radio_btn_sell.setObjectName("radio_btn_sell")
        self.gridLayout.addWidget(self.radio_btn_sell, 1, 2, 1, 1)
        self.lbl_date = QtWidgets.QLabel(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.gridLayout.addWidget(self.lbl_date, 3, 0, 1, 1)
        self.line_edit_quantity = QtWidgets.QLineEdit(AddRecordDialog)
        self.line_edit_quantity.setObjectName("line_edit_quantity")
        self.gridLayout.addWidget(self.line_edit_quantity, 5, 1, 1, 2)
        self.btn_cancel = QtWidgets.QPushButton(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_cancel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Delete_record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 9, 3, 1, 1)
        self.radio_btn_buy = QtWidgets.QRadioButton(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_btn_buy.setFont(font)
        self.radio_btn_buy.setObjectName("radio_btn_buy")
        self.gridLayout.addWidget(self.radio_btn_buy, 1, 1, 1, 1)
        self.lbl_quantity = QtWidgets.QLabel(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_quantity.setFont(font)
        self.lbl_quantity.setObjectName("lbl_quantity")
        self.gridLayout.addWidget(self.lbl_quantity, 5, 0, 1, 1)
        self.date_edit_date = QtWidgets.QDateEdit(AddRecordDialog)
        self.date_edit_date.setCalendarPopup(True)
        self.date_edit_date.setObjectName("date_edit_date")
        self.gridLayout.addWidget(self.date_edit_date, 3, 1, 1, 2)
        self.text_edit_description = QtWidgets.QTextEdit(AddRecordDialog)
        self.text_edit_description.setObjectName("text_edit_description")
        self.gridLayout.addWidget(self.text_edit_description, 7, 1, 1, 2)
        self.btn_add = QtWidgets.QPushButton(AddRecordDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_add.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Add_record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon1)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 8, 3, 1, 1)
        self.lbl_description.setBuddy(self.text_edit_description)
        self.lbl_price_per_unit.setBuddy(self.line_edit_price_per_unit)
        self.lbl_name_of_product.setBuddy(self.line_edit_name_of_product)
        self.lbl_date.setBuddy(self.date_edit_date)
        self.lbl_quantity.setBuddy(self.line_edit_quantity)

        self.retranslateUi(AddRecordDialog)
        QtCore.QMetaObject.connectSlotsByName(AddRecordDialog)
        AddRecordDialog.setTabOrder(self.radio_btn_buy, self.radio_btn_sell)
        AddRecordDialog.setTabOrder(self.radio_btn_sell, self.date_edit_date)
        AddRecordDialog.setTabOrder(self.date_edit_date, self.line_edit_name_of_product)
        AddRecordDialog.setTabOrder(self.line_edit_name_of_product, self.line_edit_quantity)
        AddRecordDialog.setTabOrder(self.line_edit_quantity, self.line_edit_price_per_unit)
        AddRecordDialog.setTabOrder(self.line_edit_price_per_unit, self.text_edit_description)
        AddRecordDialog.setTabOrder(self.text_edit_description, self.btn_add)
        AddRecordDialog.setTabOrder(self.btn_add, self.btn_cancel)

    def retranslateUi(self, AddRecordDialog):
        _translate = QtCore.QCoreApplication.translate
        AddRecordDialog.setWindowTitle(_translate("AddRecordDialog", "Add Record"))
        self.lbl_description.setText(_translate("AddRecordDialog", "Description:"))
        self.lbl_price_per_unit.setText(_translate("AddRecordDialog", "Price per Unit:"))
        self.lbl_name_of_product.setText(_translate("AddRecordDialog", "Name of Product:"))
        self.radio_btn_sell.setText(_translate("AddRecordDialog", "Sell"))
        self.lbl_date.setText(_translate("AddRecordDialog", "Date:"))
        self.btn_cancel.setText(_translate("AddRecordDialog", "Cancel"))
        self.radio_btn_buy.setText(_translate("AddRecordDialog", "Buy"))
        self.lbl_quantity.setText(_translate("AddRecordDialog", "Quantity:"))
        self.date_edit_date.setDisplayFormat(_translate("AddRecordDialog", "dd/MM/yyyy"))
        self.btn_add.setText(_translate("AddRecordDialog", "Add"))

from icons import icons_rc
