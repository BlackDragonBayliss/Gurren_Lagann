from Data_Manager import Data_Manager


class Bought_Data_Manager(Data_Manager):
    global_generation_ID = 0

    def __init__(self, sym, algo_case, operation_center):
        super().__init__(sym, algo_case, operation_center)
        super().set_data_manager_type('Bought')

    def init_data_processing(self):
        print("init", self.sym)
        self.perpetual_timer_data_pull.setup_timer_stock(1, 1000, super().data_pull, 'data_pull')

        self.perpetual_timer_data_analytics.setup_timer_stock(1, 1000,
                                                              super().get_data_controller().loop_operation_analytics,
                                                              'analytics')

    def test_print(self):
        print(super().get_data_manager_type())


def sell_stock_operation(self):
    print("selling stock")
