class Task_Master:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)

        return self.__instance

    def setup_instance(self, operation_center, thread_factory, http_utility, request_factory, type_converter,
                 top_stock_composite,
                 perpetual_timer, thread_manager, stock_composite_manager, dm_action, node_manager, time_manager,
                                    time_data_set_manager, day_decision_process_action_manager):
        self.operation_center = operation_center
        self.thread_factory = thread_factory
        self.http_utility = http_utility
        self.request_factory = request_factory
        self.type_converter = type_converter
        self.top_stock_composite = top_stock_composite
        self.thread_manager = thread_manager
        self.stock_composite_manager = stock_composite_manager
        self.DM_Action_instance = dm_action
        self.node_manager = node_manager
        self.time_manager = time_manager
        self.time_data_set_manager = time_data_set_manager
        self.day_decision_process_action_manager = day_decision_process_action_manager


    def perf_transform_stock(self, query):
        stock_composite = self.operation_center.organize_stock_composite()
        list_of_objects = [query, stock_composite, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center]
        self.thread_factory.create_thread_async_transform_stock(list_of_objects)

    # Top Stock
    def create_thread_async_top_stock_phase_internal(self):
        list_of_objects = [self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self]
        self.thread_factory.create_thread_async_top_stock_phase_internal(list_of_objects)

    def create_thread_async_top_stock_phase1(self, request):
        list_of_objects = [request, self.top_stock_composite, self.http_utility, self.request_factory,
                           self.type_converter,
                           self.operation_center, self]
        self.thread_factory.create_thread_async_top_stock_phase1(list_of_objects)

    def create_thread_async_top_stock_phase2(self, request):
        list_of_objects = [request, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self]
        self.thread_factory.create_thread_async_top_stock_phase2(list_of_objects)

    def create_thread_async_query_stock_phase1(self, request):
        list_of_objects = [request, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self]
        self.thread_factory.create_thread_async_query_stock_phase1(list_of_objects)


    # Buy
    def create_thread_async_phase1_market_buy(self):
        list_of_objects = [self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self]
        self.thread_factory.create_thread_async_phase1_market_buy(list_of_objects)

    def create_thread_async_phase2_market_buy(self, request):
        list_of_objects = [request, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self.DM_Action_instance, self]
        self.thread_factory.create_thread_async_phase2_market_buy(list_of_objects)

    def create_thread_async_phase3_market_buy(self, request):
        list_of_objects = [request, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self]
        self.thread_factory.create_thread_async_phase3_market_buy(list_of_objects)

    # Sell
    def create_thread_async_phase1_market_sell(self):
        list_of_objects = [self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self]
        self.thread_factory.create_thread_async_phase1_market_sell(list_of_objects)

    def create_thread_async_phase2_market_sell(self, request):
        list_of_objects = [request, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self.DM_Action_instance, self]
        self.thread_factory.create_thread_async_phase2_market_sell(list_of_objects)

    def create_thread_async_phase3_market_sell(self, request):
        list_of_objects = [request, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self]
        self.thread_factory.create_thread_async_phase3_market_sell(list_of_objects)

    # Account
    def create_thread_async_phase2_account(self, data):
        list_of_objects = [data, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self]
        self.thread_factory.create_thread_async_phase2_account(list_of_objects)

    def create_thread_async_phase3_account(self, data):
        list_of_objects = [data, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.stock_composite_manager, self]
        self.thread_factory.create_thread_async_phase3_account(list_of_objects)

    # Query
    def create_thread_async_query_symbol(self, request, data_manager):
        list_of_objects = [request, self.type_converter, data_manager]
        self.thread_factory.create_thread_async_query_symbol(list_of_objects)

    def create_thread_async_DM_stock_creation(self, request):
        list_of_objects = [request, self.type_converter, self.operation_center]
        self.thread_factory.create_thread_async_DM_stock_creation(list_of_objects)


    #Individual Query
    def create_thread_async_assemble_data_manager(self, request):
        list_of_objects = [request, self.type_converter, self.operation_center]
        self.thread_factory.create_thread_async_assemble_data_manager(list_of_objects)




    # Data_Manager assembly
    def create_thread_async_assemble_top_data_managers(self):
        # list_of_objects = [self.operation_center]
        self.thread_factory.create_thread_async_assemble_top_data_managers('', self.operation_center)
    def create_thread_async_initiate_top_data_managers(self):
        # list_of_objects = [self.operation_center]
        self.thread_factory.create_thread_async_initiate_top_data_managers('', self.operation_center)


    def create_thread_async_chosen_data_manager_selection(self):
        self.thread_factory.create_thread_async_chosen_data_manager_selection('', self.operation_center)



    # DM type creation process
    # Extended DM Creation
    def create_thread_async_assemble_extended_data_manager(self, sym_list):
        list_of_objects = [sym_list, self.operation_center]
        self.thread_factory.create_thread_async_assemble_extended_data_manager(list_of_objects)
    def create_thread_async_initiate_extended_data_manager(self, data_manager_list):
        list_of_objects = [data_manager_list, self.operation_center]
        self.thread_factory.create_thread_async_initiate_extended_data_manager(list_of_objects)

    # Chosen DM Creation
    def create_thread_async_assemble_chosen_data_manager(self, sym):
        list_of_objects = [sym, self.operation_center]
        self.thread_factory.create_thread_async_assemble_chosen_data_manager(list_of_objects)
    def create_thread_async_initiate_chosen_data_manager(self, data_manager):
        list_of_objects = [data_manager, self.operation_center]
        self.thread_factory.create_thread_async_initiate_chosen_data_manager(list_of_objects)

    # Bought DM Creation
    def create_thread_async_assemble_bought_data_manager(self, sym):
        list_of_objects = [sym, self.type_converter, self.operation_center]
        self.thread_factory.create_thread_async_assemble_bought_data_manager(list_of_objects)
    def create_thread_async_initiate_bought_data_manager(self, data_manager):
        list_of_objects = [data_manager, self.type_converter, self.operation_center]
        self.thread_factory.create_thread_async_initiate_bought_data_manager(list_of_objects)

    # Data_Manager (non-specific type) tasks
    def data_manager_query_stock_loop(self, data_manager):
        list_of_objects = [data_manager, self.node_manager, self]
        self.thread_factory.data_manager_query_stock_loop(list_of_objects)
    # Parse brokerage response and consume data by data_manager
    def data_manager_query_stock_conversion_loop(self, data_manager, response):
        list_of_objects = [data_manager, response, self.type_converter]
        self.thread_factory.data_manager_query_stock_conversion_loop(list_of_objects)


    #Timer processes
    def create_thread_async_buy_timer_delimiter(self,data_manager):
        list_of_objects = [data_manager, self.node_manager]

        self.thread_factory.create_thread_async_buy_timer_delimiter(list_of_objects)

    def create_thread_async_sell_timer_delimiter(self,data_manager):
        list_of_objects = [data_manager, self.node_manager]

        self.thread_factory.create_thread_async_sell_timer_delimiter(list_of_objects)





    def perf_top_stock(self):
        list_of_objects = [self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.top_stock_composite, self.thread_manager]
        self.thread_factory.manage_threads_for_top_stock(list_of_objects, self.top_stock_composite, self.thread_manager,
                                                         self.operation_center)
    def perf_top_stock_simple(self):
        list_of_objects = [self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center, self.top_stock_composite, self.thread_manager]
        self.thread_factory.manage_threads_for_top_stock(list_of_objects, self.top_stock_composite, self.thread_manager,
                                                         self.operation_center)
    def perf_query_stock_loop(self, data):
        stock_composite = self.operation_center.organize_stock_composite()
        list_of_objects = [data, stock_composite, self.http_utility, self.request_factory, self.type_converter,
                           self.operation_center]
        self.create_query_thread(self.perpetual_timer.setup_timer, 3, 5,
                                 self.thread_factory.create_thread_async_query_stock, list_of_objects)


