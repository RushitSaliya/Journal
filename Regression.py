import csv
import warnings
import pandas as pd
import sklearn
from sklearn import svm
# import matplotlib.pyplot as plt
from sklearn.exceptions import ConvergenceWarning

with open("Dataset.csv", "r") as file:
    file_reader = csv.reader(file, delimiter=",")
    rows = len(list(file_reader)) - 1

data = pd.read_csv("Dataset.csv")
array_of_data = []
array_of_target = []

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=ConvergenceWarning)

for i in range(rows):
    day = data.at[i, "day"]
    month = data.at[i, "month"]
    year = data.at[i, "year"]
    product = data.at[i, "product"]
    expense = data.at[i, "expense"]
    sell = data.at[i, "sell"]

    array_of_target.insert(rows, data.at[i, "profit"])
    array_of_data.insert(rows, [day, month, year, product, expense, sell])

# print(array_of_data)
# print(array_of_target)

# print("Data: ", array_of_data[-1:])

# enc = sklearn.preprocessing.OneHotEncoder(categorical_features = [3])
# array_of_data = enc.fit_transform(array_of_data).toarray()

# print(array_of_data)
model = svm.LinearSVR()

X, y = array_of_data[:-30], array_of_target[:-30]
model.fit(X, y)

if __name__ == "__main__":
    # y_pred = clf.predict(array_of_data)
    prediction1 = model.predict(X=array_of_data[10:])
    prediction = list(
        pd.DataFrame({'month': data.iloc[10:, 1], 'profit': prediction1[:]}).groupby('month').sum().iloc[:, 0])
    print(prediction)
    print("\nPrediction: ", prediction1, "\nExpected: ", array_of_target[10:])
    # print("Accuracy: ", accuracy_score(array_of_target, y_pred))
    print("\naccuracy of the model:" + str(
        100 * sklearn.metrics.r2_score(array_of_target[:], model.predict(X=array_of_data[:]))))

    x_values = data.iloc[:, 1].unique()
    y_values = data.groupby('month').sum()
    print(list(y_values.iloc[:, 5]))
    # plt.scatter(x_values, y_values)
    # plt.plot(x_values, list(y_values.iloc[:, 5]))
    # plt.plot(x_values, prediction)
    # plt.show()
