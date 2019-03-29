# from threading import Thread,Event,current_thread
# from threading import Timer as _Timer
#
# import aiohttp
# import asyncio
# import json
#
# class Perpetual_Timer():
#
#    def __init__(self):
#       self.currentCount = 0
#
#    # delay = 3, count = 5, method = self.threadFactory.create_thread_async_query_stock,
#    # symbol = symbol, requestValue = 0, stockComposite = stockComposite, httpUtility = self.httpUtility, requestFactory = self.requestFactory, typeConverter = self.typeConverter, operationCenter = self.operationCenter)
#    #
#    # def setup_timer_stock(self,delay,countToEnd,functionToInvoke,listOfObjects,threadManager,event,symbol):
#    def setup_timer_stock(self, delay, countToEnd, functionToInvoke, listOfObjects, threadManager, event, symbol):
#         self.delay = delay
#         self.countToEnd = countToEnd
#         self.functionToInvoke = functionToInvoke
#         self.stopped = event
#         self.symbol = symbol
#         # count = 0
#         self.listOfObjects = listOfObjects
#         # self.listOfObjects.append(symbol)
#
#         self.thread =  Thread(target=self.run, args=(),name=symbol)
#         # self.thread = Timer(self.delay, self.handle_function)
#         # self.thread = Timer(self.delay, self.run,symbol)
#         # self.timer = self.named_timer(symbol, 2, self.run())
#         # add self to list in threadManager
#         listPerpetualTimers = threadManager.get_listPerpetualTimers()
#         listPerpetualTimers.append(self)
#         # print(len(listPerpetualTimers))
#
#         # self.stopped = False
#
#         self.thread.start()
#
#
#         # self.timer.run()
#
#    # def named_timer(name, interval, function):
#    #     """Factory function to create named Timer objects.
#    #
#    #       Timers call a function after a specified number of seconds:
#    #
#    #           t = Timer('Name', 30.0, function)
#    #           t.start()
#    #           t.cancel()  # stop the timer's action if it's still waiting
#    #     """
#    #     timer = _Timer(name, interval, function)
#    #     timer.name = name
#    #     return timer
#    # def handle_function(self):
#    #
#    #    # print(self.listOfObjects)
#    #    self.functionToInvoke(self.listOfObjects)
#    #
#    #    # print(self.currentCount)
#    #    # self.thread = Timer(self.delay,self.handle_function)
#    #    # self.thread.start()
#    #    self.currentCount = (self.currentCount + 1)
#    #
#    #    if(self.currentCount == self.countToEnd):
#    #      self.thread.cancel()
#
#    def run(self):
#        # print(current_thread().getName())
#        while not self.stopped.wait(self.delay):
#            print(current_thread().getName())
#
#            # count = 0
#            # for arg in self.listOfObjects:
#            #     # print(count)
#            #     if (count == 0):
#            #         httpUtility = arg
#            #     if (count == 1):
#            #         requestFactory = arg
#            #     if (count == 2):
#            #         typeConverter = arg
#            #     if (count == 3):
#            #         operationCenter = arg
#            #     if (count == 4):
#            #         topStockComposite = arg
#            #     if (count == 5):
#            #         threadManager = arg
#            #     if (count == 6):
#            #         symbol = arg
#            #     count = count + 1
#            #
#            #     # we have top stock data
#            #     # Create post to node, json from stocks
#            #
#            #     # if posting as request top stock,
#            #     # if symbol does not exist, create and store stock
#            # print('dawgs')
#            #
#            # # get symbol
#            #
#            # # Create post to node for stock
#            #
#            # loop = asyncio.new_event_loop()
#            # asyncio.set_event_loop(loop)
#            # response = loop.run_until_complete(httpUtility.async_post_stock_top(symbol, requestFactory))
#            # jsonToProcess = json.loads(response)
#            # strOfJSON = str(jsonToProcess)
#            # # process res
#            # print('JSON of thread' + strOfJSON)
#
#            self.functionToInvoke(self.listOfObjects,self.symbol)
#
#            if (self.currentCount == self.countToEnd):
#                self.stopped.set()
#                print('ending')
#            self.currentCount = (self.currentCount + 1)
#            # call a function
#
#    def start(self):
#       self.thread.start()
#
#    def cancel(self):
#       self.thread.cancel()
#
# def printer(textInfo):
#     print(textInfo)
#
# # t = Perpetual_Timer()
# # t.setup_timer(3,printer('hi'),5)
# # t.start()


from threading import Thread,Event,current_thread
from threading import Timer as _Timer

import aiohttp
import asyncio
import json

class Perpetual_Timer():

   def __init__(self):
      self.currentCount = 0

   def setup_timer_stock(self, delay, countToEnd, functionToInvoke, name):
        self.delay = delay
        self.countToEnd = countToEnd
        self.functionToInvoke = functionToInvoke
        self.stopped = Event();
        self.name = name;
        self.thread =  Thread(target=self.__run, args=(),name=self.name)
        #
        self.thread.start()

   def setup_timer_timer_loop(self, delay, countToEnd, functionToInvoke, list_objects, name):
       self.delay = delay
       self.countToEnd = countToEnd
       self.functionToInvoke = functionToInvoke
       self.stopped = Event();
       self.name = name;
       self.list_objects();
       self.thread = Thread(target=self.__run, args=(list_objects), name=self.name)
       #
       self.thread.start()

   def __run(self):
       # print(current_thread().getName())
       while not self.stopped.wait(self.delay):
           # print(current_thread().getName())

           self.functionToInvoke()

           # if (self.currentCount == self.countToEnd):
           #     self.stopped.set()
           #     print('ending')
           # self.currentCount = (self.currentCount + 1)
           #

   # def start(self):
   #    self.thread.start()

   def cancel(self):
      # self.thread.cancel()
      print("quiting pep timer: "+self.name)
      self.stopped.set()