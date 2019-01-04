from Stock import Stock
from Five_Minute_Set import Five_Minute_Set
from Time_Manager import Time_Manager

class Data_Controller:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.is_change_operation = True
        self.current_stock = None
        self.is_stock_purchased = True

        self.number_count = 0


    def handle_stock_retrieval(self, stock):
        self.current_stock = stock
        # later support added to conditional if "stock pass-over time" to FM set,
        current_five_minute_set = self.get_current_five_minute_set()
        current_five_minute_set.append(self.current_stock)


    def loop_operation_analytics(self):
        #Later support for multiple algo's and extensibility
        # if(self.is_stock_purchased):
        #     self.data_manager.operation_center.process_async_case1()
        #     # self.algo_determine_when_to_sell()
        # else:
        #     self.algo_determine_when_to_buy()
        pass

    def get_current_five_minute_set(self):
        return self.data_manager.get_time_data_set_controller().get_current_five_minute_set().get_list_stock_container()

    def get_latest_stock_from_five_minute_set(self):
        current_five_minute_set = self.get_current_five_minute_set()
        return current_five_minute_set[(len(current_five_minute_set) - 1)]


    def algo_determine_when_to_sell(self):

        stock_list = self.generate_data_set()

        # if (self.determine_pchg_time_to_sell(stock_list)):
        #     self.data_manager.sell_stock_operation()

    def algo_determine_when_to_buy(self):
        return ''

    def determine_pchg_time_to_sell(self,stock_list):
        difference = self.calculate_pchg_difference(stock_list)
        if(difference > .03):
            return True
        return False
    def calculate_pchg_difference(self,stock_list):
        #Return percentage
        return stock_list[0].get_pchg() - stock_list[1].get_pchg()

    def determine_last_difference(self,stock1,stock2):
        return stock1.get_last() - stock2.get_last()

    def set_bought_stock(self,bought_stock):
        #DM_buy association
        # bought account information
        # self.bought_stock
        self.bought_stock = bought_stock

    def get_bought_stock(self):
        # bought account information
        return self.bought_stock

    def generate_data_set(self):
        time_manager = Time_Manager()
        five_minute_data_set_store= []
        i = 0
        while(i < 10):

            five_minute_data_set = Five_Minute_Set(time_manager.get_current_epoch_time())
            stock= Stock()
            stock.set_name('A_test')
            stock.set_pchg(.01)

            five_minute_data_set.append(stock)

            five_minute_data_set_store.append(five_minute_data_set)
            i += 1
        print("generated data len", len(five_minute_data_set_store))


    def generate_five_minute_data_set(self):
        time_manager = Time_Manager()
        five_minute_data_set_store = []
        i = 0
        while (i < 12):
            five_minute_data_set = Five_Minute_Set(time_manager.get_current_epoch_time())
            stock = Stock()

            if(i == 0):
                stock.set_name('NAV')
                stock.set_last(27.38)
            if (i == 1):
                stock.set_name('NAV')
                stock.set_last(27.02)
            if (i == 2):
                stock.set_name('NAV')
                stock.set_last(26.82)
            if (i == 3):
                stock.set_name('NAV')
                stock.set_last(28.22)
            if (i == 4):
                stock.set_name('NAV')
                stock.set_last(28.07)
            if (i == 5):
                stock.set_name('NAV')
                stock.set_last(28.25)
            if (i == 6):
                stock.set_name('NAV')
                stock.set_last(28.33)
            if (i == 7):
                stock.set_name('NAV')
                stock.set_last(28.30)
            if (i == 8):
                stock.set_name('NAV')
                stock.set_last(28.34)
            if (i == 9):
                stock.set_name('NAV')
                stock.set_last(28.16)
            if (i == 10):
                stock.set_name('NAV')
                stock.set_last(28.40)
            if (i == 11):
                stock.set_name('NAV')
                stock.set_last(28.37)

            five_minute_data_set.get_list_stock_container().append(stock)
            i += 1
        return five_minute_data_set_store