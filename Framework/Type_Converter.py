from Stock_Composite import Stock_Composite
from Stock import Stock
from Account_Information import Account_Information
import sched, time, calendar

class Type_Converter:
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


    def top_stocks_convert_to_JSON(self, listStocks):
        self.top_stock_symbol1 = ''
        self.top_stock_symbol2 = ''
        self.top_stock_symbol3 = ''
        self.top_stock_pchg1 = ''
        self.top_stock_pchg2 = ''
        self.top_stock_pchg3 = ''
        internalCount = 0
        for val in listStocks:
            if (internalCount == 0):
                self.top_stock_symbol1 = val.get_symbol()
                self.top_stock_pchg1 = val.get_pchg()
                internalCount = (internalCount + 1)
                continue
            if (internalCount == 1):
                self.top_stock_symbol2 = val.get_symbol()
                self.top_stock_pchg2 = val.get_pchg()
                internalCount = (internalCount + 1)
                continue
            if (internalCount == 2):
                self.top_stock_symbol3 = val.get_symbol()
                self.top_stock_pchg3 = val.get_pchg()
                internalCount = (internalCount + 1)
                continue

        jsonRequest = {
            'request_type': 'store_top_stocks',
            'data_symbol': [self.top_stock_symbol1,
                            self.top_stock_symbol2,
                            self.top_stock_symbol3
                            ],
            'data_val': [self.top_stock_pchg1,
                         self.top_stock_pchg2,
                         self.top_stock_pchg3
                         ]
        }
        return jsonRequest

    def parse_stock_queries(self, str_to_parse, operation_center):
        data_set_group_0_1 = str_to_parse.split('</quotetype>')
        data_set_group_0_2 = data_set_group_0_1[1].split('</quotetype>')
        data_set_group_0_3 = data_set_group_0_2[0].split('</quotes>')
        data_set_group_0_4 = data_set_group_0_3[0].split('</quote>')
        for val in data_set_group_0_4:
            data_set_group_1_2 = val.split('<symbol>');
            data_set_group_2_2 = val.split('<pchg>');
            data_set_group_3_2 = val.split('<pcls>');
            data_set_group_4_2 = val.split('<last>');
            data_set_group_5_2 = val.split('<bid>');
            data_set_group_6_2 = val.split('<ask>');

            data_set_group_1_3 = data_set_group_1_2[1].split('</symbol');
            data_set_group_2_3 = data_set_group_2_2[1].split('</pchg');
            data_set_group_3_3 = data_set_group_3_2[1].split('</pcls');
            data_set_group_4_3 = data_set_group_4_2[1].split('</last');
            data_set_group_5_3 = data_set_group_5_2[1].split('</bid');
            data_set_group_6_3 = data_set_group_6_2[1].split('</ask');
            stock_created = Stock()
            stock_created.set_sym(str(data_set_group_1_3[0]))
            stock_created.set_pchg(float(data_set_group_2_3[0]))
            stock_created.set_pcls(float(data_set_group_3_3[0]))
            stock_created.set_last(float(data_set_group_4_3[0]))
            stock_created.set_bid(float(data_set_group_5_3[0]))
            stock_created.set_ask(float(data_set_group_6_3[0]))

            operation_center.add_stock_composite_to_top_composite(Stock_Composite(stock_created.get_sym()))
            top_stock_composite = operation_center.get_top_stock_composite()
            stock_composite = top_stock_composite.get_specific_stock_composite_in_list(stock_created.get_sym())
            stock_composite.get_list_stocks().append(stock_created)

    def parse_stock_query(self, str_to_parse):
        data_set_group_1_2 = str_to_parse.split('<symbol>');
        data_set_group_2_2 = str_to_parse.split('<pchg>');
        data_set_group_3_2 = str_to_parse.split('<pcls>');
        data_set_group_4_2 = str_to_parse.split('<last>');
        data_set_group_5_2 = str_to_parse.split('<bid>');
        data_set_group_6_2 = str_to_parse.split('<ask>');

        data_set_group_1_3 = data_set_group_1_2[1].split('</symbol');
        data_set_group_2_3 = data_set_group_2_2[1].split('</pchg');
        data_set_group_3_3 = data_set_group_3_2[1].split('</pcls');
        data_set_group_4_3 = data_set_group_4_2[1].split('</last');
        data_set_group_5_3 = data_set_group_5_2[1].split('</bid');
        data_set_group_6_3 = data_set_group_6_2[1].split('</ask');

        stock_created = Stock()

        stock_created.set_sym(data_set_group_1_3[0])
        stock_created.set_pchg(data_set_group_2_3[0])
        stock_created.set_pcls(data_set_group_3_3[0])
        stock_created.set_last(data_set_group_4_3[0])
        stock_created.set_bid(data_set_group_5_3[0])
        stock_created.set_ask(data_set_group_6_3[0])
        return stock_created

    def parse_symbol_query(self, str_to_parse):
        data_set_group_1_2 = str_to_parse.split('<symbol>');
        data_set_group_2_2 = str_to_parse.split('<pchg>');
        data_set_group_3_2 = str_to_parse.split('<pcls>');
        data_set_group_4_2 = str_to_parse.split('<last>');
        data_set_group_5_2 = str_to_parse.split('<bid>');
        data_set_group_6_2 = str_to_parse.split('<ask>');

        data_set_group_1_3 = data_set_group_1_2[1].split('</symbol');
        data_set_group_2_3 = data_set_group_2_2[1].split('</pchg');
        data_set_group_3_3 = data_set_group_3_2[1].split('</pcls');
        data_set_group_4_3 = data_set_group_4_2[1].split('</last');
        data_set_group_5_3 = data_set_group_5_2[1].split('</bid');
        data_set_group_6_3 = data_set_group_6_2[1].split('</ask');

        stock_created = Stock()

        stock_created.set_sym(data_set_group_1_3[0])
        stock_created.set_pchg(data_set_group_2_3[0])
        stock_created.set_pcls(data_set_group_3_3[0])
        stock_created.set_last(data_set_group_4_3[0])
        stock_created.set_bid(data_set_group_5_3[0])
        stock_created.set_ask(data_set_group_6_3[0])

        return stock_created

    def parse_account_information(self, str_to_parse):
        data_set_group_1_2 = str_to_parse.split('<cash>');

        data_set_group_1_3 = data_set_group_1_2[1].split('</cash');

        account_information = Account_Information()
        account_information.set_balance(data_set_group_1_3[0])
        return account_information

    def parse_market_buy(self, str_to_parse, DM_Action_instance):
        #Will accept and parse stock query.
        #Store last, bid
        data_set_group_1_2 = str_to_parse.split('<symbol>');
        data_set_group_2_2 = str_to_parse.split('<pchg>');
        data_set_group_3_2 = str_to_parse.split('<pcls>');
        data_set_group_4_2 = str_to_parse.split('<last>');
        data_set_group_5_2 = str_to_parse.split('<bid>');
        data_set_group_6_2 = str_to_parse.split('<ask>');

        data_set_group_1_3 = data_set_group_1_2[1].split('</symbol');
        data_set_group_2_3 = data_set_group_2_2[1].split('</pchg');
        data_set_group_3_3 = data_set_group_3_2[1].split('</pcls');
        data_set_group_4_3 = data_set_group_4_2[1].split('</last');
        data_set_group_5_3 = data_set_group_5_2[1].split('</bid');
        data_set_group_6_3 = data_set_group_6_2[1].split('</ask');

        DM_Buy_instance = DM_Buy()

        DM_Buy_instance.set_name(data_set_group_1_3[0])
        DM_Buy_instance.set_pchg(data_set_group_2_3[0])
        DM_Buy_instance.set_pcls(data_set_group_3_3[0])
        DM_Buy_instance.set_last(data_set_group_4_3[0])
        DM_Buy_instance.set_bid(data_set_group_5_3[0])
        DM_Buy_instance.set_ask(data_set_group_6_3[0])
        ts = time.time()
        current_time = time.localtime(ts)

        DM_Buy_instance.set_epoch_of_trade(calendar.timegm(time.gmtime()))
        DM_Action_instance.set_DM_Buy(DM_Buy_instance)
        DM_Action_instance.set_name(data_set_group_1_3[0])

        return DM_Buy_instance

    def parse_DM_Action(self, str_to_parse, DM_Action_instance):
        data_set_group_1_2 = str_to_parse.split('<symbol>');
        data_set_group_2_2 = str_to_parse.split('<pchg>');
        data_set_group_3_2 = str_to_parse.split('<pcls>');
        data_set_group_4_2 = str_to_parse.split('<last>');
        data_set_group_5_2 = str_to_parse.split('<bid>');
        data_set_group_6_2 = str_to_parse.split('<ask>');

        data_set_group_1_3 = data_set_group_1_2[1].split('</symbol');
        data_set_group_2_3 = data_set_group_2_2[1].split('</pchg');
        data_set_group_3_3 = data_set_group_3_2[1].split('</pcls');
        data_set_group_4_3 = data_set_group_4_2[1].split('</last');
        data_set_group_5_3 = data_set_group_5_2[1].split('</bid');
        data_set_group_6_3 = data_set_group_6_2[1].split('</ask');

        sell_stock_instance = Stock()

        sell_stock_instance.set_sym(data_set_group_1_3[0])
        sell_stock_instance.set_pchg(data_set_group_2_3[0])
        sell_stock_instance.set_pcls(data_set_group_3_3[0])
        sell_stock_instance.set_last(data_set_group_4_3[0])
        sell_stock_instance.set_bid(data_set_group_5_3[0])
        sell_stock_instance.set_ask(data_set_group_6_3[0])


        # Set buy information into DM_Action
        DM_Buy_instance = DM_Action_instance.get_DM_Buy()

        DM_Action_instance.set_is_day_trade(True)
        # ts = time.time()
        # currentTime = time.localtime(ts)
        DM_Action_instance.set_epoch_of_trade(DM_Buy_instance.get_epoch_of_trade())

        #Estimate will be recorded upon buy. and internal metrics.
        #Estimate - actual.
        # input_value =  (float(DM_Buy_instance.get_last()) - float(stockCreated.get_last()))
        # DM_Action_instance.set_price_bought_actual(input_value)

        DM_Action_instance.set_price_bought_actual(DM_Buy_instance.get_last())
        # DM_Action_instance.set_price_bought_actual(555)
        DM_Action_instance.set_price_sold_actual(sell_stock_instance.get_last())

        print(DM_Action_instance.get_price_bought_actual())

        # price_bought_estimate: {
        #     type: String,
        #     required: true
        # },
        # price_sold_estimate: {
        #     type: String,
        #     required: true
        # },
        DM_Action_instance.set_price_bought_estimate(DM_Buy_instance.get_last())
        DM_Action_instance.set_price_sold_estimate(sell_stock_instance.get_last())

        # pchg_bought_actual: {
        #     type: String,
        #     required: true
        # },
        # pchg_sold_actual: {
        #     type: String,
        #     required: true
        # },
        DM_Action_instance.set_pchg_bought_actual(DM_Buy_instance.get_pchg())
        DM_Action_instance.set_pchg_sold_actual(sell_stock_instance.get_pchg())

        # pchg_bought_estimate: {
        #     type: String,
        #     required: true
        # },
        # pchg_sold_estimate: {
        #     type: String,
        #     required: true
        # },
        DM_Action_instance.set_pchg_bought_estimate(DM_Buy_instance.get_pchg())
        DM_Action_instance.set_pchg_sold_estimate(sell_stock_instance.get_pchg())


        return DM_Action_instance


    def set_highest_chosen(self):
        print(self.json_top_stocks.items())
        for key, value in self.json_top_stocks.items():
            if key == "data_set":
                self.list_top_stocks_json = value
                # print(self.list_top_stocks_json)
        for val in self.list_top_stocks_json:
            self.top_stock = Stock()
            is_applicable_stock = True
            for key, value in val.items():
                if key == 'symbol':
                    #if symbol cotains non-alphabetic characters, continue
                    if ("." in value):
                        print("value", value, "contains a .'")
                        is_applicable_stock = False
                        break
                    if ("\'" in value):
                        print("value", value, "contains a .'")
                        is_applicable_stock = False
                        break
                    self.top_stock.set_sym(value)
                if key == 'pchg':
                    self.top_stock.set_pchg(value)
                if key == 'pcls':
                    self.top_stock.set_pcls(value)
                if key == 'last':
                    self.top_stock.set_last(value)

            if(is_applicable_stock):
                self.list_top_stocks.append(self.top_stock)
            # print("length in set_highest "+str(len(self.list_top_stocks)))

    def calc_highest_chosen(self):
        # print(self.listTopStocks)
        for val in self.list_top_stocks:
            sym = val.get_sym()
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
        print("length top stocks",len(self.list_top_stocks))
        print("count1",self.chosen_top_stock_count1)
        print("count2",self.chosen_top_stock_count2)
        print("count3",self.chosen_top_stock_count3)

        chosen_object1 = self.list_top_stocks[self.chosen_top_stock_count1]
        chosen_object2 = self.list_top_stocks[self.chosen_top_stock_count2]
        chosen_object3 = self.list_top_stocks[self.chosen_top_stock_count3]
        self.list_chosen_stocks.append(chosen_object1)
        self.list_chosen_stocks.append(chosen_object2)
        self.list_chosen_stocks.append(chosen_object3)
        for val in self.list_chosen_stocks:
            print(val.get_sym())


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

    def get_specific_stock_composite_in_list(self, sym):
        list_stock_composites = self.get_list_stock_composites()
        for stock_composite in list_stock_composites:
            if stock_composite.get_sym() == sym:
                return stock_composite
    def reset_instance_values(self):
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