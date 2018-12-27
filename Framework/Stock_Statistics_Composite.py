from Stock_Statistics import Stock_Statistics

class Stock_Statistics_Composite:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.stat_composite = []
            self.chosen_index = None
        return self.__instance

    def create_stat(self,sym,pchg,last,spread,list_date):
        self.stat_composite.append([sym,pchg,last,spread,list_date])
    def get_stat_composite(self):
        return self.stat_composite

    def set_chosen_index(self,index):
        self.chosen_index = index
    def get_chosen_index(self):
        return self.chosen_index
    def get_chosen_stock_statistics(self):
        return self.stat_composite[self.get_chosen_index()]

    def clear_stat_composite(self):
        self.stat_composite.clear()