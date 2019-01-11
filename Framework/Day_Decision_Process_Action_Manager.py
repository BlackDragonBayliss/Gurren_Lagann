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
            self.list_top_stock_pull_one = []
            self.list_top_stock_pull_two = []
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

    def associate_top_stock_pull_lists(self, list_top_stock_pull_one, list_top_stock_pull_two):
        self.list_top_stock_pull_one = list_top_stock_pull_one
        self.list_top_stock_pull_two = list_top_stock_pull_two


    def create_chosen_lists_json(self):
        #Handle on list one value
        #data_manager,current_stock.get_name(),current_stock.get_last(),current_stock.get_pchg()
        chosen_list_one_item_one = self.list_top_stock_pull_one[0]
        chosen_list_one_item_two = self.list_top_stock_pull_one[1]
        chosen_list_one_item_three = self.list_top_stock_pull_one[2]

        chosen_list_two_item_one = self.list_top_stock_pull_two[0]
        chosen_list_two_item_two = self.list_top_stock_pull_two[1]
        chosen_list_two_item_three = self.list_top_stock_pull_two[2]


        json_data = {"sym_1_1": chosen_list_one_item_one[1],
                     "last_1_1": chosen_list_one_item_one[2],
                     "pchg_1_1": chosen_list_one_item_one[3],

                     "sym_1_2": chosen_list_one_item_two[1],
                     "last_1_2": chosen_list_one_item_two[2],
                     "pchg_1_2": chosen_list_one_item_two[3],

                     "sym_1_3": chosen_list_one_item_three[1],
                     "last_1_3": chosen_list_one_item_three[2],
                     "pchg_1_3": chosen_list_one_item_three[3],


                     "sym_2_1": chosen_list_two_item_one[1],
                     "last_2_1": chosen_list_two_item_one[2],
                     "pchg_2_1": chosen_list_two_item_one[3],

                     "sym_2_2": chosen_list_two_item_two[1],
                     "last_2_2": chosen_list_two_item_two[2],
                     "pchg_2_2": chosen_list_two_item_two[3],

                     "sym_2_3": chosen_list_two_item_three[1],
                     "last_2_3": chosen_list_two_item_three[2],
                     "pchg_2_3": chosen_list_two_item_three[3]

                     }
        print(json_data)
        return json_data


    def email_end_of_day_results(self, email_manager):
        json_data = self.create_chosen_lists_json()
        print("hit email")
        email_manager.send_end_of_day_results(json_data)
