class Stock_Statistics:
    def __init__(self, sym, pchg, last, spread):
        self.sym = sym
        self.pchg = pchg
        self.last = last
        self.spread = spread

    def get_sym(self):
        return self.sym

    def get_pchg(self):
        return self.pchg

    def get_last(self):
        return self.last


        # def get_bid(self):
        #     return self.bid
        # def set_bid(self, bid):
        #     self.bid = bid
        #
        # def get_ask(self):
        #     return self.ask
        # def set_ask(self, ask):
        #     self.ask = ask
