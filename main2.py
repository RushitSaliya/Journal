# imported all built-in modules
from PyQt5.QtWidgets import *
import csv

# imported files, which is made by the ARTISTS (If you know what I mean...🤙)
from main0 import *
from main1 import *

# imported modules which locally located within Py_Scripts directory
from Py_Scripts \
    import MainWindow, AddRecordDialog


class ClassMainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    """Welcome to the class of MainWindow (obviously) 😀"""

    def __init__(self):
        """Constructor with no legacy of parameter"""

        QMainWindow.__init__(self)
        self.setupUi(self)

        # declaration of all instance variables
        self.add_record_dialog_object = ClassAddRecordDialog()
        self.self_object = None   # instance variable for showing window again with fresh content

        # calls of event handlers
        self.btn_add_record.clicked.connect(self.pop_up_add_record_dialog)
        self.btn_refresh.clicked.connect(self.refresh_record)

        # to count number of rows in Data.csv file in order to write it in tabular form
        with open("Data.csv", "r") as file_of_main2:
            file_reader = csv.reader(file_of_main2, delimiter=",")
            rows = len(list(file_reader)) - 1

        # to set number of rows and columns of table
        self.tbl_widget_existing_records.setRowCount(rows)
        self.tbl_widget_existing_records.setColumnCount(7)

        # these are self-explanatory statements 🤗
        file_of_data = pd.read_csv("Data.csv")
        dict_index_to_headers = {0: "Date", 1: "Type", 2: "Product", 3: "Quantity", 4: "Price_Per_Unit",
                                 5: "Total_Price", 6: "Description"}

        # to assign column name to table
        self.tbl_widget_existing_records.setHorizontalHeaderLabels(["Date", "Type", "Product", "Quantity",
                                                                    "Price per Unit", "Total Price", "Description"])

        # when we want to write content from file to table...
        for i in range(rows):
            for j in dict_index_to_headers:
                self.value = str(file_of_data.at[i, dict_index_to_headers[j]])
                self.tbl_widget_existing_records.setItem(i, j, QTableWidgetItem(self.value))

    # definitions of event handlers
    def pop_up_add_record_dialog(self):
        """For the purpose of popping up the gorgeous dialog called AddRecordDialog"""

        self.add_record_dialog_object.retranslateUi(self.add_record_dialog_object)
        self.add_record_dialog_object.show()

    def refresh_record(self):
        """In order to re-load fresh data of MainWindow into table"""

        self.close()
        self.self_object = ClassMainWindow()    # specified ClassName here because I'm afraid of MaximumRecursiveError 😱
        self.self_object.retranslateUi(self.self_object)
        self.self_object.show()


class ClassAddRecordDialog(QDialog, AddRecordDialog.Ui_AddRecordDialog):
    """Class of Add Record Dialog"""

    def __init__(self):
        """Meet, Default constructor itself!!!"""

        QDialog.__init__(self)
        self.setupUi(self)

        # declaration of all instance variables
        self.entry_obj = Entry()

        # calls of event handlers
        self.btn_add.clicked.connect(self.write_entered_record_to_file)
        self.btn_add.clicked.connect(self.close)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    JOURNAL = ClassMainWindow()
    JOURNAL.show()
    app.exec_()
