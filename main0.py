from datetime import datetime
from dateutil.parser import parse
import pandas as pd

file=None
try:
    file=open("Data.csv","r")
except:
    with open("Data.csv","w") as file:
        file.write("Date,Type,Product,Quantity,Price_Per_Unit,Total_Price,Description\n")
        file.close()

try:
    file=open("dataToDoList.csv","r")
except:
    with open("dataToDoList.csv","w+") as file:
        file.write("Time,Description\n")          #file for data entry of remainders
        file.close()


class Entry:
    def __init__(self):
        self.product_name=None
        self.quantity=0
        self.price_per_unit=0.0
        self.total_price=0.0                    
        self.description=None
        self.type_of_entry=None
        self.date=None                         #default initialization
        

    def set_product_name(self,product_name):
        self.product_name = product_name

    def set_quantity(self,quantity):
        self.quantity=quantity

    def set_price_per_unit(self,price_per_unit):
        self.price_per_unit=price_per_unit

    def set_description(self,description):
        self.description=description

    def set_date(self,date):
        self.date=date


    """
    entry():

    method to write the entry in the file and will be called at last after setting all the attributes

    if anything goes wrong in setting the attributes and is not handled by code
    then just don't call the method, entry will not be added to the file
    """
    def entry(self):                            #
        file=open("Data.csv","a")
        if self.type_of_entry == 'Buy':
            self.total_price = -(self.quantity * self.price_per_unit)
        else:
            self.total_price = (self.quantity  * self.price_per_unit)
        file.write(str(self.date)+","+ str(self.type_of_entry) + "," + str(self.product_name) + "," + str(self.quantity) + "," + str(self.price_per_unit) + ","+str(self.total_price)+"," +str(self.description) + "\n")
        file.close()
    """
    delete(index)
    method to delete the entry and is to be called with "index" parameter i.e. id of entry that you
    want to delete
    """
    @staticmethod
    def delete(index):
        file=pd.read_csv("Data.csv", index_col=None)
        try:
            file.drop(file.index[index], inplace=True)
        except IndexError:
            print("Index out of bound...!!!")
        file.to_csv("Data.csv",index=False)



class Buy(Entry):
    def __init__(self):
        Entry.__init__(self)
        self.type_of_entry="Buy"

class Sell(Entry):
    def __init__(self):
        Entry.__init__(self)
        self.type_of_entry="Sell"


class ToDo:
    tasks = {}
    def __init__(self):
        self.day = datetime.now().day
        self.month = datetime.now().month
        self.year = datetime.now().year
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.description = None                  #default initialization(current time)

    def set_day(self,day):
        self.day = day

    def set_month(self,month):
        self.month = month

    def set_year(self,year):
        self.year = year

    def set_hour(self,hour):
        self.hour = hour

    def set_minute(self,minute):
        self.minute = minute

    def set_description(self,description):
        self.description = description            #setter methods for giving time of remainders

    @staticmethod
    def delete_task(index):
        file = pd.read_csv("dataToDoList.csv", index_col=None)
        try:
            file.drop(file.index[index], inplace=True)
        except IndexError:
            print("Index out of bound...!!!")
        file.to_csv("dataToDoList.csv", index=False)


    """
    remind() function will notify for reminders at or after little time of entry and should be called
    at pertiular duration continuously
    """
    @staticmethod
    def remind():
        with open("dataToDoList.csv", "r") as file:
            reader=file.readlines()[1:]
            for rows in reader:
                ToDo.tasks[(rows.split(",")[0])]=rows.split(",")[1]

        for key in sorted(ToDo.tasks.keys()):
            if parse(key) <= datetime.now():
                print(ToDo.tasks[key])
            else:
                break

    """
    add_task() will write the entry of reminder in file 
    """
    def add_task(self):
        with open("dataToDoList.csv", "a") as file:
            file.write(str(datetime(day = self.day, month = self.month, year = self.year, hour = self.hour, minute = self.minute)) + "," + str(self.description)+"\n")
            file.close()



while True:
    print("======================================================")
    print("\n1:sell\n2:buy\n3:delete\n4:Add task in ToDo\n5:Delete task in ToDo\n6:Remind tasks\n7:exit\n")
    c=int(input(":"))
    t=ToDo()
    if c == 1:
        e = Sell()
    elif c == 2:
        e = Buy()
    elif c == 3:
        index = int(input("Enter id of entry to delete:"))
        Entry.delete(index)
        continue
    elif c == 4:
        t.set_minute(int(input("Enter minute:")))  # you can set hour,month,year by calling their respective setter methods
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
        e.set_product_name(input("Product Name:\n"))
        e.set_date(input("Date:\n"))
        e.set_quantity(int(input("Quantity:\n")))
        e.set_price_per_unit(float(input("Price per Unit:\n")))
        e.set_description(input("Description:\n"))
        e.entry()
    except ValueError:
        print("Please enter values of proper type...")