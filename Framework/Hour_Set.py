class Hour_Set:
    def __init__(self,created_time):
        self.list_ten_minute_set_container = []
        self.created_time = created_time

    def get_list_ten_minute_set_container(self):
        return self.list_ten_minute_set_container

    def get_created_time(self):
        return self.created_time