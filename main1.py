from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd


class ExpenseCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)  # Generating canvas for plotting of the graph

        self.plot_expense()

        self.df = None
        self.gbe = None
        self.buy = None  # Variable initialization

    def plot_expense(self):
        """A function to plot a bar chart from appropriate data from Data.csv for expense"""

        ax = self.figure.add_subplot(111)
        # Preparing data
        self.df = pd.read_csv('Data.csv', index_col=None)
        self.gbe = self.df.groupby(['Type', 'Product'], as_index=False)[['Quantity', 'Total_Price']].sum()
        self.buy = self.gbe[self.gbe.Type == 'Buy']
        self.buy['Total_Price'] = -self.buy['Total_Price']

        # Plotting of the bar
        # self.buy.plot.bar(x='Product', y='Total_Price',title='Product wise expenses', color='#2980b9', fontsize=12)
        ax.bar(self.buy['Product'].values, self.buy['Total_Price'].values)
        ax.set_title('Expense')
        ax.set_xlabel('Product')
        ax.set_ylabel('Expense in ₹')


class ProfitCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)  # Generating canvas for plotting of the graph

        self.plot_profit()

        self.df = None
        self.gbs = None

    def plot_profit(self):
        """A function to plot a bar chart from appropriate data from Data.csv for profit"""

        ax = self.figure.add_subplot(111)
        # Preparing data
        self.df = pd.read_csv('Data.csv', index_col=None)
        self.gbs = self.df.groupby('Product', as_index=False)[['Product', 'Total_Price']].sum()

        # Plotting of the bar
        ax.bar(self.gbs['Product'].values, self.gbs['Total_Price'].values)
        ax.set_title('Profit')
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit in ₹')
