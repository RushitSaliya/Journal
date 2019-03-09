from datetime import datetime
from datetime import timedelta
import pandas as pd
from Fill_dataset_2 import map, products_dict, name_of_products
from Regression import model

file = None

"""Trying to open existing file if not found (in the case of first time execution) new file will be created."""
try:
    file = open("Data.csv", "r")
except FileNotFoundError:
    with open("Data.csv", "w") as file:
        file.write("Date,Type,Product,Quantity,Price_Per_Unit,Total_Price,Description\n")
        file.close()


class Entry:
    total_buy = 0.0
    total_sell = 0.0  # inititalization of static variables

    def __init__(self, date="", type_of_entry="", product_name="", quantity=0, price_per_unit=0.0, description=""):
        """For initializing the parameters."""

        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total_price = None
        self.description = description
        self.type_of_entry = type_of_entry
        self.date = date

    def entry(self):
        """This method will write an entry in the file and should be called at last after setting all the attributes"""

        datafile = open("Data.csv", "a")
        if self.type_of_entry == 'Buy':
            self.total_price = -(self.quantity * self.price_per_unit)
        else:
            self.total_price = (self.quantity * self.price_per_unit)
        datafile.write(str(self.date) + "," + str(self.type_of_entry) + "," + str(self.product_name) + "," + str(
            self.quantity) + "," + str(self.price_per_unit) + "," + str(self.total_price) + "," + str(
            self.description) + "\n")
        datafile.close()

    @staticmethod
    def delete(delete_index):
        """This will delete the entry at specified index i.e. delete_index parameter"""

        datafile = pd.read_csv("Data.csv", index_col=None)
        datafile.drop(datafile.index[delete_index], inplace=True)
        datafile.to_csv("Data.csv", index=False)

    @staticmethod
    def total_buy_method():
        """This method will calculate total amount of purchase and must be called after each buy data entry..."""

        datafile = pd.read_csv("Data.csv")
        buydata = datafile.where(datafile["Type"] == "Buy").iloc[:, 5]
        Entry.total_buy = -buydata.sum()
        return Entry.total_buy

    @staticmethod
    def total_sell_method():
        """This method will calculate total amount of sell and must be called after each sell data entry..."""

        datafile = pd.read_csv("Data.csv")
        selldata = datafile.where(datafile["Type"] == "Sell").iloc[:, 5]
        Entry.total_sell = selldata.sum()
        return Entry.total_sell

    @staticmethod
    def predict_profit(day1=datetime.now().day, month1=datetime.now().month, year1=datetime.now().year, day2=None, month2=None, year2=None, products=name_of_products):
        """This method will predict the profit from individual product in given period of time i.e. from date day1/month1/year1 to day2/mont2/year2"""

        predicted = {}
        date = datetime.date(datetime(year1, month1, day1))
        if day2 == month2 == year2 is None:
            lastdate = date + timedelta(days=30)
        else:
            lastdate = datetime.date(datetime(year2, month2, day2))
        temp = date
        for product in products:
            predicted[product] = 0
            date = temp
            while date != lastdate + timedelta(days=1):
                predicted[product] += float(model.predict([[date.day, date.month, date.year, products_dict[product],
                                                            map[product][0], map[product][0] + map[product][1]]]))
                date += timedelta(days=1)
        return predicted


if __name__ == "__main__":
    while True:
        print("======================================================")
        print("\n1:sell\n2:buy\n3:delete\n4:predict\n5:exit\n")
        Entry.total_buy_method()
        Entry.total_sell_method()
        print("total sell =" + str(Entry.total_sell))
        print("total buy =" + str(Entry.total_buy))
        c = int(input(":"))
        e_type_of_entry = None
        if c == 1:
            e_type_of_entry = "Sell"
        elif c == 2:
            e_type_of_entry = "Buy"
        elif c == 3:
            index = int(input("Enter id of entry to delete:"))
            Entry.delete(index)
            continue
        elif c == 4:
            print(Entry.predict_profit())
            continue
        else:
            print("======================================================\n")
            exit(0)
        try:
            e_product_name = (input("Product Name:\n"))
            e_date = (input("Date:\n"))
            e_quantity = (int(input("Quantity:\n")))
            e_price_per_unit = (float(input("Price per Unit:\n")))
            e_description = (input("Description:\n"))
            e = Entry(e_date, e_type_of_entry, e_product_name, e_quantity, e_price_per_unit, e_description)
            e.entry()
        except ValueError:
            print("Please enter values of proper type...")
