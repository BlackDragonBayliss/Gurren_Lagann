
#ON re


class Data_Manager_Request_Bundler:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.list_chosen_data_managers = []
            self.chosen_stock_temp_container = []
        return self.__instance

    def register_chosen_data_managers(self, data_manager):
        self.list_chosen_data_managers.append(data_manager)

    def update_data_manager_bundle(self):
        pass

    def valdate_chosen_data_manager_bundle():
        # Sym for each in dm list

        # Sym for each in stock_chosen_holder
        chosen_stock_temp_container = ["test1", "test2", "test3"]

        # for data_manager in self.list_chosen_data_managers:
        # chosen_conditional_symbol1 = self.list_chosen_data_managers[0].get_sym()
        # chosen_conditional_symbol2 = self.list_chosen_data_managers[1].get_sym()
        # chosen_conditional_symbol3 = self.list_chosen_data_managers[2].get_sym()

        chosen_conditional_symbol1 = "test5"
        chosen_conditional_symbol2 = "test2"
        chosen_conditional_symbol3 = "test1"

        conditional_dictionary = {chosen_conditional_symbol1: False, chosen_conditional_symbol2: False,
                                  chosen_conditional_symbol3: False}

        chosen_stock_temp_container_index = 0

        for stock in chosen_stock_temp_container:
            if (stock == chosen_conditional_symbol1):
                if (chosen_stock_temp_container_index == 0):
                    conditional_dictionary[chosen_conditional_symbol1] = True
                if (chosen_stock_temp_container_index == 1):
                    conditional_dictionary[chosen_conditional_symbol2] = True
                if (chosen_stock_temp_container_index == 2):
                    conditional_dictionary[chosen_conditional_symbol3] = True

            if (stock == chosen_conditional_symbol2):
                if (chosen_stock_temp_container_index == 0):
                    conditional_dictionary[chosen_conditional_symbol1] = True
                if (chosen_stock_temp_container_index == 1):
                    conditional_dictionary[chosen_conditional_symbol2] = True
                if (chosen_stock_temp_container_index == 2):
                    conditional_dictionary[chosen_conditional_symbol3] = True

            if (stock == chosen_conditional_symbol3):
                if (chosen_stock_temp_container_index == 0):
                    conditional_dictionary[chosen_conditional_symbol1] = True
                if (chosen_stock_temp_container_index == 1):
                    conditional_dictionary[chosen_conditional_symbol2] = True
                if (chosen_stock_temp_container_index == 2):
                    conditional_dictionary[chosen_conditional_symbol3] = True
            chosen_stock_temp_container_index += 1
        print(conditional_dictionary)

