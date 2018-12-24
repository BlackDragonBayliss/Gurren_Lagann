class Thread_Task:

    listMethodContainer = []

    import asyncio

    def __init__(self, name):
        self.name = name

    def get_listMethodContainer(self):
        return self.listMethodContainer
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # def create_modified_thread(self):
        #create thread

        #add list of async func
        # t = Thread(target=start_loop, args=(new_loop))
        # t.start()
        # begin event loop
        #add list of async func



    # def async_ method_caller():



    # def aysnc_thread(payload):
    #     new_loop = asyncio.new_event_loop()
    #
    #     # for each function listMethodContainer
    #     t = Thread(target=start_loop, args=(new_loop))
    #     t.start()
    #     return jsonRequest
    #
    # def start_loop(loop):
    #     print("hitme "+str(countLoop))
    #     asyncio.set_event_loop(loop)
    #
    #
    #     loop.run_forever()
    #     print(countLoop + 1)
    #     # countLoop += 1

    # def