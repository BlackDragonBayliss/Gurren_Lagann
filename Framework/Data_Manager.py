from abc import ABC, abstractmethod

from Time_Manager import Time_Manager
from Time_Data_Set_Manager import Time_Data_Set_Manager
from Time_Data_Set_Controller import Time_Data_Set_Controller
from Data_Controller_Factory import Data_Controller_Factory
from Perpetual_Timer import Perpetual_Timer
from Node_Manager import Node_Manager
from Task_Master import Task_Master


class Data_Manager(ABC):
    global_generation_ID = 0

    def __init__(self, sym, algo_case, operation_center, data_manager_request_bundler, time_data_set_manager):
        self.ID = self.global_generation_ID
        self.global_generation_ID += 1
        self.algo = algo_case
        self.sym = sym
        self.operation_center = operation_center
        self.data_manager_request_bundler = data_manager_request_bundler
        self.time_data_set_manager = time_data_set_manager
        self.time_manager = Time_Manager()
        self.time_data_set_manager = Time_Data_Set_Manager()
        self.data_controller_factory = Data_Controller_Factory()
        self.data_controller = self.data_controller_factory.create_data_controller(self, 0, algo_case)
        self.perpetual_timer_data_pull = Perpetual_Timer()
        self.perpetual_timer_data_analytics = Perpetual_Timer()
        self.time_data_set_controller = self.time_data_set_manager.register_time_data_set_controller(
            self.get_global_generation_ID())
        self.node_manager = Node_Manager()
        self.task_master = Task_Master()
        self.stock_bound_iteration = 0
        self.current_stock = None
        self.handle_stock_process_not_initiated = True

    def bind_data_object(self, stock):
        self.stock_bound_iteration += 1
        self.current_stock = stock
        print('current stock = ', self.current_stock.get_name(), self.current_stock.get_last())

    @abstractmethod
    def init_data_processing(self):
        pass

    def data_controller_processing(self):
        # Based off of timer, time changes, call appropriate DM_C time shifts
        self.data_controller.init_processing()

    def data_pull(self):
        self.task_master.data_manager_query_stock_loop(self)

    def handle_stock_retrieval(self, stock):
        self.get_data_controller().handle_stock_retrieval(stock)
        print('inc stock last:', stock.get_last())

    def update_package_bundler(self, stock):
        self.operation_center.get_data_manager_request_bundler().update_chosen_stock_temp_container(stock)

    def cancel_all_data_controller_processes(self, process):
        return ''

    def cancel_data_controller_process(self, process):
        return ''

    def get_global_generation_ID(self):
        return self.global_generation_ID

    def get_sym(self):
        return self.sym

    def get_data_manager_type(self):
        return self.data_manager_type

    def set_data_manager_type(self, data_manager_type):
        self.data_manager_type = data_manager_type

    def get_operation_center(self):
        return self.operation_center

    def get_data_controller(self):
        return self.data_controller

    def get_time_data_set_manager(self):
        return self.time_data_set_manager

    def get_data_manager_request_bundler(self):
        return self.data_manager_request_bundler
