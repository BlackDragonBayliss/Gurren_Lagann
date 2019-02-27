from Data_Manager import Data_Manager


class Chosen_Data_Manager(Data_Manager):
    global_generation_ID = 0

    def __init__(self, sym, algo_case, operation_center, time_data_set_manager):
        super().__init__(sym, algo_case, operation_center, time_data_set_manager)
        super().set_data_manager_type('Chosen')

    def init_data_processing(self):
        self.perpetual_timer_data_pull.setup_timer_stock(10, 1000, super().data_pull, 'data_pull')

    def test_print(self):
        print(super().get_data_manager_type())


