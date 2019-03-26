# You're shooting for all the marbles not just the marble factory.

class Stock_Observance_Rotation_Manager():
    # global_generation_ID = 0

    def __init__(self, operation_center, top_stock_monument_composite):
        self.operation_center = operation_center
        self.top_stock_monument_composite = top_stock_monument_composite
        self.isCurrentChosenDetermined = 0
        self.list_values = []

    def filter_data_managers(self):
        data_manager_list = self.top_stock_monument_composite.get_top_stock_data_manager_monument_list()
        for data_manager in data_manager_list:
            print("Filtered sym: "+ data_manager.get_sym()+ " priority:"+data_manager.get_golden_goose_priority())
            #What to put here?
                #What do we need? Filter
                    #What do we filter here?

            def fuckthisshit(something):

        # print()
        # self.current_query = current_query
        # print(self.current_query)
        # for key, value in current_query.items():
        #     if key == 'isChosenDetermined':
        #         self.isCurrentChosenDetermined = value
        #         print("isChosen: "+self.isCurrentChosenDetermined)
        #
        #     if key == 'dataList':
        #         dataList = value
        #         self.list_values = dataList
        #         print("dataList: "+str(self.list_values))
        #
        # return self.isCurrentChosenDetermined

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
        #for DM in DMList that is OC localized
        data_manager_list = self.top_stock_monument_composite.get_top_stock_data_manager_monument_list()

        for data_manager in data_manager_list:
            symbol1 = "0"
            priority1 = "0"
            symbol2 = "0"
            priority2 = "0"
            symbol3 = "0"
            priority3 = "0"

            valueIndex = 0
            for value in self.list_values:
                # singule {} dict
                for key, value in value.items():
                    if(valueIndex == 0):
                        if (key == "symbol"):
                            symbol1 = value
                        if (key == "stockPriority"):
                            priority1 = value

                    if (valueIndex == 1):
                        if (key == "symbol"):
                            symbol2 = value
                        if (key == "stockPriority"):
                            priority2 = value

                    if (valueIndex == 2):
                        if (key == "symbol"):
                            symbol3 = value
                        if (key == "stockPriority"):
                            priority3 = value
                valueIndex += 1
                # if
            print("symbol1 is: "+symbol1)
            print("priority1 is: " + priority1)
            print("symbol2 is: " + symbol2)
            print("priority2 is: " + priority2)
            print("symbol3 is: " + symbol3)
            print("priority3 is: " + priority3)


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
