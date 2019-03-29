from Data_Manager import Data_Manager


from Perpetual_Timer import Perpetual_Timer

class Chosen_Data_Manager(Data_Manager):
    global_generation_ID = 0

    def __init__(self, sym, algo_case, operation_center, time_data_set_manager):
        super().__init__(sym, algo_case, operation_center, time_data_set_manager)
        super().set_data_manager_type('Chosen')

    def init_data_processing(self):
        self.perpetual_timer_data_pull.setup_timer_stock(10, 1000, super().data_pull, 'data_pull')

    def test_print(self):
        print(super().get_data_manager_type())

    def chosen_extend_process(self):
        #End process
        self.perpetual_timer_data_pull.cancel()
        #Begin second slower process
        #Handle second process

        perpetual_timer = Perpetual_Timer()
        self.perpetual_timer_container.append(perpetual_timer)
        self.perpetual_timer_data_pull.setup_timer_stock(10, 10000, super().data_pull, 'data_pull_extend')
        # self.perpetual_timer_data_pull.cancel()
        #testing phase

