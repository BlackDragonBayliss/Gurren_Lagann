
class Data_Manager_Action:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.__instance.name = ''
        return self.__instance


    def get_DM_Buy (self):
        return self.DM_Buy
    def set_DM_Buy (self, DM_Buy):
        self.DM_Buy = DM_Buy


    def get_sym (self):
        return self.sym
    def set_sym (self, sym):
        self.sym = sym

    def get_day (self):
        return self.day
    def set_day (self, day):
        self.day = day

    def get_epoch_of_trade (self):
        return self.epoch_of_trade
    def set_epoch_of_trade (self, epoch_of_trade):
        self.epoch_of_trade = epoch_of_trade


    def get_is_day_trade (self):
        return self.is_day_trade
    def set_is_day_trade (self, is_day_trade):
        self.is_day_trade = is_day_trade


    def get_price_bought_actual (self):
        return self.price_bought_actual
    def set_price_bought_actual (self, price_bought_actual):
        self.price_bought_actual = price_bought_actual



    def get_price_sold_actual (self):
        return self.price_sold_actual
    def set_price_sold_actual (self, price_sold_actual):
        self.price_sold_actual = price_sold_actual



    def get_price_bought_estimate (self):
        return self.price_bought_estimate
    def set_price_bought_estimate (self, price_bought_estimate):
        self.price_bought_estimate = price_bought_estimate




    def get_price_sold_estimate(self):
        return self.price_sold_estimate
    def set_price_sold_estimate (self, price_sold_estimate):
        self.price_sold_estimate = price_sold_estimate



    def get_pchg_bought_actual(self):
        return self.pchg_bought_actual
    def set_pchg_bought_actual(self, pchg_bought_actual):
        self.pchg_bought_actual = pchg_bought_actual



    def get_pchg_sold_actual(self):
        return self.pchg_sold_actual
    def set_pchg_sold_actual(self, pchg_sold_actual):
        self.pchg_sold_actual = pchg_sold_actual




    def get_pchg_bought_estimate(self):
        return self.pchg_bought_estimate
    def set_pchg_bought_estimate(self, pchg_bought_estimate):
        self.pchg_bought_estimate = pchg_bought_estimate




    def get_pchg_sold_estimate(self):
        return self.pchg_sold_estimate
    def set_pchg_sold_estimate(self, pchg_sold_estimate):
        self.pchg_sold_estimate = pchg_sold_estimate




