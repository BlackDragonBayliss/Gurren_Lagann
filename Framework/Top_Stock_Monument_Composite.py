from Stock import Stock


class Top_Stock_Monument_Composite:

    def __init__(self):
        self.top_stock_data_manager_monument_list = []

    def replace_at_index_top_stock_monument_composite(self, index_replacement_list_composite):
        # internal_index = 0
        for index_replacement_list in index_replacement_list_composite:
            self.top_stock_monument_list[index_replacement_list[0]] = index_replacement_list[1]
            # internal_index += 1

    def add_to_top_stock_data_manager_monument_list(self, top_stock_data_manager):
        self.top_stock_data_manager_monument_list.append(top_stock_data_manager)

    def set_top_stock_data_manager_monument_list(self, top_stock_data_manager_monument_list):
        self.top_stock_data_manager_monument_list = top_stock_data_manager_monument_list

    def get_top_stock_data_manager_monument_list(self):
        return self.top_stock_data_manager_monument_list
