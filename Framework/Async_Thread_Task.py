# import asyncio
# import aiohttp
#
# class Async_Thread_Task:
#     def __init__(self, name):
#         self.name = name
#
#     def get_listMethodContainer(self):
#         return self.listMethodContainer
#
#     def get_name(self):
#         return self.name
#
#     def create_modified_thread(self):
#         # create thread
#         new_loop = asyncio.new_event_loop()
#         # add list of async func
#         t = Thread(target=self.start_loop, args=(new_loop))
#         t.start()
#         # begin event loop
#         # add list of async func
#
#
#
#         # def async_ method_caller():
#
#     # def aysnc_thread(payload):
#     #
#     #
#     #     # for each function listMethodContainer
#     #     t = Thread(target=start_loop, args=(new_loop,))
#     #     t.start()
#     #     return jsonRequest
#
#     def start_loop(self, loop, loopMethod):
#         # print("hitme " + str(countLoop))
#         asyncio.set_event_loop(loop)
#
#         future = asyncio.ensure_future(self.get_name)  # tasks to do
#         loop.run_until_complete(future)  # loop until done
#         # loop.run_forever()
#         # print(countLoop + 1)
#         # countLoop += 1
#
# create_modified_thread
