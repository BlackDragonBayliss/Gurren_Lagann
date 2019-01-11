from Top_Stock_Composite import Top_Stock_Composite
from Stock_Composite import Stock_Composite


class Stock_Composite_Manager:
    def __init__(self):
        self.sym = ''
        self.generation_iteration = 0
        self.stock_composite_list = []

    def get_listStocks(self):
        return self.listStocks

    def get_sym(self):
        return self.sym

    def set_sym(self, sym):
        self.sym = sym

    def get_generationIteration(self):
        return self.generationIteration

    def set_generationIteration(self, generationIteration):
        self.generationIteration = generationIteration

    def create_stock_composite(self, symbol):
        stock_composite = Stock_Composite(symbol)
        stock_composite.set_generation_iteration(self.generation_iteration)
        self.stock_composite_list.append(stock_composite)
        return stock_composite
