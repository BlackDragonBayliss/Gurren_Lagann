from DM_Buy import DM_Buy
class Day_Decision_Process_Storage_Manager:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
        return self.__instance


    def get_DM_Buy (self):
        return self.DM_Buy
    def set_DM_Buy (self, DM_Buy):
        self.DM_Buy = DM_Buy

    #Analysis question stocks
    def process_check_top_chosen_store_DM(self):
        return ''
    def process_transfer_case_top_chosen_DM(self):
        return ''



