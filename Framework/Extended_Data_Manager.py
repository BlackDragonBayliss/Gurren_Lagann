from Data_Manager import Data_Manager


class Extended_Data_Manager(Data_Manager):
    def __init__(self, sym, algo_case):
        super().__init__(sym, algo_case)
        super().set_data_manager_type('Extended_DM')

    def init_data_processing(self):
        self.perpetual_timer_data_pull.setup_timer_stock(10, 10000, super().data_pull, 'data_pull')
        print("init",self.sym)

    def test_print(self):
        print(super().get_data_manager_type())

    def extended_to_chosen_process(self, operation_center):
        # End process
        self.perpetual_timer_data_pull.cancel()
        # Begin second slower process
        # Handle second process


        operation_center.process_async_assemble_chosen_data_manager(self.get_sym())
        # perpetual_timer = Perpetual_Timer()
        # self.perpetual_timer_container.append(perpetual_timer)
        # self.perpetual_timer_data_pull.setup_timer_stock(10, 1000, super().data_pull, 'data_pull_extend')
        # self.perpetual_timer_data_pull.cancel()
        # testing phase