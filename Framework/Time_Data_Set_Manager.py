import calendar, time
from Time_Data_Set_Controller import Time_Data_Set_Controller
from Time_Manager import Time_Manager
from Perpetual_Timer import Perpetual_Timer


# Manage time set changeovers for registered Time_Data_Set_Controllers.
class Time_Data_Set_Manager:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.time_manager = Time_Manager()
            self.list_time_data_set_controllers = []
            self.current_minute = None
            self.current_hour = None
            self.previous_minute = None
            self.previous_hour = None
            self.perpetual_timer = Perpetual_Timer()
            # self.init_time_monitoring()
        return self.__instance

    def init_time_monitoring(self):
        self.perpetual_timer.setup_timer_stock(1, 1000000, self.time_monitor_loop, 'time_monitor_loop')

    # Loop time interval check conditions for data_set swap
    def time_monitor_loop(self):
        print("time looping")

        self.current_minute = self.time_manager.get_current_second()
        self.current_hour = self.time_manager.get_current_minute()

        # print("time_monitor current second", self.current_second)
        print("time_monitor current min", self.current_minute)
        print("time_monitor current hour", self.current_hour)
        self.calculate_hour_change()
        self.calculate_five_minute_change()
            # support pause time interval change

    # calculate time sets
    def calculate_hour_change(self):
        # print("calculating hour change")
        if (self.previous_hour == None):
            print("INIT setting hour change")
            self.previous_hour = self.current_hour
            return False
        if (self.current_hour != self.previous_hour):
            self.previous_hour = self.current_hour
            print('hour timeshift')
            self.time_shift_one_hour()
            return True
        return False

    def calculate_five_minute_change(self):
        # print("calculating five minute change")
        if (self.previous_minute == None):
            print("INIT setting minute change")
            self.previous_minute = self.current_minute
            return False
        if (self.current_minute != self.previous_minute):
            if (self.current_minute % 5 == 0):
                print('five_minute timeshift')

                if (self.current_minute % 10 == 0):
                    print("ten_minute time_shift")
                    self.time_shift_ten_minute()
                    self.time_shift_five_minute()
                    self.current_minute = self.previous_minute
                    return True

                self.time_shift_five_minute()
                self.current_minute = self.previous_minute
                return True

        return False

    # PARAM ID: Data_Manager generation ID
    def register_time_data_set_controller(self, ID):
        print('TDS incoming global generation:', ID)
        epoch_time = self.time_manager.get_current_epoch_time()
        time_data_set_controller = Time_Data_Set_Controller(ID, epoch_time)
        # Upon TDSC instantiation, store initial FM set
        time_data_set_controller.add_five_minute_to_store()
        self.list_time_data_set_controllers.append(time_data_set_controller)
        return time_data_set_controller


    def time_shift_five_minute(self):
        for time_data_set_controller in self.list_time_data_set_controllers:
            time_data_set_controller.five_minute_shift()
            time_data_set_controller.add_five_minute_to_store()

    def time_shift_ten_minute(self):
        for time_data_set_controller in self.list_time_data_set_controllers:
            time_data_set_controller.ten_minute_shift()

    def time_shift_one_hour(self):
        for time_data_set_controller in self.list_time_data_set_controllers:
            time_data_set_controller.hour_shift()
