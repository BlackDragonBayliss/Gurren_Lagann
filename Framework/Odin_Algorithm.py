
import numpy as np
from Calendar_Tracker import Calendar_Tracker
from Perpetual_Timer import Perpetual_Timer

#Continuous monitoring algorithm
class Odin_Algorithm:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.instance_calendar_tracker = Calendar_Tracker()
            self.perpetual_timer_monitor_pchg_delimiter = Perpetual_Timer()
            self.is_monitoring = False
            self.max_pchg_difference_baseline = .02
            self.min_pchg_difference_baseline = -.05
            # self.chosen_statistics = Chosen_Statistics()
        return self.__instance

    #Where setup, after DM bought
    # def set_bought_DM()
    #     bought_data_manger
    def initiate_monitor_pchg_delmiter(self,operation_center):
        #Need a handle on bought
        self.trade_manager = operation_center.trade_manager
        self.bought_data_manager = operation_center.get_list_bought_data_manager()
        self.data_action_manager = operation_center.get_data_manager_action()
        self.bought_price = self.bought_data_manager.get_bought_price()
        self.is_monitoring = True
        #Handle pep timer
        self.perpetual_timer_monitor_pchg_delimiter.setup_timer_stock(3, 1000, self.monitor_pchg_delimiter, 'data_pull')

    def monitor_pchg_delimiter(self):
        #pchg calculations
        #handle on bought_data_manager pchg

        #If pchg delimter met: perform sell cancel monitoring process
        if(self.calculate_pchg_delimiter_met() & self.is_monitoring):
            #Cancel monitoring process
            self.is_monitoring = False
            self.perpetual_timer_monitor_pchg_delimiter.cancel()

            #Perform sell procedure
            #Handle on trade_manager
            self.trade_manager.sell_stock()

    def calculate_pchg_delimiter_met(self):
        #Indecision of measure bid vs ask, optimistic trading vs real.
        #Handle on current
        #Handle on baseline
        current_ask = self.bought_data_manager.get_current_ask()
        price_difference = current_ask - self.bought_price

        pchg_difference = price_difference / self.bought_price

        print("Odin pchg_difference",pchg_difference)
        #If greater than or equal to max
        if(pchg_difference >= self.max_pchg_difference_baseline):
            return True
        #If less than or equal to min
        if(pchg_difference  <= self.min_pchg_difference_baseline):
            return True
        return False






    # caclulate highest chosen data_manager
    # Non-continuous
    # def algorithm_determine_highest_chosen_data_manager(self, data_manager_list, stock_statistics_composite,calendar_tracker):
    #     # for data_manager in data_manager_list:
    #     #
    #     # #based on metrics, pchg and volatility, price, determine best choice.
    #     # #later addition consider Day_of_week and can_purchase_day_calculation
    #     # self.calculate_determine_highest_chosen_data_manager(data_manager_list)
    #
    #     #For each chosen in list
    #     for data_manager in data_manager_list:
    #         spread = self.calculate_spread(data_manager_list[0])
    #         latest_stock = data_manager.get_data_controller().get_latest_stock_from_five_minute_set()
    #         #Store in Chosen_Statistics Object
    #         self.chosen_statistics.create_stat(data_manager.get_sym(),latest_stock.get_pchg(),
    #                                            latest_stock.get_last(),spread,calendar_tracker.get_formated_date())
    #         # if day to trade continue calculate chosen index
    #         if (self.calculate_determine_day_to_trade()):
    #             self.calculate_determine_highest_chosen_data_manager(stock_statistics_composite)
    #
    #
    # def calculate_determine_day_to_trade(self):
    #     # Get handle on day of week
    #     current_day = self.instance_calendar_tracker.get_current_day()
    #
    #     # Condition day of week
    #     print("current day",current_day)
    #     if (current_day == 5 or current_day == 6 or current_day == 7):
    #         return False
    #     return True
    #
    # # Non-continuous
    # # determine pchg and spread, optimized solution calculiz
    # def calculate_determine_highest_chosen_data_manager(self, stock_statistics_composite):
    #
    #     stock_stat_one = stock_statistics_composite.get_stat_composite()[0]
    #     stock_stat_two = stock_statistics_composite.get_stat_composite()[1]
    #     stock_stat_three = stock_statistics_composite.get_stat_composite()[2]
    #
    #
    #     pchg_1 = stock_stat_one.get_pchg()
    #     pchg_2 = stock_stat_two.get_pchg()
    #     pchg_3 = stock_stat_three.get_pchg()
    #
    #
    #     percentage_list = [pchg_1, pchg_2, pchg_3]
    #     percentage_transformed_list = []
    #
    #     print("Ra_Algorithm list of percentages to be transformed:",percentage_list)
    #
    #     for val in percentage_list:
    #         resultant = (100 * val)
    #         percentage_transformed_list.append(resultant)
    #
    #     sorted_list = sorted(percentage_transformed_list, key=int)
    #     print("Sorted list",sorted_list)
    #     #Will give val at index
    #     current_index = 0
    #     for val in percentage_transformed_list:
    #         if(val == sorted_list[0]):
    #             stock_statistics_composite.set_chosen_index(current_index)
    #         current_index += 1
    #
    #
    #
    #     # Get filtered paramatized data_list
    #     # parameterized_data_list = self.calculate_metrics_data_list()
    #
    #     # Optimize conditions determine best stock
    #     # self.calculate_optimized_chosen_selection(parameterized_data_list)
    #
    # def calculate_spread(self, data_manager):
    #     #Handle on each FM set, generate_five_minute_data_set
    #     data_manager.get_time_data_set_controller().set_five_minute_store(data_manager.get_data_controller().generate_five_minute_data_set())
    #     five_minute_store = data_manager.get_time_data_set_controller().get_five_minute_store()
    #
    #     list_first_index_five_minute_set = []
    #     #List populated with first index of each FM set
    #     for five_minute_set in five_minute_store:
    #         list_first_index_five_minute_set.append(five_minute_set[0].get_last())
    #
    #     #Do we want variance, covariance, std?
    #     spread = np.std(list_first_index_five_minute_set)
    #     # print(np.std(list_first_index_five_minute_set))
    #     return spread
    #
    #
    #
    #
    # def calculate_optimized_chosen_selection(self, parameterized_data_list):
    #
    #     # Handle var instantiation for chosen stocks
    #
    #     chosen_data_set_one = parameterized_data_list[0]
    #     chosen_data_set_two = parameterized_data_list[1]
    #     chosen_data_set_three = parameterized_data_list[2]
    #
    #     spread_one = chosen_data_set_one[0]
    #     spread_two = chosen_data_set_two[0]
    #     spread_three = chosen_data_set_three[0]
    #
    #     pchg_one = chosen_data_set_one[1]
    #     pchg_two = chosen_data_set_two[1]
    #     pchg_three = chosen_data_set_three[1]
    #
    #     # Handle process decision metrics process
    #     # Determine optimum spread and pchg. Need data for selection process to match optimum scenarios.
    #     # Need to hardcode success scenarios, or use machine learning.
    #     # Hardcoding baseline success scenario
    #     baseline_spread = 5
    #     baseline_pchg = .02
    #
    #     # Take value that's closest to desired metrics
    #     # Support for weighted metrics, which metric has higher weight?
    #
    #     # Calculate chosen differences
    #     spread_difference_chosen_one = baseline_spread - spread_one
    #     spread_difference_chosen_two = baseline_spread - spread_two
    #     spread_difference_chosen_three = baseline_spread - spread_three
    #
    #     pchg_difference_chosen_one = baseline_pchg - pchg_one
    #     pchg_difference_chosen_two = baseline_pchg - pchg_two
    #     pchg_difference_chosen_three = baseline_pchg - pchg_three
    #
    #     # Upon getting pchg and spread differences to basline, apply wieghts for decision process.
    #     # Then calculate overall value_of_data_filter_outcome
    #     # Higher value higher worth
    #
    #     # Determine worth metric output, closer to 1 desired matching outcome.
    #     # Closer to 0 farther undesirables
    #
    #     spread_difference_chosen_one
    #
    #     # Basline weights
    #
    #     if (baseline_spread):
    #         return ''
    #     return ''
    #
    # def create_pchg_value_list(test_set):
    #     # Return pchg_list absolute values
    #     pchg_list = []
    #     index_count = 0
    #     current_value = None
    #     previous_value = None
    #     while (index_count < len(test_set)):
    #         current_value = test_set[index_count]
    #         # previous current value measurement difference, add difference to calculation list
    #         if (previous_value == None):
    #             previous_value = current_value
    #             index_count += 1
    #             continue
    #
    #         print("current_value", current_value, "previous_value", previous_value)
    #         pchg_difference = np.absolute(100 * (((current_value - previous_value) / previous_value)))
    #         print("pchg_difference", pchg_difference)
    #         pchg_list.append(pchg_difference)
    #         previous_value = current_value
    #         index_count += 1
    #     return pchg_list
    #
    # # Now given a bought sell point and approximation differences,
    # # Still need to determine spread of of values, of simulated successful test set
    # # Need truthy data. Need to wait till week begins then we can start recording spreads, doing so programmatically and storing data for extra points.
    # # Break here.
    #
    # # Given bought price, calculate when to buy or sell given new code_tool_set
    #
    #
    # # Continuous calculation, given price and current first FM index
    #
    # def calculate_pchg_delimiter_met(bought_price, five_set_set):
    #     # Return pchg_list absolute values
    #     pchg_delimiter = 2.0
    #     is_pchg_delimiter_met = False
    #     five_minute_first_index_value = five_set_set[0]
    #     # previous current value measurement difference, add difference to calculation list
    #
    #     # print("bought_price", bought_price,"five_minute_first_index_value",five_minute_first_index_value)
    #     pchg_difference = np.absolute(100 * (((five_minute_first_index_value - bought_price) / bought_price)))
    #     print("pchg_difference", pchg_difference)
    #
    #     if (pchg_difference >= pchg_delimiter):
    #         is_pchg_delimiter_met = True
    #
    #     return is_pchg_delimiter_met
    #
    #
    # def algorithm_test_against_buy_metrics(self, stock_statistics_composite, operation_center):
    #     # self.chosen_statistics = chosen_statistics
    #     self.chosen_stat = stock_statistics_composite.get_stat_composite()[self.stock_statistics_composite.get_chosen_index()]
    #     self.is_baseline_pchg_met = False
    #     self.is_baseline_last_met = False
    #     self.is_baseline_spread_met = False
    #
    #     self.baseline_pchg = 15
    #     self.baseline_last_max = 25
    #     self.baseline_spread = 1.45
    #
    #     #Set baseline parameters, later support for adjusting metrics dynamically
    #     #Calculate if passing pchg
    #     # if(calculate_passing_pchg(chosen_stat))
    #     if(self.chosen_stat.get_pchg() >= self.baseline_pchg):
    #         is_baseline_pchg_met = True
    #     #Calculate if passing last
    #     if (self.chosen_stat.get_last() >= self.baseline_last_max):
    #         is_baseline_last_met = True
    #     # Calculate if passing spread
    #     if (self.chosen_stat.get_last() >= self.baseline_spread):
    #         is_baseline_spread_met = True
    #
    #     #If passing metrics continue buy process
    #     #Future support for conditional metrics decision making
    #     if(self.is_baseline_pchg_met & self.is_baseline_last_met & self.is_baseline_spread_met):
    #         operation_center.process_stock_statistics_to_database(stock_statistics_composite)
    #         operation_center.perform_chosen_stock_trade(stock_statistics_composite)
    #         # operation_center.cancel_chosen_stocks(stock_statistics_composite)
    #
    # def calculate_stock(self):
    #     return self.stat_composite

