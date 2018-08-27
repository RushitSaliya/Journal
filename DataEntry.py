
def credit():
        fi=open("idb.csv","a+")
        id = int(open("idb.csv","r").readlines()[-1].split(",")[0])
        balance=int(open("idb.csv","r").readlines()[-1].split(",")[1])
        cr_bal=int(input("Enter amount:"))
        f=open("DataEntry.csv","a")
        des=input("Enter Description:")
        balance+=cr_bal
        id += 1
        f.write(str(id)+",Credit,"+str(des)+","+str(cr_bal)+","+str(balance)+"\n")
        fi.write(str(id) + "," + str(balance)+"\n")
        f.close()
        fi.close()

def debit():
        fi = open("idb.csv", "a+")
        id = int(open("idb.csv","r").readlines()[-1].split(",")[0])
        balance=int(open("idb.csv","r").readlines()[-1].split(",")[1])
        db_bal=int(input("Enter amount:"))
        f=open("DataEntry.csv","a")
        des=input("Enter Description:")
        balance-=db_bal
        id += 1
        f.write(str(id)+",Debit,"+str(des)+","+str(db_bal)+","+str(balance)+"\n")
        fi.write(str(id)+","+str(balance)+"\n")
        f.close()
        fi.close()

def display():
    f=open("DataEntry.csv","r")
    print("{:10} {:10} {:15} {:10} {:10}\n".format("id","type","description","amount" ,"closing balance"))
    for l in f.readlines():
        a=l.split(",")
        print("{:10} {:10} {:15} {:10} {:10}".format(a[0],a[1],a[2],a[3],a[4]))

try:
    f=open("DataEntry.csv","r")
except:
    f=open("DataEntry.csv","w")  #file for data entry
    f.close()

try:
    f=open("idb.csv","r")
except:
    f=open("idb.csv","w")    #file for id and closing balance
    f.write("0,0\n")
    f.close()

while True:
    print("D : Debit\nC : Credit\nP : Display\nQ : Quit")
    c=input("Enter your choice:")
    if c=='c' or c=='C':
        credit()
    elif c=='d' or c=='D':
        debit()
    elif c=='p' or c=='P':
        display()
    elif c=='q' or c=='Q':
       break
    else:
        print("Wrong choice! Try again...")
