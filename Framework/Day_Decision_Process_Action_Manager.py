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
