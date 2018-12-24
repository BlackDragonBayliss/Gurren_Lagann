# from Data_Manager import Data_Manager
from Data_Controller import Data_Controller


class Data_Controller_Factory:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
        return self.__instance

    def create_data_controller(self, data_manager, data, case):
        if (case == 0):
            DM_controller_instance = Data_Controller(data_manager)
            return DM_controller_instance
            # if ():
            #     DM_Controller_Instance = DM_Controller(sym)
            #     # DM_Controller_Factory_Instance
            #     return DM_Controller_Instance
            # if ():
            #     DM_Controller_Instance = DM_Controller(sym)
            #     # DM_Controller_Factory_Instance
            #     return DM_Controller_Instance
            # if ():
            #     DM_Controller_Instance = DM_Controller(sym)
            #     # DM_Controller_Factory_Instance
            #     return DM_Controller_Instance
            # if ():
            #     DM_Controller_Instance = DM_Controller(sym)
            #     # DM_Controller_Factory_Instance
            #     return DM_Controller_Instance
        return 0
