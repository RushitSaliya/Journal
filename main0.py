
import pandas as pd
file=None
try:
    file=open("Data.csv","r")
except:
    with open("Data.csv","w") as file:
     file.write("Date,Type,Product,Quantity,Price_Per_Unit,Total_Price,Description\n")
     file.close()


class Entry:
    def __init__(self):
        self.product_name=None
        self.quantity=0
        self.price_per_unit=0.0
        self.description=None
        self.type_of_entry=None
        self.date=None               #default initialization

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
    then just don't call the method entry will not be added to the file
    """
    def entry(self):
        file=open("Data.csv","a")
        file.write(str(self.date)+","+ str(self.type_of_entry) + "," + str(self.product_name) + "," + str(self.quantity) + "," + str(self.price_per_unit) + ","+str(self.quantity*self.price_per_unit)+"," +str(self.description) + "\n")
        file.close()
    """
    delete(index)
    method to delete the entry and is to be called with "index" parameter i.e. id of entry that you
    want to delete
    """
    @staticmethod
    def delete(index):
        file=pd.read_csv("Data.csv",index_col=None)
        try:
         file.drop(file.index[index],inplace=True)
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


while True:
    print("\nsell:1\nbuy:2\ndelete:3\nexit:4\n")
    print(pd.read_csv("Data.csv"))
    c=int(input(":"))
    e=None
    if c==1:
        e=Sell()
    elif c==2:
        e=Buy()
    elif c==3:
        index = int(input("Enter id of entry to delete:"))
        Entry.delete(index)
        continue
    else:
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

