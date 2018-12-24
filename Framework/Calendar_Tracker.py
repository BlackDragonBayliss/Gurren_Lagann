import datetime

class Calendar_Tracker:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
        return self.__instance

    def get_current_day(self):
        return datetime.datetime.today().weekday()

    def is_day_holiday_day(self):
        pass

