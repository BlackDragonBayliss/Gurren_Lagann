import asyncio
from threading import Thread


class Data_Manager_Request_Bundler:
    __instance = None

    def __new__(self, sym):
        self.sym = sym
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.operation_center = None

    def set_operation_center(self, operation_center):
        self.operation_center = operation_center


    def process_stock_store(self, time_data_set_manager, stock):

        edited_request = self.process_changeover_request(time_data_set_manager)

        time_data_set_manager.isSetChangeOverSinceLast()

        time_data_set_manager.calculate_hour_change()
        time_data_set_manager.calculate_ten_minute_change()
        time_data_set_manager.calculate_five_minute_change()


    def process_changeover_request(self, time_data_set_manager):
        # time_data_set_manager.calculate_hour_change()
        # time_data_set_manager.calculate_ten_minute_change()
        # time_data_set_manager.calculate_five_minute_change()

        if (time_data_set_manager.calculate_hour_change()):
            pass

    # def validate_chosen_data_manager_dictionary(self, conditional_dictionary):
    #     temporary_value_list = []
    #     for key in conditional_dictionary:
    #         print(conditional_dictionary[key])
    #         temporary_value_list.append(conditional_dictionary[key])
    #     # If False positive exists in conditional list, then clear stock list
    #     if False in temporary_value_list:
    #         print("clearing stock list")
    #         self.chosen_stock_temp_container.clear()
    #     else:
    #         print("creating request")
    #         json = self.create_request_bundle()
    #         self.post_request_bundle(json)
    #
    # def create_request_bundle(self):
    #     stock1 = self.chosen_stock_temp_container[0]
    #     stock2 = self.chosen_stock_temp_container[1]
    #     stock3 = self.chosen_stock_temp_container[2]
    #
    #
    #     stock
    #     json = {
    #         # "stock_symbol_1": stock1.get_sym(),
    #         # "stock_last_1": stock1.get_last(),
    #         # "stock_pchg_1": stock1.get_pchg(),
    #         # "stock_bid_1": stock1.get_bid(),
    #         # "stock_ask_1": stock1.get_ask(),
    #         #
    #         # "stock_symbol_2": stock2.get_sym(),
    #         # "stock_last_2": stock2.get_last(),
    #         # "stock_pchg_2": stock2.get_pchg(),
    #         # "stock_bid_2": stock2.get_bid(),
    #         # "stock_ask_2": stock2.get_ask(),
    #         #
    #         # "stock_symbol_3": stock3.get_sym(),
    #         # "stock_last_3": stock3.get_last(),
    #         # "stock_pchg_3": stock3.get_pchg(),
    #         # "stock_bid_3": stock3.get_bid(),
    #         # "stock_ask_3": stock3.get_ask()
    #         "request_type": "data_manager_request_bundle",
    #         "isGetLatestHourSet": 1,
    #         "isGetLatestTenMinuteSet": 0,
    #         "isGetLatestFiveMinuteSet": 0,
    #         "isGetLatestStockSet": 0,
    #
    #         "dataBundleRecordSetInitiation": 0,
    #         "dataBundleDaySetInitiation": 0,
    #         "isHourChangeover": 0,
    #         "isTenMinuteChangeover": 0,
    #         "isFiveMinuteChangeover": 0,
    #         "isStockStore": 0,
    #
    #
    #         "stock_symbol_1": "sym1",
    #         "stock_last_1": "last1",
    #         "stock_pchg_1": 'pchg1',
    #         "stock_bid_1": 'bid1',
    #         "stock_ask_1": 'ask1',
    #
    #         "stock_symbol_2": "sym5",
    #         "stock_last_2": "last2",
    #         "stock_pchg_2": "pchg2",
    #         "stock_bid_2": 'bid2',
    #         "stock_ask_2": 'ask2',
    #
    #         "stock_symbol_3": 'sym3',
    #         "stock_last_3": 'last3',
    #         "stock_pchg_3": 'pchg3',
    #         "stock_bid_3": 'bid3',
    #         "stock_ask_3": 'ask3'
    #     }
    #     return json
    #
    # def post_request_bundle(self, json):
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #     response = loop.run_until_complete(
    #         self.operation_center.node_manager.async_post_data_manager_request_bundle(
    #             json))
    #
    # def create_conditional_dictionary(self):
    #     chosen_stock_temp_container = ["test1", "test2", "test3"]
    #
    #     # for data_manager in self.list_chosen_data_managers:
    #     # chosen_conditional_symbol1 = self.list_chosen_data_managers[0].get_sym()
    #     # chosen_conditional_symbol2 = self.list_chosen_data_managers[1].get_sym()
    #     # chosen_conditional_symbol3 = self.list_chosen_data_managers[2].get_sym()
    #
    #     chosen_conditional_symbol1 = "test1"
    #     chosen_conditional_symbol2 = "test2"
    #     chosen_conditional_symbol3 = "test3"
    #
    #     conditional_dictionary = {chosen_conditional_symbol1: False, chosen_conditional_symbol2: False,
    #                               chosen_conditional_symbol3: False}
    #
    #     chosen_stock_temp_container_index = 0
    #
    #     for stock in chosen_stock_temp_container:
    #         if (chosen_stock_temp_container_index == 0):
    #             if (stock == chosen_conditional_symbol1):
    #                 conditional_dictionary[chosen_conditional_symbol1] = True
    #             if (stock == chosen_conditional_symbol2):
    #                 conditional_dictionary[chosen_conditional_symbol2] = True
    #             if (stock == chosen_conditional_symbol3):
    #                 conditional_dictionary[chosen_conditional_symbol3] = True
    #
    #         if (chosen_stock_temp_container_index == 1):
    #             if (stock == chosen_conditional_symbol1):
    #                 conditional_dictionary[chosen_conditional_symbol1] = True
    #             if (stock == chosen_conditional_symbol2):
    #                 conditional_dictionary[chosen_conditional_symbol2] = True
    #             if (stock == chosen_conditional_symbol3):
    #                 conditional_dictionary[chosen_conditional_symbol3] = True
    #
    #         if (chosen_stock_temp_container_index == 2):
    #             if (stock == chosen_conditional_symbol1):
    #                 conditional_dictionary[chosen_conditional_symbol1] = True
    #             if (stock == chosen_conditional_symbol2):
    #                 conditional_dictionary[chosen_conditional_symbol2] = True
    #             if (stock == chosen_conditional_symbol3):
    #                 conditional_dictionary[chosen_conditional_symbol3] = True
    #
    #         chosen_stock_temp_container_index += 1
    #     print(conditional_dictionary)
    #     return conditional_dictionary
    #
    # def register_chosen_data_managers(self, data_manager):
    #     self.list_chosen_data_managers.append(data_manager)
    #
    # def update_chosen_stock_temp_container(self, stock):
    #     self.chosen_stock_temp_container = ["test1", "test2", "test3"]
    #     if (len(self.chosen_stock_temp_container) == 3):
    #         conditional_dictionary = self.create_conditional_dictionary()
    #         self.validate_chosen_data_manager_dictionary(conditional_dictionary)
    #         self.chosen_stock_temp_container.clear()
    #     else:
    #         print("chosen_stock_temp_container amount:", len(self.chosen_stock_temp_container))