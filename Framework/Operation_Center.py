import sched, time
from HTTP_Utility import HTTP_Utility
from Top_Stock_Composite import Top_Stock_Composite
from Stock_Composite import Stock_Composite
from Request_Factory import Request_Factory
from Type_Converter import Type_Converter
from Task_Master import Task_Master
from Thread_Factory import Thread_Factory
from Perpetual_Timer import Perpetual_Timer
from Thread_Manager import Thread_Manager
from Stock_Composite_Manager import Stock_Composite_Manager
from Data_Manager_Action import Data_Manager_Action
from Time_Manager import Time_Manager
from Time_Data_Set_Manager import Time_Data_Set_Manager
from Node_Manager import Node_Manager
from Day_Decision_Process_Action_Manager import Day_Decision_Process_Action_Manager
from Day_Decision_Process_Storage_Manager import Day_Decision_Process_Storage_Manager
from Stock_Statistics_Composite import Stock_Statistics_Composite
from Trade_Manager import Trade_Manager
from Email_Manager import Email_Manager
from Ra_Algorithm import Ra_Algorithm
from Odin_Algorithm import Odin_Algorithm

class Operation_Center:
    list_stock_composite = []
    list_top_stock_symbols = []
    list_top_stock_composite = []
    list_data_managers = []
    list_extended_data_manager = []
    list_chosen_data_manager = []
    list_bought_data_manager = []

    top_stock_composite = Top_Stock_Composite()
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
            self.top_stock_composite = Top_Stock_Composite()
            self.perpetual_timer = Perpetual_Timer()
            self.thread_manager = Thread_Manager()
            self.stock_composite_manager = Stock_Composite_Manager()
            self.data_manager_action = Data_Manager_Action()
            self.node_manager = Node_Manager()

            self.time_manager = Time_Manager()
            self.time_data_set_manager = Time_Data_Set_Manager()
            self.day_decision_process_action_manager = Day_Decision_Process_Action_Manager()
            self.day_decision_process_storage_manager = Day_Decision_Process_Storage_Manager()
            self.stock_statistics_composite = Stock_Statistics_Composite
            self.trade_manager = Trade_Manager()
            self.email_manager = Email_Manager()
            self.ra_algorithm = Ra_Algorithm()
            self.odin_algorithm = Odin_Algorithm()
            self.task_master = Task_Master()
            self.task_master.setup_instance(self.__instance, self.thread_factory, self.http_utility,
                                            self.request_factory,
                                            self.type_converter, self.top_stock_composite, self.perpetual_timer,
                                            self.thread_manager, self.stock_composite_manager, self.data_manager_action,
                                            self.node_manager, self.time_manager,
                                            self.time_data_set_manager, self.day_decision_process_action_manager,
                                            self.day_decision_process_storage_manager)
            self.is_condition_one_met = False
            self.is_condition_two_met = False
            self.is_condition_three_met = False

        return self.__instance

    def process_main_process_loop(self):
        self.time_data_set_manager.init_time_monitoring()
        self.main_process_loop()

    def main_process_loop(self):
        # timer condition with perp timer.
        # Init perpetual timer
        # setup funct that will check timer condition in Operation_Center

        # def setup_timer_stock(self, delay, countToEnd, functionToInvoke, name):
        self.perpetual_timer.setup_timer_stock(1, 1000000, self.main_loop, 'main_process_loop')

    def main_loop(self):
        ts = time.time()

        if (self.is_condition_one_met & self.calculate_time_delimiter_one()):
            print('hit first condition')

            #Get handle on process to invoke
            self.event_trigger_top_stock_process()
            self.is_condition_one_met = False

        if (self.is_condition_two_met & self.calculate_time_delimiter_two()):
            print('hit second condition')

            #Get handle on process to invoke
            self.event_trigger_trade_time__buy(self.top_stock_chosen)
            self.is_condition_two_met = False

        if (self.is_condition_three_met & self.calculate_time_delimiter_three()):
            print('hit third condition')

            #Get handle on process to invoke
            self.event_trigger_trade_time_sell()
            self.is_condition_two_met = False



    def calculate_time_delimiter_one(self):
        #Get handle on yourself and on time_manager
        if (self.time_manager.get_current_minute() == 25):
            self.is_condition_one_met = True
            return True
        return False

    def calculate_time_delimiter_two(self):
        if (self.time_manager.get_current_minute() == 26):
            self.is_condition_two_met = True
            return True
        return False

    def calculate_time_delimiter_three(self):
        if (self.time_manager.get_current_minute() == 27):
            self.is_condition_three_met = True
            return True
        return False



    def event_trigger_top_stock_process(self):
        # get top stock data
        # update DM_Action
        # execute buy process, DM_Action_Update chained
        # task_master buy process

        self.process_chosen_to_bought_calculation()


        # self.task_master.
        # self.process_async_top_stock_phase1()

    def event_trigger_trade_time__buy(self, data):
        # Isolate top stock and matching criteria and metrics.
        # trade
        # update DM_Action
        # self.process_async_phase1_market_buy(data)


        return ''

    def event_trigger_trade_time_sell(self):
        # trade
        # update stock query mechanism
        # update DM_Action
        self.process_async_phase2_market_sell()

    def event_trigger_update_DM_action(self):
        return ''



    def process_async_top_stock_phase1_internal(self):
        print("inside process_async_top_stock_phase1_internal")
        self.task_master.create_thread_async_top_stock_phase_internal()

    def process_async_top_stock_phase1(self, query):
        self.task_master.create_thread_async_top_stock_phase1(query)

    def process_async_top_stock_phase2(self, query):
        self.task_master.create_thread_async_top_stock_phase2(query)



    #Chosen selection process
    #Support needed
    def process_chosen_data_manager_selection(self):
        self.task_master.create_thread_async_chosen_data_manager_selection(query)

    def process_algorithm_determine_highest_chosen_data_manager(self):
        self.ra_algorithm.algorithm_determine_highest_chosen_data_manager(self.get_list_chosen_data_manager(),self.stock_statistics_composite)




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

    def process_async_initiate_chosen_data_manager(self, data_manager_list):
        self.task_master.create_thread_async_initiate_chosen_data_manager(data_manager_list)

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
    def process_stock_statistics_to_database(self,stock_statistics_composite):
        #Stat object to DB
        #Support for async handling
        self.node_manager.async_post_stock_statistics_composite(stock_statistics_composite)
    #Pre buy measure
    def perform_chosen_stock_trade(self,stock_statistics_composite):
        # Buy stock procedure
        # Handle on #DM_Action update
        self.trade_manager.buy_stock_full_amount(self,stock_statistics_composite)
    #Post buy
    def process_transform_chosen_to_bought(self):

        #     if(stock_statistics_composite.get_stat_composite(self.stock_statistics_composite.get_chosen_index() == chosen_stock.get_sym())):
        #         #Call dm creation proocess

        # Chosen to DB transformation
        self.process_async_assemble_bought_data_manager()


    # Garbage collect old chosen_data_managers
    def cancel_chosen_stocks:
        # for chosen_stock in self.get_list_chosen_data_manager()
        #     chosen_stock.cancel
        pass

    # SELL PROCEDURE #
    # Pre sell analytics
    def sell_stock(self):
        self.trade_manager.sell_stock_full_amount()




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





    # Timer processes
    def process_async_buy_timer_delimiter(self):
        self.task_master.create_thread_async_buy_timer_delimiter()

    def process_async_sell_timer_delimiter(self):
        self.task_master.create_thread_async_sell_timer_delimiter()

    def add_stock_composite_to_top_composite(self, stock_composite):
        self.get_top_stock_composite().get_list_stock_composites().append(stock_composite)
        # stock_composite

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

    # Return type data account
    def get_list_extended_data_manager(self):
        return self.list_extended_data_manager

    def get_list_chosen_data_manager(self):
        return self.list_chosen_data_manager

    def get_list_bought_data_manager(self):
        return self.list_bought_data_manager
