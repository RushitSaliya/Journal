# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\EstimationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EstimationWindow(object):
    def setupUi(self, EstimationWindow):
        EstimationWindow.setObjectName("EstimationWindow")
        EstimationWindow.resize(710, 484)
        self.centralwidget = QtWidgets.QWidget(EstimationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_items = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_items.setObjectName("lineEdit_items")
        self.gridLayout.addWidget(self.lineEdit_items, 2, 10, 1, 1)
        self.lbl_items = QtWidgets.QLabel(self.centralwidget)
        self.lbl_items.setObjectName("lbl_items")
        self.gridLayout.addWidget(self.lbl_items, 2, 1, 1, 1)
        self.comboBox_enteredItems = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_enteredItems.setObjectName("comboBox_enteredItems")
        self.gridLayout.addWidget(self.comboBox_enteredItems, 3, 10, 1, 1)
        self.radioButton_all = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_all.setFont(font)
        self.radioButton_all.setChecked(True)
        self.radioButton_all.setObjectName("radioButton_all")
        self.gridLayout.addWidget(self.radioButton_all, 2, 4, 1, 1)
        self.radioButton_manual = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_manual.setFont(font)
        self.radioButton_manual.setObjectName("radioButton_manual")
        self.gridLayout.addWidget(self.radioButton_manual, 2, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 1, 1, 1)
        self.btn_removeItem = QtWidgets.QPushButton(self.centralwidget)
        self.btn_removeItem.setObjectName("btn_removeItem")
        self.gridLayout.addWidget(self.btn_removeItem, 3, 12, 1, 1)
        self.btn_enterItem = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enterItem.setObjectName("btn_enterItem")
        self.gridLayout.addWidget(self.btn_enterItem, 2, 12, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 7, 1, 1)
        self.comboBox_duration = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_duration.setObjectName("comboBox_duration")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.gridLayout.addWidget(self.comboBox_duration, 1, 3, 1, 5)
        self.btn_predictProfit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_predictProfit.setObjectName("btn_predictProfit")
        self.gridLayout.addWidget(self.btn_predictProfit, 4, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 8, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.lbl_duration = QtWidgets.QLabel(self.centralwidget)
        self.lbl_duration.setObjectName("lbl_duration")
        self.gridLayout.addWidget(self.lbl_duration, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 8, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 10, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 12, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 3, 1, 2, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 11, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 2, 1, 1)
        self.lbl_itemName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_itemName.setFont(font)
        self.lbl_itemName.setObjectName("lbl_itemName")
        self.gridLayout.addWidget(self.lbl_itemName, 2, 9, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 1, 13, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 10, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 1, 12, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 7, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 6, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 5, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 502, 311))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 5, 2, 8, 10)
        EstimationWindow.setCentralWidget(self.centralwidget)
        self.lbl_items.setBuddy(self.radioButton_all)
        self.lbl_duration.setBuddy(self.comboBox_duration)

        self.retranslateUi(EstimationWindow)
        self.radioButton_all.clicked['bool'].connect(self.lineEdit_items.setHidden)
        self.radioButton_manual.clicked['bool'].connect(self.lineEdit_items.setVisible)
        self.radioButton_all.clicked['bool'].connect(self.lbl_itemName.setHidden)
        self.radioButton_manual.clicked['bool'].connect(self.lbl_itemName.setVisible)
        self.radioButton_all.clicked['bool'].connect(self.btn_enterItem.setHidden)
        self.radioButton_manual.clicked['bool'].connect(self.btn_enterItem.setVisible)
        self.radioButton_all.clicked['bool'].connect(self.comboBox_enteredItems.setHidden)
        self.radioButton_manual.clicked['bool'].connect(self.comboBox_enteredItems.setVisible)
        self.radioButton_all.clicked['bool'].connect(self.btn_removeItem.setHidden)
        self.radioButton_manual.clicked['bool'].connect(self.btn_removeItem.setVisible)
        QtCore.QMetaObject.connectSlotsByName(EstimationWindow)
        EstimationWindow.setTabOrder(self.comboBox_duration, self.radioButton_all)

    def retranslateUi(self, EstimationWindow):
        _translate = QtCore.QCoreApplication.translate
        EstimationWindow.setWindowTitle(_translate("EstimationWindow", "Estimation Window"))
        self.lbl_items.setText(_translate("EstimationWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Items</span></p></body></html>"))
        self.radioButton_all.setText(_translate("EstimationWindow", "All"))
        self.radioButton_manual.setText(_translate("EstimationWindow", "Manual"))
        self.btn_removeItem.setText(_translate("EstimationWindow", "Remove item"))
        self.btn_enterItem.setText(_translate("EstimationWindow", "Enter item"))
        self.comboBox_duration.setItemText(0, _translate("EstimationWindow", "1 Month"))
        self.comboBox_duration.setItemText(1, _translate("EstimationWindow", "3 Month"))
        self.comboBox_duration.setItemText(2, _translate("EstimationWindow", "6 Month"))
        self.comboBox_duration.setItemText(3, _translate("EstimationWindow", "1 Year"))
        self.btn_predictProfit.setText(_translate("EstimationWindow", "Predict profit"))
        self.lbl_duration.setText(_translate("EstimationWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Duration</span></p></body></html>"))
        self.lbl_itemName.setText(_translate("EstimationWindow", "Item Name"))

