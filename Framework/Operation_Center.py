import asyncio

from Data_Manager_Action import Data_Manager_Action
from Data_Manager_Request_Bundler import Data_Manager_Request_Bundler
from Day_Decision_Process_Action_Manager import Day_Decision_Process_Action_Manager
from HTTP_Utility import HTTP_Utility
from Node_Manager import Node_Manager
from Odin_Algorithm import Odin_Algorithm
from Perpetual_Timer import Perpetual_Timer
from Request_Factory import Request_Factory
from Scraper_Manager import Scraper_Manager
from Stock_Composite import Stock_Composite
from Stock_Composite_Manager import Stock_Composite_Manager
from Stock_Statistics_Composite import Stock_Statistics_Composite
from Task_Master import Task_Master
from Thread_Factory import Thread_Factory
from Thread_Manager import Thread_Manager
from Time_Data_Set_Manager import Time_Data_Set_Manager
from Time_Manager import Time_Manager
from Top_Stock_Monument_Composite import Top_Stock_Monument_Composite
from Trade_Manager import Trade_Manager
from Type_Converter import Type_Converter

from Stock_Observance_Rotation_Manager import Stock_Observance_Rotation_Manager


class Operation_Center:
    list_stock_composite = []
    list_top_stock_symbols = []
    list_top_stock_composite = []
    list_data_managers = []
    list_extended_data_manager = []
    list_chosen_data_manager = []
    list_bought_data_manager = []

    stock_composite_generation_iteration = 0
    top_stock_chosen = 0
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.__instance.name = ''
            self.http_utility = HTTP_Utility()
            self.type_converter = Type_Converter()
            self.request_factory = Request_Factory()
            self.thread_factory = Thread_Factory()
            self.top_stock_monument_composite = Top_Stock_Monument_Composite()
            self.perpetual_timer_instance= Perpetual_Timer()
            self.perpetual_timer_main_process_loop = Perpetual_Timer()
            self.perpetual_timer_buy_analysis = Perpetual_Timer()
            self.perpetual_timer_process_scrape_top_stock_list_dow_volume_industry = Perpetual_Timer()

            self.thread_manager = Thread_Manager()
            self.stock_composite_manager = Stock_Composite_Manager()
            self.data_manager_action = Data_Manager_Action()
            self.node_manager = Node_Manager()

            self.time_manager = Time_Manager()
            self.time_data_set_manager = Time_Data_Set_Manager()
            self.day_decision_process_action_manager = Day_Decision_Process_Action_Manager()
            self.stock_statistics_composite = Stock_Statistics_Composite
            self.trade_manager = Trade_Manager()
            self.odin_algorithm = Odin_Algorithm()
            self.scraper_manager = Scraper_Manager()
            self.data_manager_request_bundler = Data_Manager_Request_Bundler()
            self.task_master = Task_Master()
            self.task_master.setup_instance(self.__instance, self.thread_factory, self.http_utility,
                                            self.request_factory,
                                            self.type_converter, self.top_stock_monument_composite, self.perpetual_timer_instance,
                                            self.thread_manager, self.stock_composite_manager, self.data_manager_action,
                                            self.node_manager, self.time_manager,
                                            self.time_data_set_manager, self.day_decision_process_action_manager)

            self.is_start_yet_to_be_initiated = True
            self.is_scrape_yet_to_be_initiated = True
            self.is_top_stock_bird_yet_to_be_initiated = True

            self.is_condition_top_stock_pull_gather= False
            self.is_condition_moirae_phase_one = False
            self.is_condition_moirae_phase_two = False
            self.is_condition_moirae_phase_three = False
            self.is_condition_end_of_day = False

            self.start_hour = self.time_manager.get_current_hour() #15
            self.start_minute =self.time_manager.get_current_minute()  #42
            self.scrape_hour = self.start_hour
            # self.scrape_minute = self.start_minute + 1

            self.top_stock_bird_hour = self.start_hour
            self.top_stock_bird_minute = self.start_minute + 1

        return self.__instance

    def process_main_process_loop(self):
        print("start")
        self.time_data_set_manager.init_time_monitoring(self)
        # self.start_hour = 6
        # self.start_minute = 58
        # self.data_manager_request_bundler.setup_data_manager_request_bundler(self, self.time_data_set_manager)
        self.data_manager_request_bundler.setup_data_manager_request_bundler(self, self.get_time_data_set_manager())

        self.main_process_loop()
    def main_process_loop(self):
        self.perpetual_timer_main_process_loop.setup_timer_stock(1, 1000000, self.main_loop, 'main_process_loop')

    def intake_golden_goose_report(self,golden_goose_report):
        #GG BuySell Watch is measured locally Neo,
        #GG Update current Golden in Node.
        print("golden_goose_report: "+str(golden_goose_report))
        #Stock rotation piece
        stock_observance_rotation_manager = Stock_Observance_Rotation_Manager(self, self.get_top_stock_monument_composite())
        isContinueOperations = int(stock_observance_rotation_manager.intake_query(golden_goose_report))

        # print("isContinueOperations: "+str(isContinueOperations))

        # stock_observance_rotation_manager.tag_data_managers()

        # If proceed with activations.
        if(isContinueOperations == 1):
            print("Returning true")
            stock_observance_rotation_manager.tag_data_managers()
            #Filter each DM, cancel or slow, set slow.
            #return res ...? probably no.

            #Filter each non-priory DM, Filter for highest priory,
            #Highest priory never match - check Neo
            #Slow non-highest priorities.
            stock_observance_rotation_manager.filter_data_managers()
        else:
            print("Returning false")

        #Upon new TSP pulled, evaluated, stock stored, ...

    def main_loop(self):

        #On loop 30 minute interval, TSP Bird process

        #If 30 minute time period pass, process,
            #Process TSP pull, Node stock store,
            #Interminnent dilly dally-projective stock rotation

        #Begin 5 minute pause.
        #30 minute rotation

        #Handle 45 start
        #Test purpose. current minute, minute iterate, continue fast enough to do all measures
        #Live handling turnover,

        # #First minute iterate.
        # # if():
        # #     calculate_time_delimiter_start
        # #Second minute iterate.
        # if (self.time_manager.get_current_minute() == 30 & self.isGoldenGooseTimeMarker1):
        #     self.isGoldenGooseTimeMarker1 = False
        #     self.isGoldenGooseTimeMarker2 = True
        #     self.process_async_top_stock_phase1_internal()
        #     # self.is_start_yet_to_be_initiated = False
        #
        # #Third minute iterate.
        # if (self.time_manager.get_current_minute() == 31 & self.isGoldenGooseTimeMarker2):
        #     self.isGoldenGooseTimeMarker1 = True
        #     self.isGoldenGooseTimeMarker2 = False
        #     self.initiate_process_top_stock_bird()
        #
        #
        #

        #Iterate through whole, receiving Neo bird GGResult, processing and then rotation.
            #Follow time
        if (self.is_start_yet_to_be_initiated and self.calculate_time_delimiter_start()):
            self.process_async_top_stock_phase1_internal()
            self.is_start_yet_to_be_initiated = False

        #Scrape discontinued for now
        # if(self.is_scrape_yet_to_be_initiated and self.calculate_time_delimiter_process_scrape_top_stock_list_dow_volume_industry()):
        #     self.initiate_process_top_stocks_scrape()
        #     self.is_scrape_yet_to_be_initiated = False

        if (self.is_top_stock_bird_yet_to_be_initiated and self.calculate_time_delimiter_top_stock_bird()):
            print("We're getting a bird!")
            self.initiate_process_top_stock_bird()
            self.is_top_stock_bird_yet_to_be_initiated = False

        #TSP pull initial, stock moves, bird_TSP pulled process Neo Linked
            #



        # if (self.is_condition_end_of_day != True and self.calculate_time_delimiter_stop_time()):
        #     self.reset_procedure()
        #     self.is_condition_end_of_day = True




         # Moirae phase one 8;31
        # if (self.is_condition_moirae_phase_one != True and self.calculate_time_delimiter_moirae_phase_one()):
        #     print('Moirae phase one')
        #     # Update Data_Decision_Process_Action_Manager with chosen stocks
        #     self.create_appendage_top_stock_pull_list_one()
        #     self.is_condition_moirae_phase_one = True
        #
        # # Moirae phase two 9:28
        # if (self.is_condition_moirae_phase_two != True and self.calculate_time_delimiter_moirae_phase_two()):
        #     #transfer list tsp_1_chosen_stocks (list of liata) dm, values)
        #     print('Moirae phase two')
        #     #Reset type_converter calculated values
        #     self.type_converter.reset_instance_values()
        #     #TSP pull
        #     self.event_trigger_top_stock_gather_process_phase_two()
        #     self.is_condition_moirae_phase_two = True
        #
        # # Moirae phase three 9:29
        # if (self.is_condition_moirae_phase_three != True and self.calculate_time_delimiter_moirae_phase_three()):
        #     print('Moirae phase three')
        #     #Create appendaged list
        #     self.create_appendage_top_stock_pull_list_two()
        #     self.associate_appendage_top_stock_pull_list_to_day_decision_process_action_manager()
        #
        #     self.day_decision_process_action_manager.email_end_of_day_results(self.email_manager)
        #     self.is_condition_moirae_phase_three = True


        # 9:30 conditional begin sell analytics
        # if (self.is_condition_two_met != True and self.calculate_time_delimiter_two()):
        #     if(self.day_decision_process_action_manager.is_stock_bought() != True):
        #         self.event_trigger_trade_time_buy_end(self.top_stock_chosen)
        #         self.event_trigger_buy_analysis_process_end()
        #     self.is_condition_two_met = True



        # # 11:30 conditional end sell analytics
        # if (self.is_condition_three_met != True and self.calculate_time_delimiter_three()):
        #     print('Bought data_manager "hard" sell time')
        #     self.event_trigger_trade_time_sell()
        #     self.is_condition_three_met = True
        #
        #
        #
        # End of day / Capture analytics and Reset




    # Support needed
    # TDS call passing type of set, hour/tm/fm
    def update_data_mananager_request_bundle_time_data_set_fields(self, type):
        print("incoming type: "+type)
        for data_manager in self.get_list_chosen_data_manager():
            data_manager.get_data_manager_request_bundler().process_changeover(type)

    def create_appendage_top_stock_pull_list_one(self):
        #for each data_manager in data_manager_list package in list to be analyzed by DDPAM
        for data_manager in self.get_list_chosen_data_manager():
            current_stock = data_manager.get_data_controller().get_current_stock()
            #Conditional that data_controller data_pull process initialized
            self.list_top_stock_pull_one.append([data_manager,current_stock.get_sym(),current_stock.get_last(),current_stock.get_pchg()])

    def create_appendage_top_stock_pull_list_two(self):
        #for each data_manager in data_manager_list package in list to be analyzed by DDPAM
        for data_manager in self.get_list_chosen_data_manager():
            current_stock = data_manager.get_data_controller().get_current_stock()
            #Conditional that data_controller data_pull process initialized
            self.list_top_stock_pull_two.append([data_manager,current_stock.get_sym(),current_stock.get_last(),current_stock.get_pchg()])

    def associate_appendage_top_stock_pull_list_to_day_decision_process_action_manager(self):
        self.day_decision_process_action_manager.associate_top_stock_pull_lists(self.list_top_stock_pull_one,self.list_top_stock_pull_two)





    def calculate_time_delimiter_start(self):
        print(self.time_manager.get_current_hour())
        if(self.time_manager.get_current_hour() == self.start_hour):
            if (self.time_manager.get_current_minute() == self.start_minute):
                return True
        return False


    def calculate_time_delimiter_process_scrape_top_stock_list_dow_volume_industry(self):
        print(self.time_manager.get_current_hour())
        if(self.time_manager.get_current_hour() == self.scrape_hour):
            if (self.time_manager.get_current_minute() == self.scrape_minute):
                return True
        return False

    def calculate_time_delimiter_top_stock_bird(self):
        print(self.time_manager.get_current_hour())
        if(self.time_manager.get_current_hour() == self.top_stock_bird_hour):
            if (self.time_manager.get_current_minute() == self.top_stock_bird_minute):
                return True
        return False





    # def calculate_time_delimiter_stop(self):
    #     if(self.time_manager.get_current_hour() == self.start_hour):
    #         if (self.time_manager.get_current_minute() == self.start_minute):
    #             return True
    #     return False


    # def calculate_time_delimiter_top_stock_pull_gather(self):
    #     if(self.time_manager.get_current_hour() == self.start_hour):
    #         if (self.time_manager.get_current_minute() == self.start_minute):
    #             return True
    #     return False

    def calculate_time_delimiter_moirae_phase_one(self):
        if(self.time_manager.get_current_hour() == (self.start_hour)):
            if (self.time_manager.get_current_minute() == (self.start_minute)):
                return True
        return False
    def calculate_time_delimiter_moirae_phase_two(self):
        if(self.time_manager.get_current_hour() == (self.start_hour)):
            if (self.time_manager.get_current_minute() == (self.start_minute + 2)):
                return True
        return False

    def calculate_time_delimiter_moirae_phase_three(self):
        if(self.time_manager.get_current_hour() == (self.start_hour)):
            if (self.time_manager.get_current_minute() == (self.start_minute + 3)):
                return True
        return False



    def calculate_time_delimiter_two(self):
        if (self.time_manager.get_current_hour() == 9):
            if (self.time_manager.get_current_minute() == 30):
                return True
        return False

    def calculate_time_delimiter_three(self):
        if (self.time_manager.get_current_hour() == 11):
            if (self.time_manager.get_current_minute() == 21):
                return True
        return False

    def calculate_time_delimiter_four(self):
        if (self.time_manager.get_current_hour() == 23):
            if (self.time_manager.get_current_minute() == 46):
                return True
        return False



    #Event conditionals
    def event_trigger_top_stock_gather_process_phase_one(self):
        self.process_async_top_stock_phase1_internal()
        # self.initiate_monitor_odin_algorithm()
        # self.process_chosen_to_bought_calculation()

    def event_trigger_buy_analysis_process(self):
        self.perpetual_timer_buy_analysis.setup_timer_stock(3, 1000,
                                                            self.process_algorithm_filter_highest_chosen_data_manager,
                                                            'Ra_buy_analysis')

    def event_trigger_buy(self):
        self.perform_chosen_stock_trade()

    def event_trigger_buy_analysis_process_end(self, data):
        # End buy analytics
        # Update DDMA process
        # self.process_async_phase1_market_buy(data)
        # Begin sell analytics process

        # operation_center.process_algorithm_determine_highest_chosen_data_manager()

        # Upon buy analytics time end / call to Odin algorithm end Ra_Algo loop
        self.end_ra_analytics()

    def event_trigger_sell_analysis_process(self):
        return ''

    def event_trigger_sell_analysis_process_end(self):
        return ''


    def end_ra_analytics(self):
        self.perpetual_timer_buy_analysis.cancel()



    def event_trigger_trade_time_sell(self):
        # trade
        # update stock query mechanism
        # update DM_Action
        self.process_async_phase2_market_sell()


    # Query route payload query response
    def process_async_top_stock_phase1_internal(self):
        self.task_master.create_thread_async_top_stock_phase_internal()

    # Route relayed from internal request
    def process_async_top_stock_phase1(self, query):
        self.task_master.create_thread_async_top_stock_phase1(query)

    def process_async_top_stock_phase2(self, query):
        self.task_master.create_thread_async_top_stock_phase2(query)



    #Chosen selection process
    #Support needed
    def process_chosen_data_manager_selection(self):
        self.task_master.create_thread_async_chosen_data_manager_selection(query)

    def process_algorithm_filter_highest_chosen_data_manager(self):
        self.ra_algorithm.algorithm_filter_highest_chosen_data_manager(self,self.get_list_chosen_data_manager(),self.stock_statistics_composite)

    # Query
    def process_async_query_stock_phase1(self, query):
        self.task_master.create_thread_async_query_stock_phase1(query)

    def process_async_query_symbol(self, query):
        self.task_master.create_thread_async_query_symbol(query)

    # DM Query intake
    def process_async_DM_stock_creation(self, query):
        self.task_master.create_thread_async_DM_stock_creation(query)

    # DM type creation process
    # Extended DM Creation
    def process_async_assemble_extended_data_manager(self, sym):
        self.task_master.create_thread_async_assemble_extended_data_manager(sym)

    def process_async_initiate_extended_data_manager(self, data_manager):
        self.task_master.create_thread_async_initiate_extended_data_manager(data_manager)

    # Chosen DM Creation
    def process_async_assemble_chosen_data_manager(self, sym_list):
        self.task_master.create_thread_async_assemble_chosen_data_manager(sym_list)

    def process_async_initiate_chosen_data_manager(self):
        self.task_master.create_thread_async_initiate_chosen_data_manager(self.top_stock_monument_composite.get_top_stock_data_manager_monument_list())

    # Bought DM Creation
    def process_async_assemble_bought_data_manager(self):
        self.task_master.create_thread_async_assemble_bought_data_manager(self.data_manager_action)

    def process_async_initiate_bought_data_manager(self, data_manager):
        self.task_master.create_thread_async_initiate_bought_data_manager(data_manager)

    # Intake request, post to node phase 2 buy sequence, payload chosen stock symbol
    def process_async_phase1_market_buy(self):
        self.task_master.create_thread_async_phase1_market_buy()

    # Node handled
    def process_async_phase2_market_buy(self, query):
        self.task_master.create_thread_async_phase2_market_buy(query)

    def process_async_phase3_market_buy(self, query):
        self.task_master.create_thread_async_phase3_market_buy(query)

    # sell
    def process_async_phase1_market_sell(self):
        self.task_master.create_thread_async_phase1_market_sell()

    def process_async_phase2_market_sell(self, query):
        self.task_master.create_thread_async_phase2_market_sell(query)

    def process_async_phase3_market_sell(self, query):
        self.task_master.create_thread_async_phase3_market_sell(query)

    # account
    def process_async_phase2_account(self, data):
        self.task_master.create_thread_async_phase2_account(data)

    def process_async_phase3_account(self, data):
        self.task_master.create_thread_async_phase3_account(data)

    # Data_Manager control
    def process_async_assemble_top_data_managers(self):
        print('assemble top data account')
        self.task_master.create_thread_async_assemble_top_data_managers()

    def process_async_initiate_top_data_managers(self):
        self.task_master.create_thread_async_initiate_top_data_managers()

    def process_async_assemble_data_manager(self):
        self.task_master.create_thread_async_assemble_data_manager()

    def process_async_initiate_data_manager(self, data_manager):
        self.task_master.create_thread_async_initiate_data_manager()


    # Day_Decision_Process_Action_Manager decision process
    def process_chosen_to_bought_calculation(self):
        self.day_decision_process_action_manager.calculate_determine_highest_chosen_data_manager(self.get_list_chosen_data_manager())


    # BUY PROCEDURE #
    #Pre buy analytics
    # def initiate_monitor_odin_algorithm(self):
    #     # self.odin_algorithm.initiate_buy_monitor_chosen(self)
    #     # Support for delay in initiation


    def process_stock_statistics_to_database(self,stock_statistics_composite):
        #Stat object to DB
        #Support for async handling
        self.node_manager.async_post_stock_statistics_composite(stock_statistics_composite)
    #Pre buy measure
    def perform_chosen_stock_trade(self,stat_list):
        # Buy stock procedure
        # Handle on Day_Decision_Process_Action_Manager update
        self.trade_manager.buy_stock_full_amount(self,stat_list)

    #Post buy
    def process_transform_chosen_to_bought(self):

        self.process_async_assemble_bought_data_manager()



    #SELL PROCEDURE
    #Pre sell analytics
    def sell_stock(self):
        self.trade_manager.sell_stock_full_amount()

    def store_data_manager_action_to_database(self):
        #Stat object to DB
        #Support for async handling
        self.node_manager.async_post_data_manager_action(self.get_data_manager_action())


    #Case Analytics
    #Case condition 1
    def process_async_case_one(self):
        #Update Chosen Stat object with index of chosen stock
        self.process_algorithm_determine_highest_chosen_data_manager()
        if(self.stock_statistics_composite.get_chosen_index != None):
            self.ra_algorithm.algorithm_test_against_buy_metrics(self.stock_statistics_composite)



    #Buy condition
    def process_async_case_two(self):


        return ''
    def process_async_case_three(self):
        return ''





    #Timer processes
    def process_async_buy_timer_delimiter(self):
        self.task_master.create_thread_async_buy_timer_delimiter()

    def process_async_sell_timer_delimiter(self):
        self.task_master.create_thread_async_sell_timer_delimiter()

    def add_stock_composite_to_top_composite(self, stock_composite):
        self.get_top_stock_composite().get_list_stock_composites().append(stock_composite)
        # stock_composite





    #End of Day
    #Capture Analytics
    def capture_analytics_data_manager_action(self):
        self.day_decision_process_action_manager.capture_analytics_data_manager_action()
        self.day_decision_process_action_manager.store_data_manager_action_process()
    #Reset
    def reset_procedure(self):
        for dm in self.get_list_chosen_data_manager():
            dm.clear_perpetual_timers()
        self.get_list_chosen_data_manager().clear()
        self.perpetual_timer_main_process_loop.cancel()
        self.time_data_set_manager.perpetual_timer_time_monite_loop.cancel()

        self.is_condition_top_stock_pull_gather = False
        self.is_condition_moirae_phase_one = False
        self.is_condition_moirae_phase_two = False
        self.is_condition_moirae_phase_three = False
        self.is_condition_end_of_day = False








    # Garbage collect old chosen_data_managers
    def cancel_chosen_query_collection_processes(self):
        # for chosen_stock in self.get_list_chosen_data_manager()
        #     chosen_stock.cancel
        pass


    def get_data_manager_request_bundler(self):
        return self.data_manager_request_bundler

    def generate_stock_composite(self, symbol):
        stock_composite_generated = Stock_Composite()

        # label and tag stockComposite
        stock_composite_generated.set_generationIteration(self.stock_composite_generation_iteration)
        stock_composite_generated.set_name(symbol)

        self.stock_composite_generation_iteration = (self.stock_composite_generation_iteration + 1)

        return stock_composite_generated

    def get_list_stock_composite(self):
        return self.list_stock_composite

    def get_list_top_stock_composite(self):
        return self.list_top_stock_composite

    def get_list_top_stock_symbols(self):
        return self.list_top_stock_symbols

    def get_top_stock_composite(self):
        return self.top_stock_composite

    def get_data_manager_action(self):
        return self.data_manager_action

    def get_list_data_managers(self):
        return self.list_data_managers

    def get_list_extended_data_manager(self):
        return self.list_extended_data_manager

    def get_list_chosen_data_manager(self):
        return self.list_chosen_data_manager

    def get_list_bought_data_manager(self):
        return self.list_bought_data_manager

    def get_time_data_set_manager(self):
        return self.time_data_set_manager

    def get_data_manager_request_bundler(self):
        return self.data_manager_request_bundler

    def get_top_stock_monument_composite(self):
        return self.top_stock_monument_composite



    # def initiate_process_top_stocks_scrape(self):
    #     # self.data_manager_request_bundler.create_scrape_bundle_request(["aapl", "nvda", "ko"])
    #
    #     self.perpetual_timer_process_scrape_top_stock_list_dow_volume_industry.setup_timer_stock(1, 500, self.process_scrape_top_stock_list_dow_volume_industry,
    #                                                                                    'process_scrape_top_stock_list_dow_volume_industry')
    # support Individual self.day_decision_process_action_manager action
    def process_scrape_top_stock_list_dow_volume_industry(self):
        list_of_symbols = self.top_stock_monument_composite.process_get_top_stock_data_manager_monument_symbol_list()
        self.data_manager_request_bundler.create_scrape_bundle_request(list_of_symbols)

    def initiate_process_top_stock_bird(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(self.node_manager.async_bird_messenger_top_stock_process_complete());