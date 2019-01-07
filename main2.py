# imported all built-in modules
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import csv

# imported files, which is made by the ARTISTS (If you know what I mean...🤙)
from main0 import *
from main1 import *

# imported modules which locally located within Py_Scripts directory
from Py_Scripts \
    import MainWindow, AddRecordDialog, DeleteRecordDialog


class ClassMainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    """Welcome to the class of MainWindow (obviously) 😀"""

    def __init__(self):
        """Constructor with no legacy of parameter"""

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()

        # declaration of all instance variables
        self.add_record_dialog_object = ClassAddRecordDialog()
        self.self_object = None   # instance variable for showing window again with fresh content
        self.delete_record_dialog_object = ClassDeleteRecordDialog()

        # calls of event handlers
        self.btn_add_record.clicked.connect(self.pop_up_add_record_dialog)
        self.btn_refresh.clicked.connect(self.refresh_record)
        self.btn_delete_record.clicked.connect(self.pop_up_delete_record_dialog)

        # to count number of rows in Data.csv file in order to write it in tabular form
        with open("Data.csv", "r") as file_of_main2:
            file_reader = csv.reader(file_of_main2, delimiter=",")
            rows = len(list(file_reader)) - 1

        # to set number of rows and columns of table
        self.tbl_widget_existing_records.setRowCount(rows)
        self.tbl_widget_existing_records.setColumnCount(7)

        # to set specific column width of table widget (column_index, size)
        self.tbl_widget_existing_records.setColumnWidth(0, 70)
        self.tbl_widget_existing_records.setColumnWidth(1, 60)
        self.tbl_widget_existing_records.setColumnWidth(3, 60)  # third column (index2) is by default well-settled by born
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

    def refresh_record(self):
        """In order to re-load fresh data of MainWindow into table"""

        self.close()
        self.self_object = ClassMainWindow()    # specified ClassName here because I'm afraid of MaximumRecursiveError 😱
        self.self_object.retranslateUi(self.self_object)
        self.self_object.showMaximized()

    def pop_up_delete_record_dialog(self):
        """This block of code is responsible for popping up the DeleteRecordDialog. That's what exactly we call a method!!!"""

        self.delete_record_dialog_object.retranslateUi(self.delete_record_dialog_object)
        self.delete_record_dialog_object.show()


class ClassAddRecordDialog(QDialog, AddRecordDialog.Ui_AddRecordDialog):
    """Class of Add Record Dialog"""

    def __init__(self):
        """Meet, Default constructor itself!!!"""

        QDialog.__init__(self)
        self.setupUi(self)

        # declaration of all instance variables
        self.entry_obj = Entry()
        self.response_message = QtWidgets.QErrorMessage()  # instance variable for showing response message at the time of adding data

        # calls of event handlers
        self.btn_add.clicked.connect(self.write_entered_record_to_file)
        self.btn_add.clicked.connect(self.close)
        self.btn_cancel.clicked.connect(self.close)

    # definitions of event handlers
    def write_entered_record_to_file(self):
        """Event handler for writing entered data to file"""

        # to paste the data to the respective instance variables
        self.entry_obj.set_date(self.date_edit_date.text())
        self.entry_obj.set_product_name(self.line_edit_name_of_product.text())
        self.entry_obj.set_quantity(int(self.line_edit_quantity.text()))
        self.entry_obj.set_price_per_unit(int(self.line_edit_price_per_unit.text()))
        self.entry_obj.set_description(self.text_edit_description.toPlainText())

        if self.radio_btn_buy.isChecked():
            self.entry_obj.type_of_entry = "Buy"
        elif self.radio_btn_sell.isChecked():
            self.entry_obj.type_of_entry = "Sell"

        # to paste filled data into file (Written this comment just for the sake of comment-protocol 😅)
        self.entry_obj.entry()
        
        # to pop up success message after entering data into file
        self.response_message.setWindowTitle("Success Message")
        self.response_message.showMessage("Record Added Successfully!!!")
        self.response_message.show()


class ClassDeleteRecordDialog(QDialog, DeleteRecordDialog.Ui_DeleteRecordDialog):
    """Here (in this class) we are suppose to manage the task of deleting file's existing data"""

    def __init__(self):
        """😁 (fair enough!!!)"""

        QDialog.__init__(self)
        self.setupUi(self)

        # declaration of all instance variables
        self.index_from_line_edit = int()

        # calls of event handlers
        self.btn_delete.clicked.connect(self.delete_record)

    # definition of event handlers
    def delete_record(self):
        """When we want to just delete the record..."""

        # to fetch index that user has entered
        self.index_from_line_edit = int(self.line_edit_index.text()) - 1

        # static_method call to erase record by just the straight way that we all love ( #StaticMethod 🤘_😍)
        Entry.delete(self.index_from_line_edit)

        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    JOURNAL = ClassMainWindow()
    JOURNAL.show()
    app.exec_()
