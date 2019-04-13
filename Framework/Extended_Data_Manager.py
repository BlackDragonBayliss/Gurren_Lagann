from Data_Manager import Data_Manager
from Perpetual_Timer import Perpetual_Timer

class Extended_Data_Manager(Data_Manager):
    def __init__(self, sym, algo_case, operation_center, time_data_set_manager):
        super().__init__(sym, algo_case, operation_center, time_data_set_manager)
        super().set_data_manager_type('Extended')

    def init_data_processing(self):
        self.perpetual_timer_data_pull.setup_timer_stock(5, 10000, super().data_pull, 'data_pull')
        print("init extend",self.sym)
        self.set_is_running("1")

    def test_print(self):
        print(super().get_data_manager_type())

    def extended_to_chosen_process(self, operation_center):
        # End process
        self.perpetual_timer_data_pull.cancel()
        # Begin second slower process
        # Handle second process

        # operation_center.process_async_assemble_chosen_data_manager(self.get_sym())
        #
        #Create chosen

        operation_center.process_async_assemble_chosen_data_manager(self.sym)
        #Remove self from list, add to chosen list
        # super().set_data_manager_type('Chosen')
        # perpetual_timer = Perpetual_Timer()
        # self.perpetual_timer_container.append(perpetual_timer)
        # perpetual_timer.setup_timer_stock(1, 1000, super().data_pull, 'data_pull_extend')



        # self.perpetual_timer_data_pull.cancel()
        # testing phase