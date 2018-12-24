import calendar, time

class Time_Manager:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)

        return self.__instance

    def get_current_second(self):
        ts = time.time()
        self.currentTime = time.localtime(ts)
        return self.currentTime.tm_sec

    def get_current_minute(self):
        ts = time.time()
        self.currentTime = time.localtime(ts)
        return self.currentTime.tm_min

    def get_current_hour(self):
        ts = time.time()
        self.currentTime = time.localtime(ts)
        return self.currentTime.tm_hour

    def calculate_time(self):
        return 0

    def get_current_epoch_time(self):
        epoch_time = calendar.timegm(time.gmtime())
        return epoch_time