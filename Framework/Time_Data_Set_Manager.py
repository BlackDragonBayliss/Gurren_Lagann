import calendar, time
from Time_Data_Set_Controller import Time_Data_Set_Controller
from Time_Manager import Time_Manager
from Perpetual_Timer import Perpetual_Timer

class Time_Data_Set_Manager:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.operation_center = None
            self.time_manager = Time_Manager()
            self.list_time_data_set_controllers = []
            self.current_minute = None
            self.current_hour = None
            self.previous_minute = None
            self.previous_hour = None
            self.perpetual_timer = Perpetual_Timer()
            # self.init_time_monitoring()
        return self.__instance

    def init_time_monitoring(self, operation_center):
        self.operation_center = operation_center
        self.perpetual_timer.setup_timer_stock(1, 1000000, self.time_monitor_loop, 'time_monitor_loop')
        print("Time monitor loop initiated")

    # Loop time interval check conditions for data_set swap
    def time_monitor_loop(self):
        self.current_minute = self.time_manager.get_current_second()
        self.current_hour = self.time_manager.get_current_minute()
        print("current_minute: "+str(self.current_minute))
        print("current_hour: " + str(self.current_hour))
        self.calculate_time_change()
        # self.calculate_five_minute_change()

    # calculate time sets
    def calculate_time_change(self):
        if (self.previous_hour == None):
            print("setting previous_hour")
            self.previous_hour = self.current_hour

        if (self.previous_minute == None):
            self.previous_minute = self.current_minute
            return False

        print("current hour: "+str(self.current_hour) + " previous hour: "+str(self.previous_hour) )
        if (self.current_hour != self.previous_hour):
            print("Doing hour set change")
            self.operation_center.update_data_mananager_request_bundle_time_data_set_fields("hour")
            self.previous_hour = self.current_hour
            return True
        # return False

        if (self.current_minute != self.previous_minute):
            if (self.current_minute % 5 == 0):
                # print("calculate five_minute change true")
                if (self.current_minute % 10 == 0):
                    print("Doing ten minute set change")
                    self.operation_center.update_data_mananager_request_bundle_time_data_set_fields("ten")
                    self.current_minute = self.previous_minute
                    return True
                print("Doing five minute set change")
                self.operation_center.update_data_mananager_request_bundle_time_data_set_fields("five")
                self.current_minute = self.previous_minute
                return True
                # self.current_minute = self.previous_minute
        return False

    # def calculate_five_minute_change(self):




    # PARAM ID: Data_Manager generation ID
    def register_time_data_set_controller(self, ID):
        print('TDS incoming global generation:', ID)
        epoch_time = self.time_manager.get_current_epoch_time()
        time_data_set_controller = Time_Data_Set_Controller(ID, epoch_time)
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
