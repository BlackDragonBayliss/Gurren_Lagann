import Stock


class Stock_Composite:


    def __init__(self,name):
        self.name = name
        self.list_stocks = []
    def get_list_stocks(self):
        return self.listStocks

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_generation_iteration(self):
        return self.generationIteration
    def set_generation_iteration(self,generationIteration):
        self.generationIteration = generationIteration

    def get_list_stocks(self):
        return self.list_stocks


    # def action2(self, *args ):
    #     print(args)
    #     count = 0
    #     for arg in args:
    #         print(count)
    #         if(count==0):
    #             param1 = arg
    #         if(count==1):
    #             param2 = arg
    #         count = count+1
    #     self.chaosFunction(param1,param2)
    # def chaosFunction(self,stockComposite,intToAdd):
    #     print(stockComposite.get_name())
    #     print(intToAdd)

