class Stock:

    def __init__(self):
        self.name = ''

    def get_name (self):
        return self.name
    def set_name (self, name):
        self.name = name

    def get_pchg (self):
        return self.pchg
    def set_pchg (self, pchg):
        self.pchg = pchg

    def get_pcls (self):
        return self.pcls
    def set_pcls (self, pcls):
        self.pcls = pcls

    def get_last (self):
        return self.last
    def set_last (self, last):
        self.last = last

    def get_bid (self):
        return self.bid
    def set_bid (self, bid):
        self.bid = bid

    def get_ask(self):
        return self.ask
    def set_ask(self, ask):
        self.ask = ask
