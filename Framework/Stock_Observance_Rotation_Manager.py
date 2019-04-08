# You're shooting for all the marbles not just the marble factory.

class Stock_Observance_Rotation_Manager():
    # global_generation_ID = 0

    def __init__(self, operation_center, top_stock_monument_composite):
        self.operation_center = operation_center
        self.top_stock_monument_composite = top_stock_monument_composite
        self.isCurrentChosenDetermined = 0
        self.list_values = []


    def change_over_data_managers_to_extended(self, data_manager_list):
        for data_manager in data_manager_list:
            #Cancel, create, store in list.
            data_manager.cancel()
            #Cancel DC? DM locally? No handle here, abstraction level higher.
            # data_manager.exten

    def filter_chosen_from_extended_data_manager_list(self, highest_priority_data_manager):
        data_manager_list = self.top_stock_monument_composite.get_top_stock_data_manager_monument_list()
        data_manager_index = 0

        for dm in data_manager_list:
            print("DMLIST before removal: " + dm.get_sym())


        for data_manager in data_manager_list:
            if(data_manager.get_sym() == highest_priority_data_manager.get_sym()):
                print("hit at index: "+str(data_manager_index))
                #remove at index chosen data_manager
                if(data_manager_index == 2):
                    print("data_manager_index == 2")
                    # begin_slice_index = data_manager_index - 1
                    end_slice_index = data_manager_index + 1
                    print("end_slice_index: "+str(end_slice_index))
                    print("data_manager_index: " + str(data_manager_index))

                    del data_manager_list[data_manager_index:end_slice_index]

                    for dm in data_manager_list:
                        print("DMLIST after removal: " + dm.get_sym())
                    break
                else:
                    print("data_manager_index != 2")
                    end_slice_index = data_manager_index + 1
                    del data_manager_list[data_manager_index:end_slice_index]
                    for dm in data_manager_list:
                        print("DMLIST after removal: " + dm.get_sym())
                    break
                # print(a)
                # data_manager_list_index
            data_manager_index += 1

        return data_manager_list


    def filter_highest_priority_data_manager(self):
        data_manager_list = self.top_stock_monument_composite.get_top_stock_data_manager_monument_list()
        highest_data_manager = 0

        for data_manager in data_manager_list:
            print("Filtered sym: "+ data_manager.get_sym()+ " priority: "+str(data_manager.get_golden_goose_priority()))

            if(highest_data_manager == 0):
                highest_data_manager = data_manager
                continue
            if (highest_data_manager.get_golden_goose_priority() < data_manager.get_golden_goose_priority()):
                highest_data_manager = data_manager
                continue
        return highest_data_manager


    def intake_query(self, current_query):
        self.current_query = current_query
        print(self.current_query)
        for key, value in current_query.items():
            if key == 'isChosenDetermined':
                self.isCurrentChosenDetermined = value
                print("isChosen: "+self.isCurrentChosenDetermined)
            if key == 'dataList':
                dataList = value
                self.list_values = dataList
                print("dataList: "+str(self.list_values))

        return self.isCurrentChosenDetermined

    def tag_data_managers(self):
        data_manager_list = self.top_stock_monument_composite.get_top_stock_data_manager_monument_list()

        #Read results
        item_list_store = []
        for data_manager in data_manager_list:
            # item_list_store = []
            for value in self.list_values:
                list_to_be_added = []
                for key, value in value.items():
                    if (key == "symbol"):
                        list_to_be_added.append(value)
                    if (key == "stockPriority"):
                        list_to_be_added.append(value)
                item_list_store.append(list_to_be_added)

        #This was originally made to store symbol and priority.
        #But then what happened. Symbol priority of extended,

        print(str(item_list_store))

        for data_manager_symbol in data_manager_symbol:
            if(symbol1 == data_manager.get_sym()):
                print("hit symbol: "+data_manager.get_sym())
                data_manager.set_golden_goose_priority(priority1)

            if (symbol2 == data_manager.get_sym()):
                print("hit symbol: " + data_manager.get_sym())
                data_manager.set_golden_goose_priority(priority2)

            if (symbol3 == data_manager.get_sym()):
                print("hit symbol: " + data_manager.get_sym())
                data_manager.set_golden_goose_priority(priority3)

                # print("symbol success: "+symbol)
                # data_manager.set_golden_goose_priority(priority)
                # print("retrieved priority: "+data_manager.get_golden_goose_priority())

        for data_manager in data_manager_list:
            print("DM: "+ data_manager.get_sym() +" priority: "+ str(data_manager.get_golden_goose_priority()))
            # if(data_manager.get_is_golden_goose() == 1):
            #     data_manager.set_golden_goose_priority()

    def rotate_stocks(self, golden_goose_report):
        self.golden_goose_report = golden_goose_report

        print(self.golden_goose_report)
