from Stock import Stock


class Top_Stock_Monument_Composite:


    def __init__(self):
        self.json_top_stocks = {}
        self.list_top_stocks = []
        self.list_chosen_stocks = []
        self.list_top_stocks_json = []
        self.list_stock_commposites = []
        self.current_count = 0;
        self.current_count_calc_highest = 0
        self.chosen_top_stock_val1 = 0.0;
        self.chosen_top_stock_val2 = 0.0;
        self.chosen_top_stock_val3 = 0.0;
        self.chosen_top_stock_count1 = 0;
        self.chosen_top_stock_count2 = 0;
        self.chosen_top_stock_count3 = 0;


    def set_highest_chosen(self):
        print(self.json_top_stocks.items())
        for key, value in self.json_top_stocks.items():
            if key == "data_set":
                self.list_top_stocks_json = value
        for val in self.list_top_stocks_json:
            self.top_stock = Stock()
            for key, value in val.items():
                if key == 'symbol':
                    self.top_stock.set_name(value)
                if key == 'pchg':
                    self.top_stock.set_pchg(value)
                if key == 'pcls':
                    self.top_stock.set_pcls(value)
                if key == 'last':
                    self.top_stock.set_last(value)
            self.list_top_stocks.append(self.top_stock)
            print("length in set_highest "+str(len(self.list_top_stocks)))

    def calc_highest_chosen(self):
        # print(self.listTopStocks)
        for val in self.list_top_stocks:
            sym = val.get_name()
            pchg = float(val.get_pchg())

            if (float(pchg) > self.chosen_top_stock_val3):
                self.chosen_top_stock_val3 = pchg
                self.chosen_top_stock_count3 = self.current_count_calc_highest
            if (pchg > self.chosen_top_stock_val2):
                self.chosen_top_stock_val3 = self.chosen_top_stock_val2
                self.chosen_top_stock_count3 = self.chosen_top_stock_count2
                self.chosen_top_stock_val2 = pchg
                self.chosen_top_stock_count2 = self.current_count_calc_highest
            if (pchg > self.chosen_top_stock_val1):
                self.chosen_top_stock_val2 = self.chosen_top_stock_val1
                self.chosen_top_stock_count2 = self.chosen_top_stock_count1
                self.chosen_top_stock_val1 = pchg
                self.chosen_top_stock_count1 = self.current_count_calc_highest

            self.current_count_calc_highest = (self.current_count_calc_highest + 1);

    def collect_top_stock_results_in_list(self):
        # print(len(self.listChosenStocks))
        print(len(self.list_top_stocks))
        print(self.chosen_top_stock_count1)
        print(self.chosen_top_stock_count2)
        print(self.chosen_top_stock_count3)

        chosen_object1 = self.list_top_stocks[self.chosen_top_stock_count1]
        chosen_object2 = self.list_top_stocks[self.chosen_top_stock_count2]
        chosen_object3 = self.list_top_stocks[self.chosen_top_stock_count3]
        self.list_chosen_stocks.append(chosen_object1)
        self.list_chosen_stocks.append(chosen_object2)
        self.list_chosen_stocks.append(chosen_object3)
        for val in self.list_chosen_stocks:
            print(val.get_name())


    def clear_top_stocks_processing_values(self):
        print("hit clear_top_stocks")
        self.current_count = 0
        self.current_count_calc_highest = 0
        self.chosen_top_stock_val1 = 0.0
        self.chosen_top_stock_val2 = 0.0
        self.chosen_top_stock_val3 = 0.0
        self.chosen_top_stock_count1 = 0
        self.chosen_top_stock_count2 = 0
        self.chosen_top_stock_count3 = 0

        self.json_top_stocks = {}
        self.list_top_stocks = []
        self.list_chosen_stocks.clear()
        self.list_top_stocks_json.clear()
        self.list_stock_commposites.clear()

    def get_list_top_stocks(self):
        return self.list_top_stocks

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_json_top_stocks(self):
        return self.json_top_stocks

    def set_json_top_stocks(self, json):
        self.json_top_stocks = json

    def get_list_chosen_stocks(self):
        return self.list_chosen_stocks

    def set_list_chosen_stocks(self, list):
        self.list_chosen_stocks = list

    def get_list_stock_composites(self):
        return self.list_stock_commposites

    def get_specific_stock_composite_in_list(self, name):
        list_stock_composites = self.get_list_stock_composites()
        for stock_composite in list_stock_composites:
            if stock_composite.get_name() == name:
                return stock_composite
