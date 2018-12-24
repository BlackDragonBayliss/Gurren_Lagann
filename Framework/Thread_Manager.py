from threading import Thread

class Thread_Manager:

    listThreads = []
    listPerpetualTimers = []

    def __init__(self):
        self.name = ''

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def store_thread(self,thread):
        self.listThreads.append(thread)
        # return 0
    def get_listThreads(self):
        return self.listThreads

    def store_listPerpetualTimers(self,perpetualTimer):
        self.listPerpetualTimers.append(perpetualTimer)

    def get_listPerpetualTimers(self):
        return self.listPerpetualTimers
