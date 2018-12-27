class Trade_Manager:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            return self.__instance

    def buy_stock_full_amount(self, operation_center, stock_statistics_composite):
        # Support for request for Node request
        # Node request

        # Handle Node Buy Sequence and returned data
        # Handle second query to get position bought
        # Repeat until position gained.
        # Verifying data retrieval
        # Upon verification
        # Handle response and store in Data_Manager_Action
        operation_center.get_data_manager_action()
        # Callback to operation_center, bought
        operation_center.process_transform_chosen_to_bought()
        operation_center.cancel_chosen_stocks()

        # Init monitoring for Odin_Algorithm
        operation_center.

    def buy_stock_partial(self, sym):
        pass

    def sell_stock_full_amount(self, operation_center, stock_statistics_composite):
        # Support for request for Node request
        # Node request

        # Handle Node Buy Sequence and returned data
        # Handle second query to get position bought
        # Repeat until position gained.
        # Verifying data retrieval
        # Upon verification


        # Handle response and store in Data_Manager_Action
        # respones -> type_converter, DM Action handled there.


        operation_center.store_data_manager_action_to_database()
        # Store Data_Manager_Action in database

        # Email analytics


        # Callback to operation_center, end_operations and reset
        # operation_center.process_transform_chosen_to_bought()
        operation_center.end_operations()

    def sell_stock_partial(self, sym):
        pass

    def update_data_manager_action(self):
        pass

    def get_epoch_of_trade(self):
        return self.epoch_of_trade

    def set_epoch_of_trade(self, epoch_of_trade):
        self.epoch_of_trade = epoch_of_trade
