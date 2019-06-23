import random

# enter no of entry (under consideration of your patience)
no_of_entries = [35, 42, 90, 50, 45, 46, 45, 34, 51, 52, 135, 100]
map = {"Redmi Note 4": [14000, 2000], "Redmi Note 5": [14000, 1750], "Redmi 4": [9000, 1000], "Redmi 4A": [7000, 1250],
       "Redmi Note 6": [15000, 1850], "Redmi Y1": [12000, 1500], "Redmi Note 6 pro": [16000, 2250],
       "Redmi Note 5 pro": [14000, 1950],
       "Redmi A1": [15000, 900], "Redmi A2": [14000, 1200], "Samsung Galaxy A7": [20000, 2000],
       "Samsung Galaxy J8": [22000, 1000],
       "Samsung Galaxy J8 plus": [24000, 1250], "Samsung Galaxy J4 plus": [25000, 990],
       "Samsung Galaxy A9": [31500, 1100],
       "Samsung Galaxy A8 star": [19000, 1250], "Samsung Galaxy S9 plus": [52000, 1500],
       "Samsung Galaxy On8": [26000, 1750],
       "Samsung Galaxy Note 9": [57000, 1900], "Samsung Galaxy S8": [45000, 1300], "Samsung Galaxy On6": [22000, 1450],
       "Samsung Galaxy J2": [7000, 700], "iphone 4": [11000, 500], "iphone 5": [16000, 450], "iphone 5s": [17000, 400],
       "iphone SE": [17000, 2250], "iphone 6": [23000, 3250], "iphone 6s": [27000, 3900], "iphone 7": [35000, 4100],
       "iphone 7s": [42000, 3500], "iphone 8": [46000, 1000], "iphone X": [6000, 1100], "iphone Xs": [72000, 1500],
       "iphone Xs max": [90000, 1750], "iphone Xr": [85000, 1300], "Nokia 6.1 plus": [20000, 3000],
       "Nokia 5.1 plus": [21000, 2750],
       "Nokia 8.1": [25000, 190], "Nokia 2.1": [10000, 2500], "Nokia 7.1": [19000, 400], "Nokia 1": [7000, 700],
       "Nokia 6.1": [18500, 2700], "Nokia 3.1 plus": [16000, 3000], "Nokia 7 plus": [22000, 3500],
       "Oneplus 6T": [35000, 3000],
       "Oneplus 6": [29000, 2900], "Oneplus 5T": [27000, 2000], "Oneplus 5": [25000, 2500], "Oneplus 3T": [20000, 2000],
       "Oneplus 3": [22000, 1000], "Oneplus X": [18000, 1500], "Oneplus Two": [18000, 750],
       "Oneplus One": [17000, 1100],
       "Oppo R15 pro": [35000, 2000], "Oppo R17": [30000, 1700], "Oppo R17 pro": [34000, 1500],
       "Oppo A7": [25000, 2300],
       "Oppo F9": [20000, 1900], "Oppo A5": [21000, 1000], "Oppo F9 pro": [19000, 130], "Oppo A3s": [18000, 1300]}
products_dict = {"Redmi Note 4": 0, "Redmi Note 5": 1, "Redmi 4": 2, "Redmi 4A": 3, "Redmi Note 6": 4, "Redmi Y1": 5,
                 "Redmi Note 6 pro": 6, "Redmi Note 5 pro": 7, "Redmi A1": 8,
                 "Redmi A2": 9, "Samsung Galaxy A7": 10, "Samsung Galaxy J8": 11, "Samsung Galaxy J8 plus": 12,
                 "Samsung Galaxy J4 plus": 13, "Samsung Galaxy A9": 14,
                 "Samsung Galaxy A8 star": 15, "Samsung Galaxy S9 plus": 16, "Samsung Galaxy On8": 17,
                 "Samsung Galaxy Note 9": 18, "Samsung Galaxy S8": 19,
                 "Samsung Galaxy On6": 20, "Samsung Galaxy J2": 21, "iphone 4": 22, "iphone 5": 23, "iphone 5s": 24,
                 "iphone SE": 25, "iphone 6": 26, "iphone 6s": 27, "iphone 7": 28,
                 "iphone 7s": 29, "iphone 8": 30, "iphone X": 31, "iphone Xs": 32, "iphone Xs max": 33, "iphone Xr": 34,
                 "Nokia 6.1 plus": 35, "Nokia 5.1 plus": 36, "Nokia 8.1": 37,
                 "Nokia 2.1": 38, "Nokia 7.1": 39, "Nokia 1": 40, "Nokia 6.1": 41, "Nokia 3.1 plus": 42,
                 "Nokia 7 plus": 43, "Oneplus 6T": 44, "Oneplus 6": 45, "Oneplus 5T": 46,
                 "Oneplus 5": 47, "Oneplus 3T": 48, "Oneplus 3": 49, "Oneplus X": 50, "Oneplus Two": 51,
                 "Oneplus One": 52, "Oppo R15 pro": 53, "Oppo R17": 54, "Oppo R17 pro": 55,
                 "Oppo A7": 56, "Oppo F9": 57, "Oppo A5": 58, "Oppo F9 pro": 59, "Oppo A3s": 60}

name_of_products = ["Redmi Note 4", "Redmi Note 5", "Redmi 4", "Redmi 4A", "Redmi Note 6", "Redmi Y1",
                    "Redmi Note 6 pro", "Redmi Note 5 pro", "Redmi A1",
                    "Redmi A2", "Samsung Galaxy A7", "Samsung Galaxy J8", "Samsung Galaxy J8 plus",
                    "Samsung Galaxy J4 plus", "Samsung Galaxy A9",
                    "Samsung Galaxy A8 star", "Samsung Galaxy S9 plus", "Samsung Galaxy On8", "Samsung Galaxy Note 9",
                    "Samsung Galaxy S8",
                    "Samsung Galaxy On6", "Samsung Galaxy J2", "iphone 4", "iphone 5", "iphone 5s", "iphone SE",
                    "iphone 6", "iphone 6s",
                    "iphone 7",
                    "iphone 7s", "iphone 8", "iphone X", "iphone Xs", "iphone Xs max", "iphone Xr", "Nokia 6.1 plus",
                    "Nokia 5.1 plus", "Nokia 8.1",
                    "Nokia 2.1", "Nokia 7.1", "Nokia 1", "Nokia 6.1", "Nokia 3.1 plus", "Nokia 7 plus", "Oneplus 6T",
                    "Oneplus 6", "Oneplus 5T",
                    "Oneplus 5", "Oneplus 3T", "Oneplus 3", "Oneplus X", "Oneplus Two", "Oneplus One", "Oppo R15 pro",
                    "Oppo R17", "Oppo R17 pro",
                    "Oppo A7", "Oppo F9", "Oppo A5", "Oppo F9 pro", "Oppo A3s"]

if __name__ == "__main__":
    with open('Dataset.csv', 'a+') as file:
        choice = 1
        day = 1
        month = 0
        temp = 0

        for i in range(12):

            day = 0
            if month < 13:
                if month == 12:
                    month = 1
                else:
                    month += 1
            else:
                month = 1

            for j in range(no_of_entries[i]):

                # temp = i

                index = random.randint(0, 60)

                print("iteration: ", i + 1)
                product_name = products_dict[name_of_products[index]]

                buy = float(map[name_of_products[index]][0])
                sell = float((map[name_of_products[index]][0]) + (map[name_of_products[index]][1]))

                # this freaking line is responsible for making our dataset uniform
                profit = map[name_of_products[index]][1]

                # let us assume that every month has 30 days exactly(!) <all credit goes to laziness>
                if day >= 31:
                    break
                else:
                    if choice == 1:
                        if day == 0:
                            day = 1
                    elif choice == 0:
                        if month < 13:
                            if day < 30:
                                day += 1
                            else:
                                day = 1
                # just to avoid unexpected crash (if by chance) while continuously pressing 0 or 1
                try:
                    choice = random.randint(0, 1)
                except ValueError:
                    print("Invalid choice! Make sure that you have entered either 1 or 0")

                file.write(
                    str(day) + "," + str(month) + "," + "18" + "," + str(product_name) + "," + str(buy) + "," + str(
                        sell) + "," + str(profit) + "\n")
