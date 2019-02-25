
class MultipleIntervalJump:

    def __init__(self):
        pass

    def createIntervalJump(self, task_master):
        self.task_master = task_master
        self.task_master.create_thread_async_top_stock_phase_internal()
    # Route relayed from internal request
    def joinIntervalJump(self, task_master, response):
        self.task_master = task_master
        self.task_master.create_thread_async_top_stock_phase1(response)