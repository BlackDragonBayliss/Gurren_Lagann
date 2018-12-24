
# from DM_Buy import DM_Buy
# from Stock import Stock
from Calendar_Tracker import Calendar_Tracker



class Day_Decision_Process_Action_Manager:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.instance_calendar_tracker = Calendar_Tracker()
            # self.chosen_statistics = Chosen_Statistics()
        return self.__instance



    def get_DM_Buy(self):
        return self.DM_Buy

    def set_DM_Buy(self, DM_Buy):
        self.DM_Buy = DM_Buy

    # Analysis question stocks
    def process_check_top_chosen_DM(self):
        return ''

    def process_transfer_case_top_chosen_DM(self):
        return ''

    # Process bought stock, canceling others, init bought - else update DDPA stats, proceeding to DDPS
    def DM_Bought_Assembly(self):
        return ''



    # test_set1 = np.array([20.0, 20.2, 20.04, 20.30])
    #
    # print(create_pchg_value_list(test_set1))
    #
    # five_minute_set = [[20.0], [20.1], [20.15], [20.20], [20.3], [20.4], [20.41]]
    # for val in five_minute_set:
    #     if (calculate_pchg_delimiter_met(20.0, val)):
    #         print("selling stock")
    #     else:
    #         print("value less than delimiter")

