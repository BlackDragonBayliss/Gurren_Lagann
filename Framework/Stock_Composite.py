
class Stock_Composite:
    def __init__(self, sym):
        self.sym = sym
        self.list_stocks = []

    def get_list_stocks(self):
        return self.listStocks

    def get_sym(self):
        return self.sym

    def set_sym(self, sym):
        self.sym = sym

    def get_generation_iteration(self):
        return self.generationIteration

    def set_generation_iteration(self, generationIteration):
        self.generationIteration = generationIteration

    def get_list_stocks(self):
        return self.list_stocks
