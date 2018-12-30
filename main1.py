from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Product wise expense"
        top = 400
        left = 400
        width = 900
        height = 500

        # icon = "icon.png"

        self.setWindowTitle(title)
        self.setGeometry(top,left, width, height)
        # self.setWindowIcon(QIcon("icon.png"))

        self.MyUI()


    def MyUI(self):
        
        canvas = ExpenseCanvas(self, width=8, height=5)
        canvas.move(0,0)


class ExpenseCanvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FingureCanvas.__init__(self, fig)
        self.setParent(parent)                                     #Generating canvas for plotting of the graph

        self.plot_expense()

        self.df = None
        self.gbe = None
        self.buy = None                           #Variable intialization

    def plot_expense(self):
        """A function to plot a bar chart from appropriate data from Data.csv for expense"""

        ax = self.figure.add_subplot(111)
        #Preparing data
        self.df = pd.read_csv('Data.csv', index_col=None)
        self.gbe = self.df.groupby(['Type', 'Product'], as_index = False)[['Quantity', 'Total_Price']].sum()
        self.buy = self.gbe[self.gbe.Type == 'Buy']
        self.buy['Total_Price'] = -self.buy['Total_Price']

        #Plotting of the bar
        # self.buy.plot.bar(x='Product', y='Total_Price',title='Product wise expenses', color='#2980b9', fontsize=12)
        ax.bar(self.buy['Product'].values, self.buy['Total_Price'].values)
        ax.set_title('Product wise expense')
        ax.set_xlabel('Product')
        ax.set_ylabel('Expense in ₹')
        



class ProfitCanvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FingureCanvas.__init__(self, fig)
        self.setParent(parent)                                     #Generating canvas for plotting of the graph

        self.plot_expense()

        self.df = None
        self.gbs = None

    def plot_profit(self):
        """A function to plot a bar chart from appropriate data from Data.csv for profit"""

        ax = self.figure.add_subplot(111)
        #Preparing data
        self.df = pd.read_csv('Data.csv', index_col=None)
        self.gbs = self.df.groupby('Product', as_index = False)[['Product', 'Total_Price']].sum()

        #Plotting of the bar
        ax.bar(self.gbs['Product'].values, self.gbs['Total_Price'].values)
        ax.set_title('Product wise profit')
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit in ₹')
        
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()