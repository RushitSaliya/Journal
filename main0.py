from datetime import datetime
from dateutil.parser import parse
import pandas as pd

file = None
try:
    file = open("Data.csv", "r")
except FileNotFoundError:
    with open("Data.csv", "w") as file:
        file.write("Date,Type,Product,Quantity,Price_Per_Unit,Total_Price,Description\n")
        file.close()

try:
    file = open("dataToDoList.csv", "r")
except FileNotFoundError:
    with open("dataToDoList.csv", "w+") as file:
        file.write("Time,Description\n")  # file for data entry of remainders
        file.close()


class Entry:
    total_buy = 0.0
    total_sell = 0.0

    def __init__(self, date, type_of_entry, product_name, quantity, price_per_unit, description):
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total_price = None
        self.description = description
        self.type_of_entry = type_of_entry
        self.date = date

    """
    entry():
    method to write the entry in the file and will be called at last after setting all the attributes
    if anything goes wrong in setting the attributes and is not handled by code
    then just don't call the method, entry will not be added to the file
    """

    def entry(self):
        datafile = open("Data.csv", "a")
        if self.type_of_entry == 'Buy':
            self.total_price = -(self.quantity * self.price_per_unit)
        else:
            self.total_price = (self.quantity * self.price_per_unit)
        datafile.write(str(self.date) + "," + str(self.type_of_entry) + "," + str(self.product_name) + "," + str(
            self.quantity) + "," + str(self.price_per_unit) + "," + str(self.total_price) + "," + str(
            self.description) + "\n")
        datafile.close()

    """
    delete(index)
    method to delete the entry and is to be called with "index" parameter i.e. id of entry that you
    want to delete
    """

    @staticmethod
    def delete(delete_index):
        datafile = pd.read_csv("Data.csv", index_col=None)
        datafile.drop(datafile.index[delete_index], inplace=True)
        datafile.to_csv("Data.csv", index=False)

    """
    total_buy_sell():
    it will update two class variables buydata & selldata which are total of buy & sell respectively...
    should be called with each entry
    """
    @staticmethod
    def total_buy_sell():
        datafile = pd.read_csv("Data.csv")
        buydata = datafile.where(datafile["Type"] == "Buy").iloc[:, 5]
        selldata = datafile.where(datafile["Type"] == "Sell").iloc[:, 5]
        Entry.total_buy = -buydata.sum()
        Entry.total_sell = selldata.sum()


class ToDo:
    tasks = {}

    def __init__(self):
        self.day = datetime.now().day
        self.month = datetime.now().month
        self.year = datetime.now().year
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.description = None  # default initialization(current time)

    def set_day(self, day):
        self.day = day

    def set_month(self, month):
        self.month = month

    def set_year(self, year):
        self.year = year

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute

    def set_description(self, description):
        self.description = description  # setter methods for giving time of remainders

    @staticmethod
    def delete_task(delete_task_index):
        tododatafile = pd.read_csv("dataToDoList.csv", index_col=None)
        try:
            tododatafile.drop(tododatafile.index[delete_task_index], inplace=True)
        except IndexError:
            print("Index out of bound...!!!")
        tododatafile.to_csv("dataToDoList.csv", index=False)

    """
    remind() function will notify for reminders at or after little time of entry and should be called
    at particular duration continuously
    """

    @staticmethod
    def remind():
        with open("dataToDoList.csv", "r") as tododatafile:
            reader = tododatafile.readlines()[1:]
            for rows in reader:
                ToDo.tasks[(rows.split(",")[0])] = rows.split(",")[1]

        for key in sorted(ToDo.tasks.keys()):
            if parse(key) <= datetime.now():
                print(ToDo.tasks[key])
            else:
                break
        tododatafile.close()

    """
    add_task() will write the entry of reminder in file 
    """

    def add_task(self):
        with open("dataToDoList.csv", "a") as tododatafile:
            tododatafile.write(str(datetime(day=self.day, month=self.month, year=self.year, hour=self.hour,
                                            minute=self.minute)) + "," + str(self.description) + "\n")
            tododatafile.close()


"""
if __name__ == "__main__":
    while True:
        print("======================================================")
        print("\n1:sell\n2:buy\n3:delete\n4:Add task in ToDo\n5:Delete task in ToDo\n6:Remind tasks\n7:exit\n")
        Entry.total_buy_sell()
        print("total sell =" + str(Entry.total_sell))
        print("total buy =" + str(Entry.total_buy))
        c = int(input(":"))
        t = ToDo()
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
            t.set_minute(
                int(input("Enter minute:")))  # you can set hour,month,year by calling their respective setter methods
            t.set_description(input("Enter Description:"))
            t.add_task()
            continue
        elif c == 5:
            t.delete_task(int(input("Enter id:")))
            continue
        elif c == 6:
            t.remind()
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
"""
