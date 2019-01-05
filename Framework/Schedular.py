from Objects.Thread_Task import Thread_Task

class Schedular:
    # thread_holder = []
    def __init__(self):
        self.thread_holder = []
        self.thread_holder.insert(0, 42)

    def create_thread(self):
        return self.thread_holder[0]

    def create_async_thread():
        return 'async thread'

    def delay_thread(thread):
        return 'delayed thread response'

    def start_thread(thread):
        return 'started thread response'

schedular = Schedular()
print(schedular.create_thread())
