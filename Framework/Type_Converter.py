from Stock_Composite import Stock_Composite
from Stock import Stock
from Account_Information import Account_Information
from DM_Buy import DM_Buy
import sched, time
import calendar

class Type_Converter:
    def __init__(self):
        self.name = ''

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
        # Split strToParse into stock results, store in stockResultsList
        data_set_group_0_1 = str_to_parse.split('</quotetype>')
        data_set_group_0_2 = data_set_group_0_1[1].split('</quotetype>')
        data_set_group_0_3 = data_set_group_0_2[0].split('</quotes>')
        data_set_group_0_4 = data_set_group_0_3[0].split('</quote>')
        data_set_group_0_4 = data_set_group_0_4[:-1]
        # Luck is the religion of fools.
        # index1 = 0
        for val in data_set_group_0_4:
            # print('index '+str(index1))
            # index1 += 1
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
            stock_created.set_name(str(data_set_group_1_3[0]))
            stock_created.set_pchg(float(data_set_group_2_3[0]))
            stock_created.set_pcls(float(data_set_group_3_3[0]))
            stock_created.set_last(float(data_set_group_4_3[0]))
            stock_created.set_bid(float(data_set_group_5_3[0]))
            stock_created.set_ask(float(data_set_group_6_3[0]))

            # Create stockcomposite synced with symbol
            # operationCenter.add_stock_composite_to_top_composite(operationCenter.generate_stock_composite(stockCreated.get_symbol()))

            operation_center.add_stock_composite_to_top_composite(Stock_Composite(stock_created.get_name()))
            # Handle topStockComposite
            top_stock_composite = operation_center.get_top_stock_composite()
            # Handle stockComposite
            # print(stockCreated.get_symbol())
            stock_composite = top_stock_composite.get_specific_stock_composite_in_list(stock_created.get_name())
            # stockComposite = topStockComposite.get_listStockComposites()[0]
            # print(stockComposite.get_listStocks())
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

        stock_created.set_name(data_set_group_1_3[0])
        stock_created.set_pchg(data_set_group_2_3[0])
        stock_created.set_pcls(data_set_group_3_3[0])
        stock_created.set_last(data_set_group_4_3[0])
        stock_created.set_bid(data_set_group_5_3[0])
        stock_created.set_ask(data_set_group_6_3[0])

        # stock_composite = composite_manager.create_stock_composite(stock_created.get_name())
        #
        # stock_composite.get_list_stocks().append(stock_created)
        #we want to beind a stockcomposite

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

        stock_created.set_name(data_set_group_1_3[0])
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

        # print(account_information.get_balance())

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

        sell_stock_instance.set_name(data_set_group_1_3[0])
        sell_stock_instance.set_pchg(data_set_group_2_3[0])
        sell_stock_instance.set_pcls(data_set_group_3_3[0])
        sell_stock_instance.set_last(data_set_group_4_3[0])
        sell_stock_instance.set_bid(data_set_group_5_3[0])
        sell_stock_instance.set_ask(data_set_group_6_3[0])


        # Set buy information into DM_Action
        DM_Buy_instance = DM_Action_instance.get_DM_Buy()

        # DM_Action_instance.set_name(sell_stock_instance.get_name())
        # DM_Buy_instance
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