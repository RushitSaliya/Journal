# imported all built-in modules for which we cares
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import csv
import sys

import matplotlib
matplotlib.use('Qt5Agg')


# imported file s, which is made by the ARTISTS (If you know what I mean...🤙)
from main0 import *
from main1 import *

# imported modules which locally located within Py_Scripts directory
from Py_Scripts \
    import MainWindow, AddRecordDialog, DeleteRecordDialog, SignInDialog, StatisticsWindow, EstimationWindow


class Methods:
    """This class is the collection of some handy methods. All the methods of this class are @staticmethod"""

    @staticmethod
    def get_rows(path):
        """This method is for getting number of rows from the file"""

        with open(path, "r") as file_of_main2:
            file_reader = csv.reader(file_of_main2, delimiter=",")
            rows = len(list(file_reader)) - 1
        return rows

    @staticmethod
    def isSubElement(sub_element, array):
        """Method to check whether given element <sub_element> is a sub element of list <array> or not"""

        flag = False
        for i in range(array.__len__()):
            if sub_element == array[i]:
                flag = True
        return flag


class ClassSignInDialog(QDialog, SignInDialog.Ui_SignInDialog):
    """Class of SignIN dialog for validating user-credentials"""

    def __init__(self):
        """I don't have anything to say here :)"""

        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        # declaration of all instance variables
        self.start_app_obj = None
        self.response_message = QtWidgets.QErrorMessage()

        # calls of event handlers
        self.btn_Sign_in.clicked.connect(self.start_application)

    def start_application(self):
        """If user has entered valid credentials then he/she is more then welcome to this application"""

        if self.line_edit_username.text() == "12" and self.line_edit_password.text() == "12":
            self.start_app_obj = ClassMainWindow()
            self.start_app_obj.retranslateUi(self.start_app_obj)
            self.start_app_obj.showMaximized()
            self.close()
        else:
            self.response_message.setWindowTitle("Error Message")
            self.response_message.showMessage("Invalid Username or Password 😟 !!!")
            self.response_message.show()
            self.line_edit_username.clear()
            self.line_edit_password.clear()

            # After entering wrong username or password user must encountered with Username focused line-edit
            self.line_edit_username.setFocus()


class ClassMainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    """Welcome to the class of MainWindow (obviously) 😀"""

    def __init__(self):
        """Constructor with no legacy of parameter"""

        # noinspection PyArgumentList
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()

        # declaration of all instance variables
        self.add_record_dialog_object = ClassAddRecordDialog()
        self.self_object = None   # instance variable for showing window again with fresh content
        self.delete_record_dialog_object = ClassDeleteRecordDialog()
        self.graph_dialog = ClassStatisticsWindow()
        self.estimation_window = ClassEstimationWindow()

        # calls of event handlers
        self.btn_add_record.clicked.connect(self.pop_up_add_record_dialog)
        self.btn_refresh.clicked.connect(self.refresh_record)
        self.btn_delete_record.clicked.connect(self.pop_up_delete_record_dialog)
        self.btn_statistics.clicked.connect(self.pop_up_statistics_dialog)
        self.btn_suggestions.clicked.connect(self.pop_up_estimation_window)

        # assigned shortcuts to some reputed actions which has high frequency of usage
        self.shortcut1 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_R), self)
        # noinspection PyUnresolvedReferences
        self.shortcut1.activated.connect(self.refresh_record)

        self.shortcut2 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_A), self)
        # noinspection PyUnresolvedReferences
        self.shortcut2.activated.connect(self.pop_up_add_record_dialog)

        self.shortcut3 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_D), self)
        # noinspection PyUnresolvedReferences
        self.shortcut3.activated.connect(self.pop_up_delete_record_dialog)

        self.shortcut4 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_S), self)
        # noinspection PyUnresolvedReferences
        self.shortcut4.activated.connect(self.pop_up_statistics_dialog)

        self.shortcut5 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_E), self)
        # noinspection PyUnresolvedReferences
        self.shortcut5.activated.connect(self.pop_up_estimation_window)

        # to count number of rows in Data.csv file in order to write it in tabular form
        rows = Methods.get_rows("Data.csv")

        # to set number of rows and columns of table
        self.tbl_widget_existing_records.setRowCount(rows)
        self.tbl_widget_existing_records.setColumnCount(7)

        # to set specific column width of table widget (column_index, size)
        self.tbl_widget_existing_records.setColumnWidth(0, 70)
        self.tbl_widget_existing_records.setColumnWidth(1, 60)
        self.tbl_widget_existing_records.setColumnWidth(3, 60)  # third column (index2) is by default well-settled
        self.tbl_widget_existing_records.setColumnWidth(4, 85)
        self.tbl_widget_existing_records.setColumnWidth(5, 85)
        self.tbl_widget_existing_records.setColumnWidth(6, 600)

        # these are self-explanatory statements 🤗
        file_of_data = pd.read_csv("Data.csv")
        dict_index_to_headers = {0: "Date", 1: "Type", 2: "Product", 3: "Quantity", 4: "Price_Per_Unit",
                                 5: "Total_Price", 6: "Description"}

        # to assign column name to @table
        self.tbl_widget_existing_records.setHorizontalHeaderLabels(["Date", "Type", "Product Name", "Quantity",
                                                                    "Price per Unit", "Total Price", "Description"])

        # when we want to write content from file to table...
        for i in range(rows):
            for j in dict_index_to_headers:
                self.value = str(file_of_data.at[i, dict_index_to_headers[j]])
                self.tbl_widget_existing_records.setItem(i, j, QTableWidgetItem(self.value))

    # definitions of event handlers
    def pop_up_add_record_dialog(self):
        """For the purpose of popping up the (Self-proclaimed) gorgeous dialog called AddRecordDialog"""

        self.add_record_dialog_object.retranslateUi(self.add_record_dialog_object)
        self.add_record_dialog_object.show()

    # FIXME: encountered a bug about refreshing data (for more reference refer issue#1 of this repo)
    def refresh_record(self):
        """In order to re-load fresh data of MainWindow into table"""

        self.close()
        self.self_object = ClassMainWindow()    # specified ClassName here because I'm afraid of MaximumRecursiveError 😱
        self.self_object.retranslateUi(self.self_object)

        self.self_object.showMaximized()

        # for updating date label right on MainWindow
        self.self_object.lbl_date.setText("Date: " + str(datetime.now().date()) + "\n     (YYYY-MM-DD)")
        self.self_object.lbl_date.setFont(QFont('Arial', 15))  # we have to update a label's font after doing explicit modification on it

        self.self_object.lbl_buy.setText("Buy: " + str(Entry.total_buy_method()))
        self.self_object.lbl_buy.setFont(QFont('Arial', 15))

        self.self_object.lbl_sell.setText("Sell: " + str(Entry.total_sell_method()))
        self.self_object.lbl_sell.setFont(QFont('Arial', 15))

    def pop_up_delete_record_dialog(self):
        """This block of code is responsible for popping up the DeleteRecordDialog. That's what exactly we call a method!!!"""

        self.delete_record_dialog_object.retranslateUi(self.delete_record_dialog_object)
        self.delete_record_dialog_object.show()

    def pop_up_statistics_dialog(self):
        self.graph_dialog.retranslateUi(self.graph_dialog)
        self.graph_dialog.showMaximized()

    def pop_up_estimation_window(self):
        self.estimation_window.retranslateUi(self.estimation_window)
        self.estimation_window.showMaximized()


class ClassAddRecordDialog(QDialog, AddRecordDialog.Ui_AddRecordDialog):
    """Class of Add Record Dialog"""

    # noinspection PyArgumentList
    def __init__(self):
        """Meet, Default constructor itself!!!"""

        QDialog.__init__(self)
        self.setupUi(self)

        # declaration of all instance variables
        self.entry_obj = None
        self.response_message = QtWidgets.QErrorMessage()  # instance variable for showing response message at the time of adding data

        # calls of event handlers
        self.btn_add.clicked.connect(self.write_entered_record_to_file)
        self.btn_add.clicked.connect(self.close)
        self.btn_cancel.clicked.connect(self.close)

    # definitions of event handlers
    def write_entered_record_to_file(self):
        """Event handler for writing entered data to file"""

        # to paste the data to the respective instance variables
        self.entry_obj = Entry(date=self.date_edit_date.text(), product_name=self.line_edit_name_of_product.text(),
                               quantity=int(self.line_edit_quantity.text()), price_per_unit=int(self.line_edit_price_per_unit.text()),
                               description=self.text_edit_description.toPlainText())

        if self.radio_btn_buy.isChecked():
            self.entry_obj.type_of_entry = "Buy"
        elif self.radio_btn_sell.isChecked():
            self.entry_obj.type_of_entry = "Sell"

        # to paste filled data into file from Ui_Elements (Written this comment just for the sake of comment-protocol 😅)
        self.entry_obj.entry()

        # to pop up success message after entering data into file
        self.response_message.setWindowTitle("Success Message")
        self.response_message.showMessage("Record Added Successfully 🙂 !!!")
        self.response_message.show()


class ClassDeleteRecordDialog(QDialog, DeleteRecordDialog.Ui_DeleteRecordDialog):
    """Here (in this class) we are suppose to manage the task of deleting file's existing data"""

    # noinspection PyArgumentList
    def __init__(self):
        """😁 (fair enough!!!)"""

        QDialog.__init__(self)
        self.setupUi(self)

        # declaration of all instance variables
        self.index_from_line_edit = int()
        self.response_message = QtWidgets.QErrorMessage()

        # calls of event handlers
        self.btn_delete.clicked.connect(self.delete_record)

    # definition of event handlers
    def delete_record(self):
        """When we want to just erase the record..."""

        # to fetch index that user has entered
        self.index_from_line_edit = int(self.line_edit_index.text()) - 1

        # let us try first that the index that user has just entered is valid or not...!!!
        try:
            # static_method call for erasing record by just the straight way that we all love ( #StaticMethod 🤘_😍)
            Entry.delete(self.index_from_line_edit)

            # to pop up success message after successful deletion of record
            self.response_message.setWindowTitle("Success Message")
            self.response_message.showMessage("Record deleted successfully 🙂 !!!")
            self.response_message.show()

        except IndexError:
            # to pop up error message in case of Invalid Index
            self.response_message.setWindowTitle("Error Message")
            self.response_message.showMessage("Invalid Index 😟 !!!")
            self.response_message.show()

        self.close()


class ClassStatisticsWindow(QMainWindow, StatisticsWindow.Ui_StatisticsWindow):
    """In this class poet wants to plot data on the graph by dividing them into Buy and Sell"""

    def __init__(self):
        """Default constructor for ClassStatisticsWindow"""

        QMainWindow.__init__(self)
        self.setupUi(self)

        self.canvas0 = ExpenseCanvas(self, width=6, height=6)
        self.canvas0.move(50, 60)

        self.canvas1 = ProfitCanvas(self, width=6, height=6)
        self.canvas1.move(710, 60)


class ClassEstimationWindow(QMainWindow,  EstimationWindow.Ui_EstimationWindow):
    """This class is all about prediction of profit"""

    # list of items selected by user which will be predicted by prediction model
    strList = []

    # dictionary of items with its predicted profit as key and its value respectively
    result_dict = {}

    def __init__(self):
        """Default constructor for ClassEstimationWindow"""

        # noinspection PyArgumentList
        QMainWindow.__init__(self)
        self.setupUi(self)

        # declaration of class variables
        self.response_message = QtWidgets.QErrorMessage()
        self.prediction_canvas = None

        # for plotting prediction graph on MainWindow with appropriate co-ordinates
        self.figure = Figure(figsize=(12, 8), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addWidget(self.canvas, 5, 1, 5, 11)

        # declaration of event-handler
        self.btn_enterItem.clicked.connect(self.enter_item_to_list)
        self.btn_removeItem.clicked.connect(self.remove_item_from_list)
        self.btn_predictProfit.clicked.connect(self.generate_graphs_of_predicted_profit)

        # to hide lbl_itemName and lineEdit_item initially to prevent access if radioButton_all is checked
        if self.radioButton_all.isChecked():
            self.lineEdit_items.setHidden(True)
            self.lbl_itemName.setHidden(True)
            self.btn_enterItem.setHidden(True)
            self.comboBox_enteredItems.setHidden(True)
            self.btn_removeItem.setHidden(True)
        else:
            self.lineEdit_items.setVisible(True)
            self.lineEdit_items.setVisible(True)
            self.btn_enterItem.setVisible(True)
            self.comboBox_enteredItems.setVisible(True)
            self.btn_removeItem.setVisible(True)

        # to set auto-completer to lineEdit_items
        rows = Methods.get_rows("Data.csv")

        file_of_data = pd.read_csv("Data.csv")

        for i in range(rows):
            self.value = str(file_of_data.at[i, "Product"])
            ClassEstimationWindow.strList.append(self.value)

        # TODO: need to change source of data into following line from 'name_of_products' to 'strList'
        self.completer = QCompleter(name_of_products, self.lineEdit_items)

        # when we want to set match option something like, "Tell me if you found this word (or character) even in between"
        self.completer.setFilterMode(Qt.MatchContains)

        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)     # to make QCompleter CaseInsensitive
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.lineEdit_items.setCompleter(self.completer)    # to impose completer to lineEdit

    def enter_item_to_list(self):
        """To insert entered item to comboBox for further procedure"""

        item = self.lineEdit_items.text()

        # TODO: change list parameter of isSubElement method from name_of_products to ClassEstimationWindow.strList
        if Methods.isSubElement(item, name_of_products):
            self.comboBox_enteredItems.addItem(item)
            self.lineEdit_items.clear()
            self.lineEdit_items.setFocus()
        else:
            self.lineEdit_items.clear()
            self.lineEdit_items.setFocus()
            self.response_message.setWindowTitle("Error Message")
            self.response_message.showMessage("Invalid item inserted 😟 !!!")
            self.response_message.show()

    def remove_item_from_list(self):
        """To remove entered item from comboBox for further procedure"""

        self.comboBox_enteredItems.removeItem(self.comboBox_enteredItems.currentIndex())

    def generate_graphs_of_predicted_profit(self):
        """To generate graphs of predicted profit for preferred items"""

        from_this_year, from_this_month, from_this_day = str(datetime.now().date()).split('-')

        # if user wants duration of upcoming 1 month, 3 months, 6 months or 1 year then the index of selected comboBox-element will be 0, 1, 2 or 3 respectively
        if self.comboBox_duration.currentIndex() == 0:
            to_this_year, to_this_month, to_this_day = str((datetime.now().date()) + timedelta(days=30)).split('-')
        elif self.comboBox_duration.currentIndex() == 1:
            to_this_year, to_this_month, to_this_day = str((datetime.now().date()) + timedelta(days=90)).split('-')
        elif self.comboBox_duration.currentIndex() == 2:
            to_this_year, to_this_month, to_this_day = str((datetime.now().date()) + timedelta(days=180)).split('-')
        else:
            to_this_year, to_this_month, to_this_day = str((datetime.now().date()) + timedelta(days=365)).split('-')

        # converted split string into integer to pass these into @predict_profit method since it's accepts day, month and year in integer only (rude af!)
        from_this_year, from_this_month, from_this_day = int(from_this_year), int(from_this_month), int(from_this_day)
        to_this_year, to_this_month, to_this_day = int(to_this_year), int(to_this_month), int(to_this_day)

        # to select items according to checked radioButton
        if self.radioButton_manual.isChecked():
            items = [self.comboBox_enteredItems.itemText(i) for i in range(self.comboBox_enteredItems.count())]
        else:
            items = name_of_products

        # TODO: temporarily passed value of products name_of_products instead of passing data from Data.csv
        ClassEstimationWindow.result_dict = Entry.predict_profit(from_this_day, from_this_month, from_this_year, to_this_day, to_this_month, to_this_year, items)

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.bar([item for item in ClassEstimationWindow.result_dict], [ClassEstimationWindow.result_dict[item] for item in ClassEstimationWindow.result_dict])
        ax.set_title('Profit prediction')
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit in ₹')

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    JOURNAL = ClassSignInDialog()
    JOURNAL.show()
    sys.exit(app.exec_())
