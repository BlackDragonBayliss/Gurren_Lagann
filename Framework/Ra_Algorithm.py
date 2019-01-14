import numpy as np
from Calendar_Tracker import Calendar_Tracker


# Time delimiter buy and select from small batches and sell under metrics conditions met.
class Ra_Algorithm:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.instance_calendar_tracker = Calendar_Tracker()
            self.is_clear_stat_container = True
            self.baseline_price = 25
            self.baseline_pchg = 15
            self.baseline_spread = 3.25
        return self.__instance

    # caclulate highest chosen data_manager
    # Non-continuous
    def algorithm_filter_highest_chosen_data_manager(self, operation_center, data_manager_list,
                                                     stock_statistics_composite,
                                                     calendar_tracker):


        # On condtion met, return highest chosen #ON_MONITORING
            #Update DM_Action chosen based on condition met, or time delimiter

        # #based on metrics, pchg and volatility, price, determine best choice.
        # #later addition consider Day_of_week and can_purchase_day_calculation


        for data_manager in data_manager_list:
            spread = self.calculate_spread(data_manager)
            latest_stock = data_manager.get_data_controller().get_latest_stock_from_five_minute_set()
            # Store in Chosen_Statistics Objects
            stock_statistics_composite.create_stat(data_manager.get_sym(), latest_stock.get_last(),
                                                   latest_stock.get_pchg(),
                                                   spread,
                                                   calendar_tracker.get_formated_date())
            # self.is_first_filter_iteration = False
        self.calculate_is_chosen_selection_delimiter_met(operation_center, stock_statistics_composite)

    def calculate_is_chosen_selection_delimiter_met(self, operation_center, stock_statistics_composite):
        # Deterministic filter process
        for stat_list in stock_statistics_composite:
            self.calculate_optimized_chosen_selection(stat_list)

        # End-outcome decision process
        for stat_list in stock_statistics_composite:
            # If is_chosen_selected True, buy process, end loop.
            if (stat_list.get_is_chosen()):
                operation_center.perform_chosen_stock_trade(stat_list)
                self.is_clear_stat_container = False
        # If is_chosen_selected False, clear data filter composite and continue process
        if (self.is_clear_stat_container):
            stock_statistics_composite.clear_stat_composite()

    def calculate_optimized_chosen_selection(self, stat_list):

        # Run battery of tests for price, pchg, spread into categorization matrices
        list_temp_stat_conditional_determinate = []
        list_temp_stat_conditional_determinate.append(self.calculate_is_baseline_condition_met_price(stat_list[1]))
        list_temp_stat_conditional_determinate.append(self.calculate_is_baseline_condition_met_pchg(stat_list[2]))
        list_temp_stat_conditional_determinate.append(self.calculate_is_baseline_condition_met_spread(stat_list[3]))
        if (list_temp_stat_conditional_determinate[0] & list_temp_stat_conditional_determinate[1] &
                list_temp_stat_conditional_determinate[2]):
            stat_list.append[True]
        else:
            stat_list.append[False]

        # Future support for getting pchg and spread differences to basline, apply wieghts for decision process.
        # Then calculate overall value_of_data_filter_outcome
        # Higher value higher worth
        # Determine worth metric output, closer to 1 desired matching outcome.
        # Closer to 0 farther undesirables

    def calculate_is_baseline_condition_met_price(self, price):
        # If price falls into acceptable range
        if (price < self.baseline_price):
            return True
        return False

    def calculate_is_baseline_condition_met_pchg(self, pchg):
        # If pchg falls into acceptable range
        if (pchg > self.baseline_pchg):
            return True
        return False

    def calculate_is_baseline_condition_met_spread(self, spread):
        # If spread falls into acceptable range
        if (spread < self.baseline_spread):
            return True
        return False

    def calculate_spread(self, data_manager):
        # Handle on each FM set, generate_five_minute_data_set
        data_manager.get_time_data_set_controller().set_five_minute_store(
            data_manager.get_data_controller().generate_five_minute_data_set())
        five_minute_store = data_manager.get_time_data_set_controller().get_five_minute_store()

        list_first_index_five_minute_set = []
        # List populated with first index of each FM set
        for five_minute_set in five_minute_store:
            list_first_index_five_minute_set.append(five_minute_set[0].get_last())

        # Do we want variance, covariance, std?
        spread = np.std(list_first_index_five_minute_set)
        # print(np.std(list_first_index_five_minute_set))
        return spread

    def calculate_determine_day_to_trade(self):
        # Get handle on day of week
        current_day = self.instance_calendar_tracker.get_current_day()

        # Condition day of week
        print("current day", current_day)
        if (current_day == 5 or current_day == 6 or current_day == 7):
            return False
        return True

    def create_pchg_value_list(test_set):
        # Return pchg_list absolute values
        pchg_list = []
        index_count = 0
        current_value = None
        previous_value = None
        while (index_count < len(test_set)):
            current_value = test_set[index_count]
            # previous current value measurement difference, add difference to calculation list
            if (previous_value == None):
                previous_value = current_value
                index_count += 1
                continue

            print("current_value", current_value, "previous_value", previous_value)
            pchg_difference = np.absolute(100 * (((current_value - previous_value) / previous_value)))
            print("pchg_difference", pchg_difference)
            pchg_list.append(pchg_difference)
            previous_value = current_value
            index_count += 1
        return pchg_list

    def calculate_pchg_delimiter_met(bought_price, five_set_set):
        # Return pchg_list absolute values
        pchg_delimiter = 2.0
        is_pchg_delimiter_met = False
        five_minute_first_index_value = five_set_set[0]
        # previous current value measurement difference, add difference to calculation list

        # print("bought_price", bought_price,"five_minute_first_index_value",five_minute_first_index_value)
        pchg_difference = np.absolute(100 * (((five_minute_first_index_value - bought_price) / bought_price)))
        print("pchg_difference", pchg_difference)

        if (pchg_difference >= pchg_delimiter):
            is_pchg_delimiter_met = True

        return is_pchg_delimiter_met

    def algorithm_test_against_buy_metrics(self, stock_statistics_composite, operation_center):
        # self.chosen_statistics = chosen_statistics
        self.chosen_stat = stock_statistics_composite.get_stat_composite()[
            self.stock_statistics_composite.get_chosen_index()]
        self.is_baseline_pchg_met = False
        self.is_baseline_last_met = False
        self.is_baseline_spread_met = False

        self.baseline_pchg = 15
        self.baseline_last_max = 25
        self.baseline_spread = 1.45

        # Set baseline parameters, later support for adjusting metrics dynamically
        # Calculate if passing pchg
        # if(calculate_passing_pchg(chosen_stat))
        if (self.chosen_stat.get_pchg() >= self.baseline_pchg):
            is_baseline_pchg_met = True
        # Calculate if passing last
        if (self.chosen_stat.get_last() >= self.baseline_last_max):
            is_baseline_last_met = True
        # Calculate if passing spread
        if (self.chosen_stat.get_last() >= self.baseline_spread):
            is_baseline_spread_met = True

        # If passing metrics continue buy process
        # Future support for conditional metrics decision making
        if (self.is_baseline_pchg_met & self.is_baseline_last_met & self.is_baseline_spread_met):
            operation_center.process_stock_statistics_to_database(stock_statistics_composite)
            operation_center.perform_chosen_stock_trade(stock_statistics_composite)
            # operation_center.cancel_chosen_stocks(stock_statistics_composite)

    def calculate_stock(self):
        return self.stat_composite
