class Request_Factory:
    def __init__(self):
        ''

    def query_stock_symbol(self, name):
        json_request = {"request_type": "query_stock",
                        "name": name
                        }
        return json_request

    # Top Stock
    def lookup_top_stocks_phase_internal(self):
        json_request = {"request_type": "lookup_top_stocks_phase1",
                        "data": 'init'
                        }
        return json_request

    def lookup_top_stocks_phase2(self, data_list):
        json_request = {"request_type": "lookup_top_stocks_phase2",
                        "data_list": data_list
                        }
        return json_request

    def async_post_node_manager_query(self, name):
        json_request = {"request_type": "NM_query_stock",
                        "name": name
                        }
        return json_request

    # Bird messenger service
    def async_bird_messenger_top_stock_process_complete(self):
        json_request = {"request_type": "bird_messenger_query_money_machine",
                        "isTopStockResponse": "1"
                        }
        return json_request


    def async_post_stock_statistics_composite(self, stock_statistics_composite):
        chosen_stock_stat = stock_statistics_composite.get_chosen_stock_statistics()
        sym = chosen_stock_stat.get_sym()
        pchg = chosen_stock_stat.get_pchg()
        last = chosen_stock_stat.get_last()
        spread = chosen_stock_stat.get_spread()
        list_date = chosen_stock_stat.get_list_date()
        json_request = {"request_type": "stock_statistics",
                        "sym": sym,
                        "pchg": pchg,
                        "last": last,
                        "spread": spread,
                        "list_date": list_date
                        }
        return json_request

    def async_post_data_manager_action(self, data_manager_action):
        # chosen_stock_stat = data_manager_action.get_chosen_stock_statistics()
        # Support for sell field updates
        sym = data_manager_action.get_sym()
        pchg = data_manager_action.get_pchg()
        last = data_manager_action.get_last()
        spread = data_manager_action.get_spread()
        list_date = data_manager_action.get_list_date()
        json_request = {"request_type": "store_data_manager_action",
                        "sym": sym,
                        "pchg": pchg,
                        "last": last,
                        "spread": spread,
                        "list_date": list_date
                        }
        return json_request

    def lookup_top_stocks_phase3(self, top_stock_composite):

        data_list = []

        name1 = ''
        pchg1 = 0
        pcls1 = 0
        last1 = 0
        bid1 = 0
        ask1 = 0
        name2 = ''
        pchg2 = 0
        pcls2 = 0
        last2 = 0
        bid2 = 0
        ask2 = 0
        name3 = ''
        pchg3 = 0
        pcls3 = 0
        last3 = 0
        bid3 = 0
        ask3 = 0

        index_composite = 0
        for stock_composite in top_stock_composite.get_list_stock_composites():

            if (index_composite == 0):
                stock = stock_composite.get_list_stocks()[0]
                # List of values added to list
                name1 = stock.get_name()
                pchg1 = stock.get_pchg()
                pcls1 = stock.get_pcls()
                last1 = stock.get_last()
                bid1 = stock.get_bid()
                ask1 = stock.get_ask()

            if (index_composite == 1):
                stock = stock_composite.get_list_stocks()[0]
                # List of values added to list
                name2 = stock.get_name()
                pchg2 = stock.get_pchg()
                pcls2 = stock.get_pcls()
                last2 = stock.get_last()
                bid2 = stock.get_bid()
                ask2 = stock.get_ask()

            if (index_composite == 2):
                stock = stock_composite.get_list_stocks()[0]
                # List of values added to list
                name3 = stock.get_name()
                pchg3 = stock.get_pchg()
                pcls3 = stock.get_pcls()
                last3 = stock.get_last()
                bid3 = stock.get_bid()
                ask3 = stock.get_ask()

            index_composite += 1

        json_request = {
            "request_type": "lookup_top_stocks_phase3",
            "name1": name1,
            "pchg1": pchg1,
            "pcls1": pcls1,
            "last1": last1,
            "bid1": bid1,
            "ask1": ask1,
            "name2": name2,
            "pchg2": pchg2,
            "pcls2": pcls2,
            "last2": last2,
            "bid2": bid2,
            "ask2": ask2,
            "name3": name3,
            "pchg3": pchg3,
            "pcls3": pcls3,
            "last3": last3,
            "bid3": bid3,
            "ask3": ask3,
        }
        return json_request

    def async_query_stock(self, symbol):
        json_request = {"request_type": "query_stock_phase2",
                        "name": symbol
                        }
        return json_request

    def async_post_stock_query_phase1(self, stock_composite):

        data_list = []

        name = ''
        pchg = 0
        pcls = 0
        last = 0
        bid = 0
        ask = 0

        index_composite = 0
        stock = stock_composite.get_list_stocks()[0]
        # List of values added to list
        name = stock.get_name()
        pchg = stock.get_pchg()
        pcls = stock.get_pcls()
        last = stock.get_last()
        bid = stock.get_bid()
        ask = stock.get_ask()

        index_composite += 1

        json_request = {"request_type": "query_stock_phase2",
                        "name": name,
                        "pchg": pchg,
                        "pcls": pcls,
                        "last": last,
                        "bid": bid,
                        "ask": ask,
                        }
        return json_request

    # Account
    def async_post_account_information_phase1(self, stock_composite):

        data_list = []

        name = ''
        pchg = 0
        pcls = 0
        last = 0
        bid = 0
        ask = 0

        index_composite = 0
        stock = stock_composite.get_list_stocks()[0]
        # List of values added to list
        name = stock.get_name()
        pchg = stock.get_pchg()
        pcls = stock.get_pcls()
        last = stock.get_last()
        bid = stock.get_bid()
        ask = stock.get_ask()

        index_composite += 1

        json_request = {"request_type": "query_account_information_phase1",
                        "name": name,
                        "pchg": pchg,
                        "pcls": pcls,
                        "last": last,
                        "bid": bid,
                        "ask": ask,
                        }
        return json_request

    def async_post_account_information_phase2(self, account_information):

        dataList = []

        balance = 0

        index_composite = 0
        balance = account_information.get_balance()
        print(balance)
        # List of values added to list

        index_composite += 1

        json_request = {"request_type": "query_account_information_phase2",
                        "balance": balance
                        }
        return json_request

    # Buy
    def async_post_market_buy_phase1(self, data):
        json_request = {
            "request_type": "trade_market_buy_phase2",
            "data": data
            # "payload":{
            #     "data": data
            # }
        }
        return json_request

    def async_post_market_buy_phase2(self, stock):
        data_list = []

        balance = 0

        name = stock.get_name()
        pchg = stock.get_pchg()
        pcls = stock.get_pcls()
        last = stock.get_last()
        bid = stock.get_bid()
        ask = stock.get_ask()

        # indexComposite += 1
        # print(name)
        json_request = {
            "request_type": "trade_market_buy_phase3",
            "name": name,
            "pchg": pchg,
            "pcls": pcls,
            "last": last,
            "bid": bid,
            "ask": ask
        }
        return json_request

    def async_post_market_buy_phase3(self, account_information):
        data_list = []

        balance = 0

        index_composite = 0
        balance = account_information.get_balance()
        print(balance)
        # List of values added to list

        index_composite += 1

        json_request = {"request_type": "trade_market_buy_phase4",
                        "balance": balance
                        }
        return json_request

    # Sell
    def async_post_market_sell_phase1(self, data):
        json_request = {"request_type": "trade_market_sell_phase2",
                        "data": data
                        }
        return json_request

    def async_post_market_sell_phase2(self, DM_Action):
        data_list = []

        name = ''
        pchg = 0
        pcls = 0
        last = 0
        bid = 0
        ask = 0

        index_composite = 0
        # stock = stockComposite.get_listStocks()[0]
        # List of values added to list
        name = DM_Action.get_name()
        is_day_trade = DM_Action.get_is_day_trade()
        price_bought_actual = DM_Action.get_price_bought_actual()
        price_sold_actual = DM_Action.get_price_sold_actual()
        price_bought_estimate = DM_Action.get_price_bought_estimate()
        price_sold_estimate = DM_Action.get_price_sold_estimate()
        pchg_bought_actual = DM_Action.get_pchg_bought_actual()
        pchg_sold_actual = DM_Action.get_pchg_sold_actual()
        pchg_bought_estimate = DM_Action.get_pchg_bought_estimate()
        pchg_sold_estimate = DM_Action.get_pchg_sold_estimate()
        epoch_of_trade = DM_Action.get_epoch_of_trade()

        index_composite += 1

        json_request = {
            "request_type": "trade_market_sell_phase3",
            "name": name,
            "is_day_trade": is_day_trade,
            "epoch_of_trade": epoch_of_trade,
            "price_bought_actual": price_bought_actual,
            "price_sold_actual": price_sold_actual,
            "price_bought_estimate": price_bought_estimate,
            "price_sold_estimate": price_sold_estimate,
            "pchg_bought_actual": pchg_bought_actual,
            "pchg_sold_actual": pchg_sold_actual,
            "pchg_bought_estimate": pchg_bought_estimate,
            "pchg_sold_estimate": pchg_sold_estimate
        }
        return json_request

    def async_post_market_sell_phase3(self, stock):
        data_list = []

        name = ''
        pchg = 0
        pcls = 0
        last = 0
        bid = 0
        ask = 0

        index_composite = 0
        # stock = stockComposite.get_listStocks()[0]
        # List of values added to list
        name = stock.get_name()
        pchg = stock.get_pchg()
        pcls = stock.get_pcls()
        last = stock.get_last()
        bid = stock.get_bid()
        ask = stock.get_ask()

        index_composite += 1

        json_request = {"request_type": "trade_market_sell_phase3",
                        "name": name,
                        "pchg": pchg,
                        "pcls": pcls,
                        "last": last,
                        "bid": bid,
                        "ask": ask,
                        }
        return json_request

    def top_stock_pull(self):
        json_request = {
            "request_type": "get_top_stocks"
        }
        return json_request

    def top_stocks_post_DB(self, json):
        json_request = json
        print(json_request)
