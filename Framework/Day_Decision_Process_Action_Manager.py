# from Bought_Data_Buy import DM_Buy
# from Stock import Stock
from Data_Manager_Action import Data_Manager_Action
from Calendar_Tracker import Calendar_Tracker


class Day_Decision_Process_Action_Manager:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.data_manager_action = Data_Manager_Action()
            self.instance_calendar_tracker = Calendar_Tracker()
            self.list_chosen_data_manager = []
            # self.chosen_statistics = Chosen_Statistics()
        return self.__instance

    #Depreciated / Bought_Data_Manager stored in Operation_Center

    # Analysis question stocks
    def process_check_top_chosen_DM(self):
        return ''

    def process_transfer_case_top_chosen_DM(self):
        return ''

    # Process bought stock, canceling others, init bought - else update DDPA stats, proceeding to DDPS
    def capture_analytics_data_manager_action(self):
        self.get_data_manager_action()
        #set values

    def store_data_manager_action_process(self, node_manager):
        # node_manager.
        return ''

    def get_data_manager_action(self):
        return self.data_manager_action

    def get_list_chosen_data_manager(self):
        return self.list_chosen_data_manager
    def set_list_chosen_data_manager(self, list_chosen_data_manager):
        self.list_chosen_data_manager = list_chosen_data_manager

    def email_end_of_day_results(self, email_manager):
        print("hit email")
        json_data = {   "sym1": self.get_list_chosen_data_manager()[0].get_sym(),
                        "sym2": self.get_list_chosen_data_manager()[1].get_sym(),
                        "sym3": self.get_list_chosen_data_manager()[2].get_sym()
                        }
        print(json_data)

        email_manager.send_end_of_day_results(json_data)
