from Data_Manager import Data_Manager


class Extended_Data_Manager(Data_Manager):
    # global_generation_ID = 0
    # name = 'child'
    def __init__(self, sym, algo_case):
        super().__init__(sym, algo_case)
        super().set_data_manager_type('Extended_DM')

    def init_data_processing(self):
        self.perpetual_timer_data_pull.setup_timer_stock(1, 1000, super().data_pull, 'data_pull')
        print("init",self.sym)
        #def setup_timer_stock(self, delay, countToEnd, functionToInvoke, name):

    def test_print(self):
        # print(self.get_sym())
        print(super().get_data_manager_type())
        # print(super().name)