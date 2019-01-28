import asyncio
from threading import Thread


class Data_Manager_Request_Bundler:

    def __new__(self, sym):
        self.sym = sym
        self.
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.operation_center = None
        self.time_data_set_manager = None

        self.isGetLatestHourSet = 0
        self.isGetLatestTenMinuteSet = 0
        self.isGetLatestFiveMinuteSet = 0
        self.isGetLatestStockSet = 0

        self.dataBundleRecordSetInitiation = 0
        self.dataBundleDaySetInitiation = 0
        self.isHourChangeoverValue = 0
        self.isTenMinuteChangeoverValue = 0
        self.isFiveMinuteChangeoverValue = 0
        self.isStockStoreValue = 0

    def setup_data_manager_request_bundler(self, operation_center, time_data_set_manager, sym):
        self.operation_center = operation_center
        self.time_data_set_manager = time_data_set_manager
        self.sym =  sym

    def process_data_initialization(self, stock):
        self.dataBundleRecordSetInitiation = 1
        json = self.create_request_bundle(stock)
        self.post_request_bundle(json)
        self.reset_data_initialization_value()

    def reset_data_initialization_value(self):
        self.dataBundleRecordSetInitiation = 0

    def process_stock_store(self, stock):
        self.process_changeover_request()
        json = self.create_request_bundle(stock)
        self.post_request_bundle(json)
        self.reset_process_changeover_request()

    def reset_process_changeover_request(self):
        self.isHourChangeoverValue = 0
        self.isChangeoverValue = 0
        self.isHourChangeoverValue = 0

    def process_changeover_request(self):
        if (self.time_data_set_manager.calculate_hour_change()):
            self.isHourChangeoverValue = 1
            return
        if (self.time_data_set_manager.calculate_ten_minute_change()):
            self.isTenMinuteChangeoverValue = 1
            return
        if (self.time_data_set_manager.calculate_five_minute_change()):
            self.isFiveMinuteChangeoverValue = 1
            return

    def create_request_bundle(self, stock):
        json = {
            "request_type": "data_manager_request_bundle",
            "isGetLatestHourSet": self.isGetLatestHourSet,
            "isGetLatestTenMinuteSet": self.isGetLatestTenMinuteSet,
            "isGetLatestFiveMinuteSet": self.isGetLatestFiveMinuteSet,
            "isGetLatestStockSet": self.isGetLatestStockSet,

            "dataBundleRecordSetInitiation": self.dataBundleRecordSetInitiation,
            "dataBundleDaySetInitiation": self.dataBundleDaySetInitiation,
            "isHourChangeover": self.isHourChangeoverValue,
            "isTenMinuteChangeover": self.isTenMinuteChangeoverValue,
            "isFiveMinuteChangeover": self.isFiveMinuteChangeoverValue,
            "isStockStore": self.isStockStoreValue,

            "stock_symbol": stock.get_sym(),
            "stock_last": stock.get_last(),
            "stock_pchg": stock.get_pchg(),
            "stock_bid": stock.get_bid(),
            "stock_ask": stock.get_ask()
        }
        return json


    def post_request_bundle(self, json):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(
            self.operation_center.node_manager.async_post_data_manager_request_bundle(
                json))






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