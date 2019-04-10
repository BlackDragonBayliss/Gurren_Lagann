import asyncio
from threading import Thread
from Data_Manager import Data_Manager
from Extended_Data_Manager import Extended_Data_Manager
from Chosen_Data_Manager import Chosen_Data_Manager
from Bought_Data_Manager import Bought_Data_Manager


class Thread_Factory:
    def __init__(self):
        self.name = ''
        self.start_background_loop_assemble_extended_data_manager_index = 0


    def start_background_loop_transform_stock(self, data, stock_composite, http_utility, request_factory,
                                              type_converter,
                                              operation_center):
        type_converter.parse_stock_query(data, stock_composite)
        operation_center_stock_composite_list = operation_center.get_list_stock_composite()
        operation_center_stock_list = operation_center_stock_composite_list[0].get_list_stocks()
        print(operation_center_stock_list[0].get_last())

    def create_thread_async_transform_stock(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                stock_composite = arg
            if (count == 2):
                http_utility = arg
            if (count == 3):
                request_factory = arg
            if (count == 4):
                type_converter = arg
            if (count == 5):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_transform_stock,
                   args=(data, stock_composite, http_utility, request_factory, type_converter, operation_center))
        t.start()

    def start_background_loop_task(self, data, request_code, top_stock_composite):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.async_post_top_stock(data, request_code, top_stock_composite))

    def create_thread_async_task(self, data, request_code, top_stock_composite):
        t = Thread(target=self.start_background_loop_task, args=(data, request_code, top_stock_composite))
        t.start()

    def start_background_loop_query_stock_loop(self, data, request_code, stock_composite, http_utility, request_factory,
                                               type_converter, operation_center):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(http_utility.async_post_stock(data, request_factory))
        typeConverter.parse_stock_query(response, stock_composite)

    def create_thread_async_query_stock_loop(self, data, request_code, stock_composite, http_utility, request_factory,
                                             type_converter, operation_center):
        t = Thread(target=self.start_background_loop_query_stock, args=(
            data, request_code, stock_composite, http_utility, request_factory, type_converter, operation_center))
        t.start()

    # Top Stock Pull
    def start_background_loop_top_stock_phase_internal(self, http_utility, request_factory, type_converter,
                                                       operation_center, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(http_utility.async_post_stock_top_phase_internal(request_factory))

    def create_thread_async_top_stock_phase_internal(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                http_utility = arg
            if (count == 1):
                request_factory = arg
            if (count == 2):
                type_converter = arg
            if (count == 3):
                operation_center = arg
            if (count == 4):
                task_master = arg

            count = count + 1

        t = Thread(target=self.start_background_loop_top_stock_phase_internal,
                   args=(
                       http_utility, request_factory, type_converter, operation_center,
                       task_master))
        t.start()

    def start_background_loop_top_stock_phase1(self, data, top_stock_composite, http_utility, request_factory,
                                               type_converter,
                                               operation_center, task_master):
        #Parse TSP from brokerage, call to assemble Chosen_Data_Manager objects


        type_converter.set_json_top_stocks(data)
        type_converter.set_highest_chosen()
        type_converter.calc_highest_chosen()

        type_converter.collect_top_stock_results_in_list()

        data_list = type_converter.get_list_chosen_stocks()
        sym_data_list = []
        for val in data_list:
            sym_data_list.append(val.get_sym())
        # operation_center.list_chosen_data_manager = data_list
        print("start_background_loop_top_stock_phase1: "+str(sym_data_list))
        operation_center.set_is_initial_top_stock_pull_completed("1")
        operation_center.process_async_assemble_extended_data_manager(sym_data_list)

        # else:
        #     #Handle extended creation, given type_converter metrics reset.
        #     #What is different for handling new extended,
        #
        #
        #     pass



    def create_thread_async_top_stock_phase1(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            # print(count)
            if (count == 0):
                data = arg
            if (count == 1):
                top_stock_composite = arg
            if (count == 2):
                http_utility = arg
            if (count == 3):
                request_factory = arg
            if (count == 4):
                type_converter = arg
            if (count == 5):
                operation_center = arg
            if (count == 6):
                task_master = arg

            count = count + 1

        t = Thread(target=self.start_background_loop_top_stock_phase1,
                   args=(
                       data, top_stock_composite, http_utility, request_factory, type_converter, operation_center,
                       task_master))
        t.start()

    def start_background_loop_top_stock_phase2(self, data, http_utility, request_factory, type_converter,
                                               operation_center, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        type_converter.parse_stock_queries(data, operation_center)
        top_stock_composite = operation_center.get_top_stock_composite()

        response = loop.run_until_complete(
            http_utility.async_post_stock_top_phase2(top_stock_composite, request_factory))

        data_list = top_stock_composite.get_list_chosen_stocks()
        for val in data_list:
            print(val.get_name())


            # topStockComposite.clear_top_stocks_processing_values()
            # topStockComposite.get_listChosenStocks().clear()

    def create_thread_async_top_stock_phase2(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                http_utility = arg
            if (count == 2):
                request_factory = arg
            if (count == 3):
                type_converter = arg
            if (count == 4):
                operation_center = arg
            if (count == 5):
                task_master = arg

            count = count + 1

        t = Thread(target=self.start_background_loop_top_stock_phase2,
                   args=(data, http_utility, request_factory, type_converter, operation_center, task_master))
        t.start()

    def start_background_loop_query_stock_phase1(self, data, http_utility, request_factory, type_converter,
                                                 operation_center, composite_manager, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        stock_composite = type_converter.parse_stock_query(data, composite_manager)
        # topStockComposite = operationCenter.get_topStockComposite()

        response = loop.run_until_complete(http_utility.async_post_stock_query_phase1(stock_composite, request_factory))


        # topStockComposite.clear_top_stocks_processing_values()
        # topStockComposite.get_listChosenStocks().clear()

    def create_thread_async_query_stock_phase1(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                http_utility = arg
            if (count == 2):
                request_factory = arg
            if (count == 3):
                type_converter = arg
            if (count == 4):
                operation_center = arg
            if (count == 5):
                composite_manager = arg
            if (count == 6):
                task_master = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_query_stock_phase1,
                   args=(data, http_utility, request_factory, type_converter, operation_center, composite_manager,
                         task_master))
        t.start()

    # buy
    def start_background_loop_phase1_market_buy(self, http_utility, request_factory, type_converter,
                                                operation_center, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # handle on chosen_stocks_list


        # handle on decision process init




        #Future support for storing buy info in database
        # response = loop.run_until_complete(http_utility.async_post_market_buy_phase1(request_data, request_factory))



    def create_thread_async_phase1_market_buy(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                http_utility = arg
            if (count == 1):
                request_factory = arg
            if (count == 2):
                type_converter = arg
            if (count == 3):
                operation_center = arg
            if (count == 4):
                task_master = arg

            count = count + 1

        t = Thread(target=self.start_background_loop_phase1_market_buy,
                   args=(http_utility, request_factory, type_converter, operation_center, task_master))
        t.start()

    def start_background_loop_phase2_market_buy(self, data, http_utility, request_factory, type_converter,
                                                operation_center, composite_manager, DM_Action_instance, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        DM_Buy_instance = type_converter.parse_market_buy(data, DM_Action_instance)

        # # topStockComposite = operationCenter.get_topStockComposite()
        #
        response = loop.run_until_complete(http_utility.async_post_market_buy_phase2(DM_Buy_instance, request_factory))
        #
        # # topStockComposite.clear_top_stocks_processing_values()
        # # topStockComposite.get_listChosenStocks().clear()
        print('buy phase2')

    def create_thread_async_phase2_market_buy(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                http_utility = arg
            if (count == 2):
                request_factory = arg
            if (count == 3):
                type_converter = arg
            if (count == 4):
                operation_center = arg
            if (count == 5):
                composite_manager = arg
            if (count == 6):
                DM_Action_instance = arg
            if (count == 6):
                task_master = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_phase2_market_buy,
                   args=(data, http_utility, request_factory, type_converter, operation_center, composite_manager,
                         DM_Action_instance, task_master))
        t.start()

    def start_background_loop_phase3_market_buy(self, data, http_utility, request_factory, type_converter,
                                                operation_center, composite_manager, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        stock_composite = type_converter.parse_stock_query(data, composite_manager)
        # # topStockComposite = operationCenter.get_topStockComposite()
        #
        response = loop.run_until_complete(http_utility.async_post_market_buy_phase3(stock_composite, request_factory))
        #
        # # topStockComposite.clear_top_stocks_processing_values()
        # # topStockComposite.get_listChosenStocks().clear()
        print('buy phase3')

    def create_thread_async_phase3_market_buy(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                http_utility = arg
            if (count == 2):
                request_factory = arg
            if (count == 3):
                type_converter = arg
            if (count == 4):
                operation_center = arg
            if (count == 5):
                composite_manager = arg
            if (count == 6):
                task_master = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_phase3_market_buy,
                   args=(data, http_utility, request_factory, type_converter, operation_center, composite_manager,
                         task_master))
        t.start()

    # sell

    def start_background_loop_phase1_market_sell(self, http_utility, request_factory, type_converter,
                                                 operation_center, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # typeConverter.parse_stock_queries(data, operationCenter)
        # topStockComposite = operationCenter.get_topStockComposite()
        #


        request_data = operation_center.get_DM_Action().get_name()
        print("request_data is: " + request_data)
        response = loop.run_until_complete(http_utility.async_post_market_sell_phase1(request_data, request_factory))
        #
        # topStockComposite.clear_top_stocks_processing_values()
        # topStockComposite.get_listChosenStocks().clear()

        print('sell phase1')

    def create_thread_async_phase1_market_sell(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                http_utility = arg
            if (count == 1):
                request_factory = arg
            if (count == 2):
                type_converter = arg
            if (count == 3):
                operation_center = arg
            if (count == 4):
                task_master = arg

            count = count + 1

        t = Thread(target=self.start_background_loop_phase1_market_sell,
                   args=(http_utility, request_factory, type_converter, operation_center, task_master))
        t.start()

    def start_background_loop_phase2_market_sell(self, data, http_utility, request_factory, type_converter,
                                                 operation_center, composite_manager, DM_Action_instance, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # Sell response data, Return a finished DM_Action
        # We will need to acquire data from buy action that was stored and use those metrics.


        # Query
        DM_Action = type_converter.parse_DM_Action(data, DM_Action_instance)
        # DM_Action
        response = loop.run_until_complete(http_utility.async_post_market_sell_phase2(DM_Action, request_factory))

        print(data)
        print('sell phase2')

    def create_thread_async_phase2_market_sell(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                http_utility = arg
            if (count == 2):
                request_factory = arg
            if (count == 3):
                type_converter = arg
            if (count == 4):
                operation_center = arg
            if (count == 5):
                composite_manager = arg
            if (count == 6):
                DM_Action_instance = arg
            if (count == 7):
                taskMaster = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_phase2_market_sell,
                   args=(data, http_utility, request_factory, type_converter, operation_center, composite_manager,
                         DM_Action_instance, task_master))
        t.start()

    # account

    def start_background_loop_phase2_account(self, data, http_utility, request_factory, type_converter,
                                             operation_center, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # parse data into account object
        account_information = type_converter.parse_account_information(data)

        # post account information to be stored
        response = loop.run_until_complete(
            httpUtility.async_post_account_information_phase2(account_information, request_factory))
        print('account phase2')
        # print(data)

    def create_thread_async_phase2_account(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                http_utility = arg
            if (count == 2):
                request_factory = arg
            if (count == 3):
                type_converter = arg
            if (count == 4):
                operation_center = arg
            if (count == 5):
                task_master = arg

            count = count + 1

        t = Thread(target=self.start_background_loop_phase2_account,
                   args=(data, http_utility, request_factory, type_converter, operation_center, task_master))
        t.start()

    def start_background_loop_phase3_account(self, data, http_utility, request_factory, type_converter,
                                             operation_center, composite_manager, task_master):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        account_information = type_converter.parse_stock_query(data, composite_manager)
        # # topStockComposite = operationCenter.get_topStockComposite()
        #
        response = loop.run_until_complete(
            http_utility.async_post_stock_query_phase3(account_information, request_factory))

        # # topStockComposite.clear_top_stocks_processing_values()
        # # topStockComposite.get_listChosenStocks().clear()
        print('account phase3')
        print(data)

    def create_thread_async_phase3_account(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                http_utility = arg
            if (count == 2):
                request_factory = arg
            if (count == 3):
                type_converter = arg
            if (count == 4):
                operation_center = arg
            if (count == 5):
                composite_manager = arg
            if (count == 6):
                task_master = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_phase3_account,
                   args=(data, http_utility, request_factory, type_converter, operation_center, composite_manager,
                         task_master))
        t.start()

    # Query

    def start_background_loop_query_symbol(self, data, type_converter,
                                           data_manager):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        stock = type_converter.parse_symbol_query(data)
        data_manager.bind_data_object(stock)

    def create_thread_async_query_symbol(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                type_converter = arg
            if (count == 2):
                data_manager = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_query_symbol,
                   args=(data, type_converter, data_manager))
        t.start()



    #Advanced DM assembly
    #Extended DM
    #Assembly of DM
    # Chosen DM
    # Assembly of DM
    def start_background_loop_assemble_extended_data_manager(self, sym_list,
                                                           operation_center):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # test_sym_list = ['NRP','AAPL','USG']

        # extended_data_manager_list = operation_center.get_list_chosen_data_manager()

        if(operation_center.get_is_initial_extended_assembled() == "0"):
            print("start_background_loop_assemble_extended_data_manager: hit true")
            for sym in sym_list:
                extended_data_manager_instance = Extended_Data_Manager(sym, 0, operation_center,
                                                                       operation_center.get_time_data_set_manager())
                operation_center.top_stock_monument_composite.add_to_top_stock_data_manager_monument_list(
                    extended_data_manager_instance)

        else:
            print("start_background_loop_assemble_extended_data_manager: hit else")

            chosen = operation_center.top_stock_monument_composite.get_chosen_data_manager()
            extended_list = operation_center.top_stock_monument_composite.get_top_stock_data_manager_monument_list()
            new_symbol_list =  sym_list

            match_results = []

            # Filter for chosen
            for new_sym in new_symbol_list:
                if (new_sym == chosen.sym):
                    match_results.append(new_sym)

            # Filter for extended.
            for new_sym in new_symbol_list:
                for extended in extended_list:
                    if (extended == new_sym):
                        match_results.append(extended)

            print("new_symbol_list before results: " + str(new_symbol_list))

            for match_item in match_results:
                new_symbol_list.remove(match_item)
            print("Match results: " + str(match_results))
            print("new_symbol_list results: " +  str(new_symbol_list))

            for symbol in new_symbol_list:
                print(symbol)


            #for sym in match_list, create extended and add to
            for sym in new_symbol_list:
                extended_data_manager_instance = Extended_Data_Manager(sym, 0, operation_center,
                                                                       operation_center.get_time_data_set_manager())
                operation_center.top_stock_monument_composite.add_to_top_stock_data_manager_monument_list(
                    extended_data_manager_instance)


        operation_center.set_is_initial_extended_assembled("1")
        operation_center.process_async_initiate_extended_data_manager()

    def create_thread_async_assemble_extended_data_manager(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                sym_list = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_assemble_extended_data_manager,
                   args=(sym_list, operation_center))
        t.start()


    # Chosen DM
    # Assembly of DM
    def start_background_loop_assemble_chosen_data_manager(self, sym,
                                                           operation_center):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # test_sym_list = ['NRP','AAPL','USG']


        # extended_data_manager_list = operation_center.get_list_chosen_data_manager()
        # for sym in sym_list:
        chosen_data_manager_instance = Chosen_Data_Manager(sym, 0, operation_center,
                                                           operation_center.get_time_data_set_manager())
        operation_center.top_stock_monument_composite.set_chosen_data_manager(
            chosen_data_manager_instance)

        # chosen_data_manager_list = operation_center.get_list_chosen_data_manager()
        # for sym in sym_list:
        #     chosen_data_manager_instance = Chosen_Data_Manager(sym, 0, operation_center,
        #                                                        operation_center.get_time_data_set_manager())
        #     operation_center.top_stock_monument_composite.add_to_top_stock_data_manager_monument_list(chosen_data_manager_instance)
            # chosen_data_manager_list.append(chosen_data_manager_instance)

        # operation_center.process_async_initiate_chosen_data_manager(chosen_data_manager_list)
        operation_center.process_async_initiate_chosen_data_manager(chosen_data_manager_instance)

    def create_thread_async_assemble_chosen_data_manager(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                sym = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_assemble_chosen_data_manager,
                   args=(sym, operation_center))
        t.start()


    # Bought DM
    # Assembly of DM
    def start_background_loop_assemble_bought_data_manager(self, sym, type_converter,
                                                           operation_center):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        bought_data_manager_instance = Bought_Data_Manager(sym,0,operation_center)
        bought_data_manager_list = operation_center.get_list_bought_data_manager()

        # ID storage process...
        bought_data_manager_list.append(bought_data_manager_instance)

        # init process
        operation_center.process_async_initiate_bought_data_manager(bought_data_manager_instance)



    def create_thread_async_assemble_bought_data_manager(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                sym = arg
            if (count == 1):
                type_converter = arg
            if (count == 2):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_assemble_bought_data_manager,
                   args=(sym, type_converter, operation_center))
        t.start()



    #Extended DM
    #Initiation
    def start_background_loop_initiate_extended_data_manager(self, data_manager_list, operation_center
                                                           ):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        #passing DM list to...or
        if(operation_center.get_is_initial_golden_goose_process_completed() == "0"):
            for data_manager in data_manager_list:
                print("init ex data_manager: "+data_manager.get_sym())
                data_manager.init_data_processing()

            operation_center.set_is_initial_golden_goose_process_completed("1")

        else:
            print("hit inside consecutive iteration extended data_manager")
            #Handle check DM isRunning
            for data_manager in data_manager_list:
                if(data_manager.get_is_running()):
                    print("sweet running do nothing")
                else:
                    print("init ex data_manager: "+data_manager.get_sym())
                    data_manager.init_data_processing()

    def create_thread_async_initiate_extended_data_manager(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data_manager_list = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_initiate_extended_data_manager,
                   args=(data_manager_list, operation_center))
        t.start()



    # Chosen DM
    # Initiation
    def start_background_loop_initiate_chosen_data_manager(self, data_manager, operation_center
                                                             ):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # init chosen_data_manager'sf
        # for data_manager in data_manager_list:
        data_manager.init_data_processing()

        # Update Data_Decision_Process_Action_Manager with chosen stocks
        # operation_center.top_stock_monument_composite.set_top_stock_data_manager_monument_list(data_manager_list)


    def create_thread_async_initiate_chosen_data_manager(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data_manager = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_initiate_chosen_data_manager,
                   args=(data_manager, operation_center))
        t.start()




    # Bought DM
    # Initiation
    def start_background_loop_initiate_bought_data_manager(self, data_manager, operation_center
                                                             ):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        data_manager.init_data_processing()

    def create_thread_async_initiate_bought_data_manager(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data_manager = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_initiate_bought_data_manager,
                   args=(data_manager, operation_center))
        t.start()
















    # DM management
    # def start_background_loop_assemble_top_data_managers(self, data, operation_center
    #                                                      ):
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #
    #     # handle on DM chosen list
    #     # top_stock_composite = operation_center.get_top_stock_composite()
    #
    #     data_list = top_stock_composite.get_list_chosen_stocks()
    #     list_data_managers = operation_center.get_list_data_managers()
    #     # for each sym create DM and store in dm_list
    #     for val in data_list:
    #         print(val.get_name())
    #         # for each symbol create DM
    #         data_manager = Data_Manager(val.get_name(),0)
    #         # store in list
    #         list_data_managers.append(data_manager)
    #
    #     # local call to init, psuedo-callback
    #     operation_center.process_async_initiate_top_data_managers()
    #     print('loop_assemble_top_data_managers')
    #     # response = loop.run_until_complete(httpUtility.async_post_stock_query_phase1(stockComposite, requestFactory))
    #
    # def create_thread_async_assemble_top_data_managers(self, data, operation_center):
    #     # count = 0
    #     # for arg in list_of_objects:
    #     #     if (count == 0):
    #     #         operation_center = arg
    #     #     count = count + 1
    #     t = Thread(target=self.start_background_loop_assemble_top_data_managers,
    #                args=(data, operation_center))
    #     t.start()
    #
    # # Init process
    # def start_background_loop_initiate_top_data_managers(self, data, operation_center
    #                                                      ):
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #
    #     list_data_managers = operation_center.get_list_data_managers()
    #
    #     for data_manager in list_data_managers:
    #         data_manager.init_data_processing()
    #
    #     print('loop_initiate_top_data_managers')
    #     # response = loop.run_until_complete(httpUtility.async_post_stock_query_phase1(stockComposite, requestFactory))
    #
    # def create_thread_async_initiate_top_data_managers(self, data, operation_center):
    #     # count = 0
    #     # for arg in list_of_objects:
    #     #     if (count == 0):
    #     #         operation_center = arg
    #     #     count = count + 1
    #
    #     t = Thread(target=self.start_background_loop_initiate_top_data_managers,
    #                args=(data, operation_center))
    #     t.start()



    # Decide on chosen

    def start_background_loop_decide_chosen_data_manager(self, data, operation_center):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # data_manager_list[0].init_data_processing()
        # for data_manager in data_manager_list:
        #     data_manager.init_data_processing()

        #Who's handling decision process, needs to be 1 layer of abstraction.



            # response = loop.run_until_complete(httpUtility.async_post_stock_query_phase1(stockComposite, requestFactory))


    def create_thread_async_decide_chosen_data_manager(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_initiate_chosen_data_manager,
                   args=(data, operation_center))
        t.start()

    #
    # def start_background_loop_assemble_data_manager(self, data, operation_center
    #                                                 ):
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #
    #     # create DM process
    #     data_manager = Data_Manager()
    #
    #     # how to get DM by ID
    #     #
    #
    #     # operation_center bind
    #     operation_center.add_data_manager_to_list(data_manager)
    #
    #     # response = loop.run_until_complete(httpUtility.async_post_stock_query_phase1(stockComposite, requestFactory))
    #
    # def create_thread_async_assemble_data_manager(self, list_of_objects):
    #     count = 0
    #     for arg in list_of_objects:
    #         if (count == 0):
    #             operation_center = arg
    #         count = count + 1
    #     t = Thread(target=self.start_background_loop_assemble_data_manager,
    #                args=(operation_center))
    #     t.start()
    #
    # # init process
    # def start_background_loop_initiate_data_manager(self, data, operation_center
    #                                                 ):
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #
    #     # create DM process
    #     data_manager = Data_Manager()
    #
    #     # how to get DM by ID
    #     #
    #
    #     # operation_center bind
    #     operation_center.add_data_manager_to_list(data_manager)
    #
    #     # response = loop.run_until_complete(httpUtility.async_post_stock_query_phase1(stockComposite, requestFactory))
    #
    # def create_thread_async_initiate_data_manager(self, list_of_objects):
    #     count = 0
    #     for arg in list_of_objects:
    #         if (count == 0):
    #             data = arg
    #         if (count == 1):
    #             operation_center = arg
    #         count = count + 1
    #
    #     t = Thread(target=self.start_background_loop_initiate_data_manager,
    #                args=(data, operation_center))
    #     t.start()


    # DM tasks
    def start_background_loop_data_manager_query_stock_loop(self, data_manager, node_manager, task_manager):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        sym = data_manager.get_sym()
        # Async call to node, query brokerage, return un-parsed brokerage response
        response = loop.run_until_complete(node_manager.async_post_node_manager_query(sym))
        # print("response: ", response)
        # Consume data_manager and brokerage response
        task_manager.data_manager_query_stock_conversion_loop(data_manager,response)


    def data_manager_query_stock_loop(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data_manager = arg
            if (count == 1):
                node_manager = arg
            if (count == 2):
                task_manager = arg

            count = count + 1

        t = Thread(target=self.start_background_loop_data_manager_query_stock_loop,
                   args=(data_manager, node_manager, task_manager))
        t.start()


    def start_background_loop_data_manager_query_stock_conversion_loop(self, data_manager, response, type_converter):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        stock = type_converter.parse_stock_query(response)
        data_manager.handle_stock_retrieval(stock)

    def data_manager_query_stock_conversion_loop(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data_manager = arg
            if (count == 1):
                response = arg
            if (count == 2):
                type_converter = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_data_manager_query_stock_conversion_loop,
                   args=(data_manager, response, type_converter))
        t.start()



    def start_background_loop_DM_stock_creation(self, data, type_converter, operation_center):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        stock = type_converter.parse_symbol_query(data)
        print("stock pchg is: ", stock.get_pchg())

        # operation_center

        # top_stock_composite = operation_center.get_top_stock_composite()

        DM_list = operation_center.get_list_data_managers()
        #hhandle on DM List

        # chosen_stock_list = top_stock_composite.get_list_chosen_stocks()[0]
        for DM in DM_list:
            if DM.sym == stock.get_name():
                DM.bind_data_object(stock)
        # data_manager.bind_data_object(stock)

    def create_thread_async_DM_stock_creation(self, list_of_objects):
        count = 0

        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                type_converter = arg
            if (count == 2):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_DM_stock_creation,
                   args=(data, type_converter, operation_center))
        t.start()




    # Timer processes
    def start_background_loop_buy_timer_delimiter(self, data, operation_center
                                                    ):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # create DM process
        data_manager = Data_Manager()

        # operation_center bind
        operation_center.add_data_manager_to_list(data_manager)

        # response = loop.run_until_complete(httpUtility.async_post_stock_query_phase1(stockComposite, requestFactory))

    def create_thread_async_buy_timer_delimiter(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_buy_timer_delimiter,
                   args=(data, operation_center))
        t.start()


    def start_background_loop_sell_timer_delimiter(self, data, operation_center
                                                    ):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # create DM process
        data_manager = Data_Manager()

        # operation_center bind
        operation_center.add_data_manager_to_list(data_manager)

        # response = loop.run_until_complete(httpUtility.async_post_stock_query_phase1(stockComposite, requestFactory))

    def create_thread_async_sell_timer_delimiter(self, list_of_objects):
        count = 0
        for arg in list_of_objects:
            if (count == 0):
                data = arg
            if (count == 1):
                operation_center = arg
            count = count + 1

        t = Thread(target=self.start_background_loop_sell_timer_delimiter,
                   args=(data, operation_center))
        t.start()

