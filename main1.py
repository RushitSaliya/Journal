#importing required moduls
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd


class ExpenseCanvas(FigureCanvas):
    """A child which inherits lots of behaviours from parent to generate graph canvas 🙂"""

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        """Well, that is where child uses inherited behaviours for his one and only aim of his life, embedding graph to canvas indeed !!😄"""

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        #And here he is done with his task 😌
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)  
        self.plot_expense()

        #Variables which are yet to assign with their values
        self.df = None
        self.gbe = None
        self.buy = None  

    def plot_expense(self):
        """"One and only aim of this method is to serve a beutiful graph made with all processed ingredients 🤩"""

        ax = self.figure.add_subplot(111)

        # Here, all the chopping of vegetables happen to cook a dish 
        self.df = pd.read_csv('Data.csv', index_col=None)
        self.gbe = self.df.groupby(['Type', 'Product'], as_index=False)[['Quantity', 'Total_Price']].sum()
        self.buy = self.gbe[self.gbe.Type == 'Buy']
        self.buy['Total_Price'] = -self.buy['Total_Price']

        #And here all the processed ingredients gone to the hands of cook(matplotlib).
        ax.bar(self.buy['Product'].values, self.buy['Total_Price'].values)
        ax.set_title('Expense')
        ax.set_xlabel('Product')
        ax.set_ylabel('Expense in ₹')


class ProfitCanvas(FigureCanvas):
    """Well come to the class were we show employer his own diligence, a profit graph indeed !!😌"""

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        """Have nothing to say..After explaining same for the ExpenseCanvas 🙂"""

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)  

        self.plot_profit()

        self.df = None
        self.gbs = None

    def plot_profit(self):
        """One and only task of this method is to make employer happy by showing him a visual representation of his diligence !!🤗"""

        ax = self.figure.add_subplot(111)

        # And here it collects and form data required to plot a graph
        self.df = pd.read_csv('Data.csv', index_col=None)
        self.gbs = self.df.groupby('Product', as_index=False)[['Product', 'Total_Price']].sum()

        # Handed on to the master for creating graph
        ax.bar(self.gbs['Product'].values, self.gbs['Total_Price'].values)
        ax.set_title('Profit')
        ax.set_xlabel('Product')
        ax.set_ylabel('Profit in ₹')

