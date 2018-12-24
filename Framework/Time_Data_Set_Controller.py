from Time_Manager import Time_Manager
from Five_Minute_Set import Five_Minute_Set
from Ten_Minute_Set import Ten_Minute_Set
from Hour_Set import Hour_Set
from Day_Set import Day_Set


class Time_Data_Set_Controller:
    def __init__(self, ID, created_time):
        self.ID = ID
        self.created_time = created_time
        self.time_manager = Time_Manager()
        self.five_minute_store = []
        self.current_five_minute_set = Five_Minute_Set(created_time)
        self.current_ten_minute_set = Ten_Minute_Set(created_time)
        self.current_hour_set = Hour_Set(created_time)
        self.current_day_set = Day_Set(created_time)

        self.current_day_set.get_list_hour_set_container().append(self.current_hour_set)
        self.current_hour_set.get_list_ten_minute_set_container().append(self.current_ten_minute_set)
        self.current_ten_minute_set.get_list_five_minute_set_container().append(self.current_five_minute_set)

    # Stores record of each FM set
    def add_five_minute_to_store(self):
        self.five_minute_store.append(self.get_current_five_minute_set())

    # Time shifts managed by Time_Data_Set_Manager
    def five_minute_shift(self):
        print("FM shift, printing contents:", self.get_current_five_minute_set().get_list_stock_container())
        self.current_ten_minute_set.get_list_five_minute_set_container().append(self.get_current_five_minute_set())
        self.current_five_minute_set = Five_Minute_Set(self.time_manager.get_current_epoch_time())

    def ten_minute_shift(self):
        print("TM shift, printing index of FM's:",
              len(self.get_current_ten_minute_set().get_list_five_minute_set_container()))
        self.current_hour_set.get_list_ten_minute_set_container().append(self.current_ten_minute_set)
        self.current_ten_minute_set = Ten_Minute_Set(self.time_manager.get_current_epoch_time())

    def hour_shift(self):
        print("H shift, printing index of TM's:", len(self.get_current_hour_set().get_list_ten_minute_set_container()))
        self.current_day_set.get_list_hour_set_container().append(self.current_hour_set)
        self.current_hour_set = Hour_Set(self.time_manager.get_current_epoch_time())

    def get_ID(self):
        return self.ID

    def get_created_time(self):
        return self.created_time

    # Data sets will need to be obtained and used by Data_Controller
    def get_current_five_minute_set(self):
        return self.current_five_minute_set

    def get_current_ten_minute_set(self):
        return self.current_ten_minute_set

    def get_current_hour_set(self):
        return self.current_hour_set

    def get_five_minute_store(self):
        return self.five_minute_store
