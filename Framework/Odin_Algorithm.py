
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

