import datetime

class Calendar_Tracker:
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
        return self.__instance


    def is_weekend(self):
        if(datetime.datetime.today().weekday() == 5 | datetime.datetime.today().weekday() == 6):
            return False
        return True

    def is_day_holiday_day(self):
        pass


    def get_current_day(self):
        return datetime.datetime.today().weekday()

    def get_formated_date(self):
        today = str(datetime.date.today())
        list_date = today.split('-')
        returned_list = [list_date[1],list_date[2],list_date[0],self.get_current_day()]
        return returned_list

