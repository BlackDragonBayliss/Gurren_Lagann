class Trade_Manager:
    __instance = None
    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            return self.__instance

    def buy_stock_full_amount(self,operation_center,stock_statistics_composite):
        #Support for request for Node request
        #Node request

        #Handle Node Buy Sequence and returned data
        #Handle second query to get position bought
            #Repeat until position gained.
            #Verifying data retrieval
        #Upon verification
        # Handle response and store in Data_Manager_Action
        operation_center.get_data_manager_action()
        #Callback to operation_center
        operation_center.process_transform_chosen_to_bought()
        pass

    def buy_stock_partial(self, sym):
        pass

    def update_data_manager_action(self):
        pass

    def get_epoch_of_trade (self):
        return self.epoch_of_trade
    def set_epoch_of_trade (self, epoch_of_trade):
        self.epoch_of_trade = epoch_of_trade


