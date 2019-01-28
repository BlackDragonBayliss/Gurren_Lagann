# # # # from threading import Thread
# # # # import asyncio
# # # # import aiohttp
# # # import requests
# # #
# # #
# # #
# # # # import asyncio
# # # # import aiohttp
# # # #
# # # # async def fetch(url):
# # # #     respone1 = requests.get(url)
# # # #     response = await respone1
# # # #     return await response.text()
# # # #
# # # # loop = asyncio.get_event_loop()
# # # # loop.run_until_complete(asyncio.gather(
# # # #     asyncio.ensure_future(fetch("http://www.google.com")),
# # # #     asyncio.ensure_future(fetch("http://www.github.com")),
# # # #     asyncio.ensure_future(fetch("http://www.reddit.com"))
# # # # ))
# # #
# # #
# # # # async def fetch(url):
# # # #     response = await aiohttp.request('GET', url)
# # # #     return await response.text()
# # # #
# # # # loop = asyncio.get_event_loop()
# # # # loop.run_until_complete(asyncio.gather(
# # # #     asyncio.ensure_future(fetch("http://www.google.com")),
# # # #     asyncio.ensure_future(fetch("http://www.github.com")),
# # # #     asyncio.ensure_future(fetch("http://www.reddit.com"))
# # # # ))
# # #
# # #
# # #
# # # # async def fetch(url):
# # # #     response = await aiohttp.request('GET', url)
# # # #     return await response.text()
# # # #
# # # # def start_background_loop(loop):
# # # #     asyncio.set_event_loop(loop)
# # # #     loop.run_forever()
# # # # # Create a new loop
# # # #
# # # # new_loop = asyncio.new_event_loop()
# # # # # Assign the loop to another thread
# # # # t = Thread(target=start_background_loop, args=(new_loop))
# # # # t.start()
# # # # # Give it some async work
# # # #
# # # # future = asyncio.run_coroutine_threadsafe(
# # # #     fetch("http://www.google.com"),
# # # #     new_loop
# # # # )
# # # # # Wait for the result
# # # # print(future.result())
# # # # # # Do it again but with a callback
# # # # # asyncio.run_coroutine_threadsafe(
# # # # #     requests.get("http://www.github.com"),
# # # # #     new_loop
# # # # # ).add_done_callback(lambda future: print(future.result()))
# # # #
# # # #
# # #
# # # #
# # # # import asyncio
# # # # import requests
# # # # import bs4
# # # #
# # # # urls = ["http://www.google.com"]
# # # #
# # # # async def getContent(url):
# # # #     loop = asyncio.get_event_loop()
# # # #     print("getting content for: " + url) # print should be called here
# # # #     # execute a non async function async
# # # #     future = loop.run_in_executor(None, requests.get, url)
# # # #
# # # #     # doing stuff with bs4
# # # #     # soup = bs4.BeautifulSoup((await future).text, "html.parser") # should now interrupt
# # # #
# # # #     return await future
# # # #
# # # # async def main():
# # # #     loop = asyncio.get_event_loop()
# # # #
# # # #     print("starting gathering...")
# # # #     # creating a list of futures
# # # #     futures = [getContent(url) for url in urls]
# # # #     # packing futures into a awaitable list future
# # # #     responses_future = asyncio.gather(*futures)
# # # #
# # # #     print("doing stuff in between...")
# # # #     # waiting for all futures
# # # #     responses = await responses_future
# # # #
# # # #     print("Done")
# # # #
# # # #     for response in responses:
# # # #         print(response)
# # # #
# # # # loop = asyncio.get_event_loop()
# # # # loop.run_until_complete(main())
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# #from Framework.HTTP_Utility
# # import HTTP_Utility
# # from HelperClasses.Request_Factory import Request_Factory
# #
# # import asyncio
# # import requests
# # import bs4
# # import json
# #
# #
# # urls = ['http://localhost:3000/api/brokerage']
# #
# # async def getContent(url):
# #     loop = asyncio.get_event_loop()
# #     requestFactoryObject = Request_Factory()
# #     jsonRequest =  requestFactoryObject.factory_intake(0, {
# # 		"stockSymbol":"CLWT"
# # 	})
# #     # print(jsonRequest)
# #     # HTTP_Utility.post_request(jsonRequest)
# #     print("getting content for: ") # print should be called here
# #     # execute a non async function async
# #
# #     # print (jsonRequest)
# #     future = loop.run_in_executor(None, HTTP_Utility.post_request, url, jsonRequest)
# #
# #     # doing stuff with bs4
# #     # soup = bs4.BeautifulSoup((await future).text, "html.parser") # should now interrupt
# #
# #     # return await future
# #
# #
# # async def main():
# #     # loop = asyncio.get_event_loop()
# #
# #     print("starting gathering...")
# #     # creating a list of futures
# #     futures = [getContent(url) for url in urls]
# #     # packing futures into a awaitable list future
# #     responses_future = asyncio.gather(*futures)
# #     # finalRespone = await getContent(urls)
# #     print("doing stuff in between...")
# #     # waiting for all futures
# #     responses = await responses_future
# #
# #     # print("Done")
# #
# #     for response in responses:
# #         print(response)
# #     # print(finalRespone)
# #
# # loop1 = asyncio.get_event_loop()
# # loop1.run_until_complete(main())
# #
#
#
#
#
#
#
#
# #
# #
# #
# #
# #
# # # from requests import async
# # # If using requests > v0.13.0, use
# # from grequests import async
# #
# # urls = [
# #     'http://python-requests.org',
# #     'http://httpbin.org',
# #     'http://python-guide.org',
# #     'http://kennethreitz.com'
# # ]
# #
# # # A simple task to do to each response object
# # def do_something(response):
# #     print(response.url)
# #
# # # A list to hold our things to do via async
# # async_list = []
# #
# # for u in urls:
# #     # The "hooks = {..." part is where you define what you want to do
# #     #
# #     # Note the lack of parentheses following do_something, this is
# #     # because the response will be used as the first argument automatically
# #     action_item = async.get(u, hooks = {'response' : do_something})
# #
# #     # Add the task to our list of things to do via async
# #     async_list.append(action_item)
# #
# # # Do our list of things to do via async
# # async.map(async_list)
# #
# #
# #
# #
# #
#
#
# # import grequests
# #
# # def print_res(res):
# #     from pprint import pprint
# #     pprint (vars(res))
# #
# # req = grequests.get('http://www.google.com', hooks=dict(response=print_res))
# # job = grequests.send(req, grequests.Pool(1))
# #
# # for i in range(10):
# #     print (i)
#
# # import asyncio
# # import aiohttp
# # import requests
# # import bs4
# # import json
#
#
# # import aiohttp
# # import asyncio
# #
# # async def fetch(session, url):
# #
# #     async with session.post(url) as response:
# #         return await response.text()
# #
# # async def main():
# #     async with aiohttp.ClientSession() as session:
# #         html = await fetch(session, 'https://jsonplaceholder.typicode.com/posts/')
# #         print(html)
# #
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main())
#
#
#
# # async def parsePlaylist(url):
# #     headers = {'Content-Type': 'application/json'}
# #     # {
# # # 	"title": "foo",
# # #       "body": "bar",
# # #       "userId": "1"
# # # }
# #
# #     # try:
# #     page = await aiohttp.post(url, headers=headers)
# #     page = await page.text()
# #     print(page)
# #     # except:
# #     #     print('derp')
# #     #     return False
# #
# # # responseRequest = await parsePlaylist('https://jsonplaceholder.typicode.com/posts/')
# # # print(responseRequest)
# #
# # loop = asyncio.new_event_loop()
# # # prepare_for_foo()
# # task = loop.create_task(parsePlaylist('https://jsonplaceholder.typicode.com/posts/'))
# # # remaining_work_not_depends_on_foo()
# # loop.run_until_complete(task)
#
#
#
#
#
#
#
#      #    try:
# 	# 	page = await aiohttp.post(url, headers=headers)
# 	# 	page = await page.text()
#     # # except:
#     # # 	return False
# 	# 	page = requests.get(url, headers=headers)
# 	# 	soup = BeautifulSoup(page, 'html.parser')
# 	# 	tags = soup.find_all("tr", class_="pl-video yt-uix-tile ")
# 	# 	links = []
#     #
# 	# 	for tag in tags:
# 	# 		links.append("https://www.youtube.com/watch?v=" + tag['data-video-id'])
# 	# 	if links != []:
# 	# 		return links
# 	# 	else:
# 	# 		return False
# 	# except:
# 	# 	return False
#
#
#
# # def parsePlaylist(url):
# # 	try:
# # 		page = await aiohttp.post(url, headers=headers)
# # 		page = await page.text()
# # 	except:
# # 		return False
#
# # import sched, time
# # import HTTP_Utility
# # from objects.Stock import Stock
# # from objects.Top_Stock_Composite import Top_Stock_Composite
# # from objects.Thread_Task import Thread_Task
#
#
#
#
# # from Operation_Center import Operation_Center
# # operationCenter = Operation_Center()
# # # #
# # operationCenter.begin_operation()
#
#
#
#
#
#
#
# # imports
# # import threading
# # import time
# #
# # def worker():
# #     print ("worker....")
# #     time.sleep(3)
# #
# # threads = []
# # for i in range(5):
# #     thread = threading.Thread(target=worker)
# #     threads.append(thread)
# #     thread.start()
#
# # import timeit
# # def foobar():
# #     print('yo')
# # timeit.timeit('foobar()','from __main__ import foobar', number=1000)
#
# # import time
# # def sleeper():
# #     while True:
# #         # Get user input
# #         num = input('How long to wait: ')
# #
# #         # Try to convert it to a float
# #         try:
# #             num = float(num)
# #         except ValueError:
# #             print('Please enter in a number.\n')
# #             continue
# #
# #         # Run our time.sleep() command,
# #         # and show the before and after time
# #         print('Before: %s' % time.ctime())
# #         time.sleep(num)
# #         print('After: %s\n' % time.ctime())
# #
# #
# # try:
# #     sleeper()
# # except KeyboardInterrupt:
# #     print('\n\nKeyboard exception received. Exiting.')
# #     exit()
#
#
# # import aiohttp
# # import asyncio
# # import json
# # from threading import Thread,Event,current_thread
# # from Perpetual_Timer import Perpetual_Timer
# #
# # from HTTP_Utility import HTTP_Utility
# # from Request_Factory import Request_Factory
#
#
#
# # httpUtility = HTTP_Utility()
# # symbol = "APPL"
# # requestFactory = Request_Factory()
# #
# # loop = asyncio.new_event_loop()
# # asyncio.set_event_loop(loop)
# # response = loop.run_until_complete(httpUtility.async_post_stock_top(symbol, requestFactory))
# #
# # print(response)
# import asyncio
# from threading import Thread
# import time
# import calendar
#
# # from HTTP_Utility import HTTP_Utility
# # from Top_Stock_Composite import Top_Stock_Composite
# # from Stock_Composite import Stock_Composite
# # from Request_Factory import Request_Factory
# # from Type_Converter import Type_Converter
# # from Task_Master import Task_Master
# # from Thread_Factory import Thread_Factory
# # from Perpetual_Timer import Perpetual_Timer
# # from Thread_Manager import Thread_Manager
# # from Composite_Manager import Composite_Manager
#
#
# # from threading import Thread,Event,current_thread
# # from threading import Timer as _Timer
# #
# # import aiohttp
# # import asyncio
# # import json
# #
# #
# # class Perpetual_Timer():
# #
# #    def __init__(self):
# #       self.currentCount = 0
# #
# #    def setup_timer_stock(self, delay, countToEnd, functionToInvoke, name):
# #         self.delay = delay
# #         self.countToEnd = countToEnd
# #         self.functionToInvoke = functionToInvoke
# #         self.stopped = Event();
# #         self.name = name;
# #         self.thread =  Thread(target=self.run, args=(),name=self.name)
# #
# #         self.thread.start()
# #
# #
# #    def run(self):
# #        # print(current_thread().getName())
# #        while not self.stopped.wait(self.delay):
# #            print(current_thread().getName())
# #
# #            self.functionToInvoke()
# #
# #            if (self.currentCount == self.countToEnd):
# #                self.stopped.set()
# #                print('ending')
# #            self.currentCount = (self.currentCount + 1)
# #            # call a function
# #
# #    def start(self):
# #       self.thread.start()
# #
# #    def cancel(self):
# #       self.thread.cancel()
# #
# #
# #
# # class Operation:
# #     def __init__(self):
# #         self.name = ''
# #     def initiateMainLoop(self):
# #         print('initiate hit')
# #         # loop = asyncio.new_event_loop()
# #         # asyncio.set_event_loop(loop)
# #         # # typeConverter.parse_stock_queries(data, operationCenter)
# #         # # topStockComposite = operationCenter.get_topStockComposite()
# #         #
# #         # #Break update
# #         # response = loop.run_until_complete(self.mainLoop())
# #         self.mainLoop()
# #
# #
# #     def mainLoop(self):
# #         # print('hey')
# #         # httpUtility = HTTP_Utility()
# #         # requestFactory = Request_Factory()
# #         # httpUtility.test(requestFactory)
# #         ts = time.time()
# #         #
# #         currentTime = time.localtime(ts);
# #         # # print(currentTime.tm_hour)
# #         # # time.struct_time(tm_year=2018, tm_mon=9, tm_mday=1, tm_hour=11, tm_min=21, tm_sec=24, tm_wday=5, tm_yday=244, tm_isdst=1)
# #         #
# #         if currentTime.tm_hour == 12:
# #             print('hit success')
# #
# #
# # operationInstance = Operation()
# #
# #
# # perpetualTImer = Perpetual_Timer()
# # perpetualTImer.setup_timer_stock(2,3,operationInstance.initiateMainLoop,'perp1')
# # setup_timer_stock(self, delay, countToEnd, functionToInvoke):
#
#
#
#
# print(calendar.timegm(time.gmtime()))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # operationCenter.process_query_top_stock()
#
#
# # operationCenter.create_query_thread
#
# # from threading import Timer,Thread,Event
#
# # from Perpetual_Timer import Perpetual_Timer
# #
# # def printer():
# #     print('shit')
# #
# # perpetualTimer = Perpetual_Timer(3,printer,5)
# # perpetualTimer.start()
#
# # from Top_Stock_Composite import Top_Stock_Composite
# # from Stock_Composite import Stock_Composite
# #
# #
# #
# # # class Test:
# # #
# # #     listStocks = []
# # #
# # #     def __init__(self):
# # #         self.name = 'derpyhoof'
# # #
# # #     def perform(self, fun, *args ):
# # #         fun( *args )
# # #
# # #
# # #     def action2(self, *args ):
# # #         # print(((p*r))-w)
# # #         print(r.get_name())
# # #         # print(args)
# # #
# # #
# # # # p = Top_Stock_Composite()
# # #
# # # testObj = Test()
# # r = Stock_Composite()
# # q = Stock_Composite()
# # # #
# # # p = 5
# # # r = 20
# # # w = 3
# # r.perform( r.action2, q, 4)
#
#
#
#
#
#
#

from threading import Thread
from queue import Queue
from Top_Stock_Composite import Top_Stock_Composite
import time

# def thread1(threadname, q):
#     #read variable "a" modify by thread 2
#     while True:
#         a = q.get()
#         if a is None: return # Poison pill
#         print (a)
#
# def thread2(threadname, q):
#     a = 0
#     for _ in range(10):
#         a += 1
#         q.put(a)
#         time.sleep(2)
#     q.put(None) # Poison pill
#
# queue = Queue()
# tsc = Top_Stock_Composite()
#
# thread1 = Thread( target=thread1, args=("Thread-1", queue) )
# thread2 = Thread( target=thread2, args=("Thread-2", queue) )
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# def thread1(threadname, tsc):
#     # print (a)
#     tsc.set_name("henry")
# def thread2(threadname, tsc):
#     # a = 0
#     print("name is: "+tsc.get_name())
#
# queue = Queue()
# tsc = Top_Stock_Composite()
#
# thread1 = Thread( target=thread1, args=("Thread-1", tsc) )
# thread2 = Thread( target=thread2, args=("Thread-2", tsc) )
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()


# mport datetime
# datetime.datetime.now()
# datetime(2009, 1, 6, 15, 8, 24, 78915)
#
# print(datetime.datetime.now())
#
# >>> datetime.datetime.time(datetime.datetime.now())
# datetime.time(15, 8, 24, 78915)
#
# >>> print(datetime.datetime.time(datetime.datetime.now()))
# 09:17:51.914526
# The same, but slightly more compact:
#
# >>> datetime.datetime.now().time()





# import sys
# # x = sys.stdin.read()
# #
# # print(x)
#
#
# StringToSplit = sys.stdin.read()#input('please enter string: ')#sys.stdin.read()#input("Enter")
# # array_of_input = StringToSplit.split("\"")
# #
#
# #
# # # print(array_of_input)
# #
# completedString = ""
# # currentIndex = 0
#
# line = StringToSplit.replace('\n','')
# line = StringToSplit.replace('\t','')
#
# print(line)

#For each index
# for value in array_of_input:
#     # Add /" in front of each value
#     # if(currentIndex != 0):
#     ValueAppended ="\\"+ "\""+value
#     completedString += ValueAppended
#     currentIndex += 1
# print(completedString)


# list = []
#
# list.append('fuck')
# print(list)


# from Perpetual_Timer import Perpetual_Timer
#
# PT = Perpetual_Timer()
#
# def sayHi():
#     print("Hello")
#
# PT.setup_timer_stock(1, 4, sayHi, 'hello_thread')


# PT.run()


# def main():
#     HourlyTemperatures=[]
#     # computedInputHourlyTemperatureslist=GetTemperatures(HourlyTemperatures)
#     GetTemperatures(HourlyTemperatures)
#     AverageTemp=ComputeAverageTemp(HourlyTemperatures)
#     # print("Average=",average)
#     DisplayTemperatures(HourlyTemperatures, AverageTemp)
#
# def ComputeAverageTemp(HourlyTemperatures):
#     average = 0
#     for value in HourlyTemperatures:
#         average = sum(HourlyTemperatures) / len(HourlyTemperatures)
#     return average
#
# def GetTemperatures(HourlyTemperatures):
#     curHour=0
#     # inputHourlyTemperatureList = HourlyTemperatures
#     while(curHour<24):
#         print("hour", curHour)
#         inputTemperature=float(input("Enter Temperature for hour:"))
#         while (inputTemperature>-50 and inputTemperature<130):
#             HourlyTemperatures.append(inputTemperature)
#             curHour=curHour+1
#             break
#         if(inputTemperature<-50 or inputTemperature>130):
#             print("Please re-enter a value within range")
#     return HourlyTemperatures
#
# def DisplayTemperatures(HourlyTemperatures, AverageTemp):
#     for temp in HourlyTemperatures:
#         #print output as requested
#         print(temp)
# main()




# class Person:
#
#     def __init__(self, first, last, age):
#         self.firstname = first
#         self.lastname = last
#         self.age = age
#
#     def __str__(self):
#         return self.firstname + " " + self.lastname + ", " + str(self.age)
#
# class Employee(Person):
#
#     def __init__(self, first, last, age, staffnum):
#         super().__init__(first, last, age)
#         self.staffnumber = staffnum
#
#     def __str__(self):
#         # return super().__str__() + ", " +  self.staffnumber
#         return 'doh'
#
#
# x = Person("Marge", "Simpson", 36)
# y = Employee("Homer", "Simpson", 28, "1007")
#
# print(x)
# print(y)


# from abc import ABC, abstractmethod
#
#
# class AbstractClassExample(ABC):
#     @abstractmethod
#     def do_something(self):
#         ''' To override '''
#         pass
#         # print("Some implementation!")
#
#     @abstractmethodtf
#     def do_something_cool(self):
#         ''' To override '''
#         pass
#
# class AnotherSubclass(AbstractClassExample):
#     def do_something(self):
#         return ''
#     def do_something_cool(self):
#         # super().do_something()
#         print("The enrichment from AnotherSubclass")
#
#
# x = AnotherSubclass()
# x.do_something_cool()



# from Extended_Data_Manager import Extended_Data_Manager
# from Chosen_Data_Manager import Chosen_Data_Manager
# from Bought_Data_Manager import Bought_Data_Manager
#
# extended_DM = Extended_Data_Manager("AAPL",0)
# chosen_DM = Chosen_Data_Manager("DDP",0)
# bought_DM = Bought_Data_Manager("BOY",0)
#
# extended_DM.init_data_processing()
# chosen_DM.init_data_processing()
# bought_DM.init_data_processing()




#
# # Create the main function
# def main():
#     # declare any necessary variable(s)
#     boolUserStillAddingWords = True
#     boolAskingUserInput = True
#     listWords = []
#
#     # // Loop: while the user want to enter more words (minimum of 8)
#     # // Prompt for, input and store a word (string) into a list
#     while (boolUserStillAddingWords):
#         # if(lengthOfListWords < 8):
#
#         # Ask "add more words until 8 minimum words in list.
#         print("Current count of words is", len(listWords),'-', "please enter more until a minimum of 8 words")
#         inputString = input("Please add a word: ")
#         listWords.append(inputString)
#         if (len(listWords) >= 8):
#             while(boolAskingUserInput):
#                 inputAddMoreWords = input("Add more words? (y/n)")
#                 if (inputAddMoreWords == "y" or inputAddMoreWords == 'n'):
#                     if(inputAddMoreWords == "y"):
#                         break
#                     if(inputAddMoreWords == "n"):
#                         boolAskingUserInput = False
#                         boolUserStillAddingWords = False
#                         #     // Pass the list of words to following functions, and perform the manipulations
#                         #
#                         #     //  to produce and return a new, modified, copy of the list.
#                         #     //  NOTE: None of the following functions can change the list parameter it
#                         #     //  receives – the manipulated items must be returned as a new list.
#                         listSortByIncreasingLength = SortByIncreasingLength(listWords)
#                         listSortByDecreasingLength = SortByDecreasingLength(listWords)
#                         listSortByTheMostVowels = SortByTheMostVowels(listWords)
#                         listSortByTheLeastVowels = SortByTheLeastVowels(listWords)
#                         listCapitalizeEveryOtherCharacter =CapitalizeEveryOtherCharacter(listWords)
#                         listReverseWordOrdering = ReverseWordOrdering(listWords)
#                         listFoldWordsOnMiddleOfList = FoldWordsOnMiddleOfList(listWords)
#
#                         # Display the contents of the modified lists of words
#                         # Ask if the user wants to process another list of words
#
#                         DisplayModifiedListsOfWords(listSortByIncreasingLength,listSortByDecreasingLength,
#                                                     listSortByTheMostVowels,listSortByTheLeastVowels,
#                                                     listCapitalizeEveryOtherCharacter,listReverseWordOrdering,
#                                                     listFoldWordsOnMiddleOfList)
#
#                         boolCreateAnotherList = AskUserProcessAnotherList()
#                         if(boolCreateAnotherList):
#                             main()
#                         break
#                 else:
#                     #prompt user "Please enter correct syntax"
#                     print("Please enter \"y\" or \"n\"")
#                     continue
#         continue
#
# # Pass the list of words to following functions, and perform the manipulations
#
# # to produce and return a new, modified, copy of the list.
# # NOTE: None of the following functions can change the list parameter it
# # receives – the manipulated items must be returned as a new list.
#
# def SortByIncreasingLength(listWords):
#     calculatedList = sorted(listWords, key=lambda word: len(word))
#     print(calculatedList)
#     return calculatedList
# def SortByDecreasingLength(listWords):
#     calculatedList = sorted(listWords, key=lambda word: len(word), reverse=True)
#     print(calculatedList)
#     return calculatedList
# def SortByTheMostVowels(listWords):
#     print('SortByMostVowels')
#     calculatedList = sorted(listWords, key=lambda word :AlgoSortVowels(word), reverse=True)
#     print(calculatedList)
#     return calculatedList
# def SortByTheLeastVowels(listWords):
#     print('SortByLeastVowels')
#     calculatedList = sorted(listWords, key=lambda word: AlgoSortVowels(word))
#     print(calculatedList)
#     return calculatedList
# def CapitalizeEveryOtherCharacter(listWords):
#     print('CapitalizeEveryOtherCharacter')
#     calculatedList = []
#     for word in listWords:
#         calculatedWord = AlgoCapitalizeEveryOtherCharacter(word)
#         calculatedList.append(calculatedWord)
#     print(calculatedList)
#     return calculatedList
# def ReverseWordOrdering(listWords):
#     calculatedList = AlgoReverseList(listWords)
#     print(calculatedList)
#     return calculatedList
#
# #No idea what the professor means to sort by ??
# def FoldWordsOnMiddleOfList(listWords):
#     calculatedList = sorted(listWords, key=lambda word: len(word))
#     print(calculatedList)
#     return calculatedList
#
# def AlgoSortVowels(str):
#     # Intializing count variable to 0
#     count = 0
#     # Creating a set of vowels
#     vowel = set("aeiouAEIOU")
#     # Loop to traverse the alphabet in the given string
#     for alphabet in str:
#         # If alphabet is present in set vowel
#         if alphabet in vowel:
#             count = count + 1
#     return count
#
# def AlgoCapitalizeEveryOtherCharacter(str):
#     currentIndex = 0
#     calculatedWord = ""
#     splitList = list(str)
#
#     for character in splitList:
#         if(currentIndex == 0):
#             calculatedWord += character
#             currentIndex += 1
#             continue
#         if (currentIndex % 2 != 0):
#             currentCharacter = character.capitalize()
#             calculatedWord += currentCharacter
#         if(currentIndex % 2 == 0):
#             currentCharacter = character
#             calculatedWord += currentCharacter
#         currentIndex += 1
#     return calculatedWord
#
# def AlgoReverseList(listWords):
#     calculatedList = []
#     boolCalculating = True
#     currentIndex = 0
#     lengthListWords = len(listWords)
#    # Calculate list in descending order
#     while (boolCalculating):
#         # Calculate current list index starting from the last indexed value
#         calculatedListIndex = lengthListWords-(currentIndex+1)
#         calculatedList.append(listWords[calculatedListIndex])
#         currentIndex += 1
#         if(calculatedListIndex == 0):
#             boolCalculating = False
#     return calculatedList
#
#
# # Display the contents of the modified lists of words
# # Ask if the user wants to process another list of words
#
# def DisplayModifiedListsOfWords(listSortByIncreasingLength,listSortByDecreasingLength,
#                                                     listSortByTheMostVowels,listSortByTheLeastVowels,
#                                                     listCapitalizeEveryOtherCharacter,listReverseWordOrdering,
#                                                     listFoldWordsOnMiddleOfList):
#     # Display the contents of the modified lists of words
#     print("Below is the sorted lists:")
#     print("Sorted by increasing length:",listSortByIncreasingLength)
#     print("Sorted by decreasing length:", listSortByDecreasingLength)
#     print("Sorted by the most vowels:", listSortByTheMostVowels)
#     print("Sorted by least vowels:", listSortByTheLeastVowels)
#     print("List of words: capitalize every other character:", listCapitalizeEveryOtherCharacter)
#     print("List of words: reverse order:", listReverseWordOrdering)
#     print("List of words: fold words on middle of list:", listFoldWordsOnMiddleOfList)
#
# def AskUserProcessAnotherList():
#     boolAskingUserInput = True
#     boolCreateAnotherList = None
#     inputAddAnotherList = input("Process another list? (y/n) ")
#
#     while(boolAskingUserInput):
#         if (inputAddAnotherList == "y" or inputAddAnotherList == 'n'):
#             if (inputAddAnotherList == "y"):
#                 boolAskingUserInput = False
#                 boolCreateAnotherList = True
#                 break
#             if (inputAddAnotherList == "n"):
#                 boolAskingUserInput = False
#                 break
#         else:
#             # prompt user "Please enter correct syntax"
#             print("Please enter \"y\" or \"n\"")
#             continue
#     return boolCreateAnotherList
# main()



# class Person:
#
#     def __init__(self, first, last, age):
#         self.firstname = first
#         self.lastname = last
#         self.age = age
#
#     def __str__(self):
#         return self.firstname + " " + self.lastname + ", " + str(self.age)
#
# class Employee(Person):
#
#     def __init__(self, first, last, age, staffnum):
#         super().__init__(first, last, age)
#         self.staffnumber = staffnum
#
#     def __str__(self):
#         # return super().__str__() + ", " +  self.staffnumber
#         return 'doh'
#
#
# x = Person("Marge", "Simpson", 36)
# y = Employee("Homer", "Simpson", 28, "1007")
#
# print(x)
# print(y)



# class AbstractClassExample(ABC):
#     @abstractmethod
#     def do_something(self):
#         ''' To override '''
#         pass
#         # print("Some implementation!")
#
#     @abstractmethod
#     def do_something_cool(self):
#         ''' To override '''
#         pass

# tempList = [.3,.04,.01,.05]
# newList = []
#
# for val in tempList:
#     resultant =(100 * val)
#     newList.append(resultant)
#
# print(sorted(newList, key=int))

# templist = [25, 50, 100, 150, 200, 250, 300, 33]
# print(sorted(templist, key=int))


# import tensorflow as tf
#
#
# c = np.array([[3.,4], [5.,6], [6.,7]])
# # print(np.mean(c,1))
#
# Mean = tf.reduce_mean(c,1)
# with tf.Session() as sess:
#     result = sess.run(Mean)
#     print(result)


import numpy as np

# a = np.array([[1, 2], [3, 4]])
# a = np.array([1,2,3,4,5])
# print(np.mean(a))
#
# print(np.std(a))
# print(np.std(np.array([0,1])))

#Using spread calculate common volatility scenarios.
#Calculate desired spread range.

#Given time range and interval, values

#8:30 - 9:30, how many five minute sets? 60/5 = 12 sets

#In scenario where we measure the first index of each FM set.
#determine aproximate pchg value set.





# def create_pchg_value_list(test_set):
#     #Return pchg_list absolute values
#     pchg_list = []
#     index_count = 0
#     current_value = None
#     previous_value = None
#     while(index_count < len(test_set)):
#         current_value = test_set[index_count]
#         #previous current value measurement difference, add difference to calculation list
#         if(previous_value == None):
#             previous_value = current_value
#             index_count += 1
#             continue
#
#         print("current_value", current_value,"previous_value",previous_value)
#         pchg_difference = np.absolute(100*(((current_value - previous_value)/previous_value)))
#         print("pchg_difference", pchg_difference)
#         pchg_list.append(pchg_difference)
#         previous_value = current_value
#         index_count += 1
#     return pchg_list
#
#
# test_set1 = np.array([20.0,20.2,20.04,20.30])
#
# print(create_pchg_value_list(test_set1))
#
#
#
# #Now given a bought sell point and approximation differences,
# #Still need to determine spread of of values, of simulated successful test set
# #Need truthy data. Need to wait till week begins then we can start recording spreads, doing so programmatically and storing data for extra points.
# #Break here.
#
# #Given bought price, calculate when to buy or sell given new code_tool_set
#
#
# #ongoing, given price and current first FM index
#
# def calculate_pchg_delimiter_met(bought_price, five_set_set):
#     #Return pchg_list absolute values
#     pchg_delimiter = 2.0
#     is_pchg_delimiter_met = False
#     five_minute_first_index_value = five_set_set[0]
#     #previous current value measurement difference, add difference to calculation list
#
#     # print("bought_price", bought_price,"five_minute_first_index_value",five_minute_first_index_value)
#     pchg_difference = np.absolute(100*(((five_minute_first_index_value - bought_price)/bought_price)))
#     print("pchg_difference", pchg_difference)
#
#     if(pchg_difference>=pchg_delimiter):
#         is_pchg_delimiter_met = True
#
#     return is_pchg_delimiter_met
#
#
# five_minute_set = [[20.0],[20.1],[20.15],[20.20],[20.3],[20.4], [20.41]]
# for val in five_minute_set:
#     if(calculate_pchg_delimiter_met(20.0, val)):
#         print("selling stock")
#     else:
#         print("value less than delimiter")














# def sort_values_by_pchg(test_set):
#     # print('SortByLeastVowels')
#     # calculatedList = sorted(test_set, key=lambda val: sort_determine_pchg(val))
#     calculated_list = sort_determine_pchg(test_set)
#     print(calculated_list)
#     return calculated_list
#
# def sort_determine_pchg(test_set):
#     # Intializing count variable to 0
#     count = 0
#     # Creating a set of vowels
#     # vowel = set("aeiouAEIOU")
#     # Loop to traverse the alphabet in the given string
#     for alphabet in str:
#         # If alphabet is present in set vowel
#         if alphabet in vowel:
#             count = count + 1
#     return count


# from Calendar_Tracker import Calendar_Tracker
#
# cm = Calendar_Tracker()
# print(cm.get_formated_date())




import smtplib
#
# from string import Template
#
# from .mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# MY_ADDRESS = 'commandercarr1@gmail.com'
# PASSWORD = 'Lilylucy5!'
#
#
# # def get_contacts(filename):
# #     """
# #     Return two lists names, emails containing names and email addresses
# #     read from a file specified by filename.
# #     """
# #
# #     names = []
# #     emails = []
# #     with open(filename, mode='r', encoding='utf-8') as contacts_file:
# #         for a_contact in contacts_file:
# #             names.append(a_contact.split()[0])
# #             emails.append(a_contact.split()[1])
# #     return names, emails
#
#
# # def read_template(filename):
# #     """
# #     Returns a Template object comprising the contents of the
# #     file specified by filename.
# #     """
# #
# #     with open(filename, 'r', encoding='utf-8') as template_file:
# #         template_file_content = template_file.read()
# #     return Template(template_file_content)
#
#
# def main():
#     # names, emails = get_contacts('mycontacts.txt')  # read contacts
#     # message_template = read_template('message.txt')
#
#     # set up the SMTP server 465 587
#     s = smtplib.SMTP(host='commandercarr1@gmail.com', port=465)
#     s.starttls()
#     s.login(MY_ADDRESS, PASSWORD)
#
#
#
#     msg = MIMEMultipart()  # create a message
#
#     # # add in the actual person name to the message template
#     message = "hey"#message_template.substitute(PERSON_NAME=name.title())
#
#     # Prints out the message body for our sake
#     print(message)
#
#     # setup the parameters of the message
#     msg['From'] = MY_ADDRESS
#     msg['To'] = "commandercarr1@gmail.com"
#     msg['Subject'] = "Coding guru"
#
#     # add in the message body
#     msg.attach(MIMEText(message, 'plain'))
#
#     # send the message via the server set up earlier.
#     s.send_message(msg)
#     del msg
#
#     # Terminate the SMTP session and close the connection
#     s.quit()
#
#
# if __name__ == '__main__':
#     main()


# server = smtplib.SMTP('smtp.gmail.com:587')
# server.ehlo()
# server.starttls()
#
# msg = "\r\n".join([
#   "From: commandercarr1@@gmail.com",
#   "To: commandercarr1@gmail.com",
#   "Subject: Just a message",
#   "",
#   "Why, oh why"
#   ])




# def json_creater(self, list_of_values):
#     # chosen_stock_stat = data_manager_action.get_chosen_stock_statistics()
#     # Support for sell field updates
#
#     # json_begining = "{"
#     json_request = {"request_type": "store_data_manager_action",
#                     "sym": sym,
#                     "pchg": pchg,
#                     "last": last,
#                     "spread": spread,
#                     "list_date": list_date
#                     }
#     return json_request





# import aiohttp
# import asyncio
# from threading import Thread
# # from Request_Factory import Request_Factory
#
# class Node_Manager:
#     __instance = None
#     def __new__(self):
#         if self.__instance == None:
#             self.__instance = object.__new__(self)
#             # self.request_factory = Request_Factory()
#         return self.__instance
#
#     async def fetch(self,session, url, data):
#         async with session.post(url, data=data) as response:
#             return await response.text()
#
#     async def test_list_post(self,list_items):
#         async with aiohttp.ClientSession() as session:
#             json_request = json_request = {
#                     "request_type": "test_list_post",
#                     "sym": "symbol",
#                     "list_items": list_items
#                     }
#             url = 'http://localhost:3000/api/brokerage'
#             response_returned = await self.fetch(session, url, json_request)
#             return response_returned
#
# nm = Node_Manager()
#
#
#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# response = loop.run_until_complete(nm.test_list_post([1,2,3]))

# chosen_conditional_symbol1 = 'yo'
# conditional_dictionary = {chosen_conditional_symbol1: False,"chosen_conditional_symbol2": False,"chosen_conditional_symbol3": False}
#         # chosen_stock_temp_container_index = 0
#
# conditional_dictionary["yo"] = True
#
# print(conditional_dictionary)


# def validate_chosen_data_manager_bundle():
#     conditional_dictionary = create_conditional_dictionary()
#
#     #Validate all conditions in dictionary are true
#     for key in conditional_dictionary:
#
#
# def create_conditional_dictionary():
#     chosen_stock_temp_container = ["test1", "test2", "test3"]
#
#     # for data_manager in self.list_chosen_data_managers:
#     # chosen_conditional_symbol1 = self.list_chosen_data_managers[0].get_sym()
#     # chosen_conditional_symbol2 = self.list_chosen_data_managers[1].get_sym()
#     # chosen_conditional_symbol3 = self.list_chosen_data_managers[2].get_sym()
#
#     chosen_conditional_symbol1 = "test2"
#     chosen_conditional_symbol2 = "test1"
#     chosen_conditional_symbol3 = "test5"
#
#     conditional_dictionary = {chosen_conditional_symbol1: False, chosen_conditional_symbol2: False,
#                               chosen_conditional_symbol3: False}
#
#     chosen_stock_temp_container_index = 0
#
#     for stock in chosen_stock_temp_container:
#         if (chosen_stock_temp_container_index == 0):
#             if (stock == chosen_conditional_symbol1):
#                 conditional_dictionary[chosen_conditional_symbol1] = True
#             if (stock == chosen_conditional_symbol2):
#                 conditional_dictionary[chosen_conditional_symbol2] = True
#             if (stock == chosen_conditional_symbol3):
#                 conditional_dictionary[chosen_conditional_symbol3] = True
#
#         if (chosen_stock_temp_container_index == 1):
#             if (stock == chosen_conditional_symbol1):
#                 conditional_dictionary[chosen_conditional_symbol1] = True
#             if (stock == chosen_conditional_symbol2):
#                 conditional_dictionary[chosen_conditional_symbol2] = True
#             if (stock == chosen_conditional_symbol3):
#                 conditional_dictionary[chosen_conditional_symbol3] = True
#
#         if (chosen_stock_temp_container_index == 2):
#             if (stock == chosen_conditional_symbol1):
#                 conditional_dictionary[chosen_conditional_symbol1] = True
#             if (stock == chosen_conditional_symbol2):
#                 conditional_dictionary[chosen_conditional_symbol2] = True
#             if (stock == chosen_conditional_symbol3):
#                 conditional_dictionary[chosen_conditional_symbol3] = True
#
#         chosen_stock_temp_container_index += 1
#     print(conditional_dictionary)
#     return conditional_dictionary
#
# validate_chosen_data_manager_bundle()


# def validate_chosen_data_manager_dictionary(conditional_dictionary):
#     temporary_value_list = []
#     for key in conditional_dictionary:
#         print(conditional_dictionary[key])
#         temporary_value_list.append(conditional_dictionary[key])
#     #If False positive exists in conditional list, then clear stock list
#     if False in temporary_value_list:
#         print("clearing stock list")
#         print("clearing conditional_dictional? list")
#     else:
#         print("creating request")
#
#
#
# conditional_dictionary = {"sym1": False, "sym2": True,
#                          "sym3": True}
# validate_chosen_data_manager_dictionary(conditional_dictionary)


# from Data_Manager_Request_Bundler import Data_Manager_Request_Bundler




def create_request_bundle(hourValue, tenMinuteValue, fiveMinuteValue):
    # stock1 = self.chosen_stock_temp_container[0]
    # stock2 = self.chosen_stock_temp_container[1]
    # stock3 = self.chosen_stock_temp_container[2]

    json = {
        # "stock_symbol_1": stock1.get_sym(),
        # "stock_last_1": stock1.get_last(),
        # "stock_pchg_1": stock1.get_pchg(),
        # "stock_bid_1": stock1.get_bid(),
        # "stock_ask_1": stock1.get_ask(),
        #
        # "stock_symbol_2": stock2.get_sym(),
        # "stock_last_2": stock2.get_last(),
        # "stock_pchg_2": stock2.get_pchg(),
        # "stock_bid_2": stock2.get_bid(),
        # "stock_ask_2": stock2.get_ask(),
        #
        # "stock_symbol_3": stock3.get_sym(),
        # "stock_last_3": stock3.get_last(),
        # "stock_pchg_3": stock3.get_pchg(),
        # "stock_bid_3": stock3.get_bid(),
        # "stock_ask_3": stock3.get_ask(),
        "request_type": "data_manager_request_bundle",
        "isGetLatestHourSet": 0,
        "isGetLatestTenMinuteSet": 0,
        "isGetLatestFiveMinuteSet": 0,
        "isGetLatestStockSet": 0,

        "dataBundleRecordSetInitiation": 0,
        "dataBundleDaySetInitiation": 0,
        "isHourChangeover": hourValue,
        "isTenMinuteChangeover": tenMinuteValue,
        "isFiveMinuteChangeover": fiveMinuteValue,
        "isStockStore": 0

        # ,

        # "stock_symbol_1": "sym1",
        # "stock_last_1": "last1",
        # "stock_pchg_1": 'pchg1',
        # "stock_bid_1": 'bid1',
        # "stock_ask_1": 'ask1',
        #
        # "stock_symbol_2": "sym5",
        # "stock_last_2": "last2",
        # "stock_pchg_2": "pchg2",
        # "stock_bid_2": 'bid2',
        # "stock_ask_2": 'ask2',
        #
        # "stock_symbol_3": 'sym3',
        # "stock_last_3": 'last3',
        # "stock_pchg_3": 'pchg3',
        # "stock_bid_3": 'bid3',
        # "stock_ask_3": 'ask3'
    }
    return json

jsonResponse = create_request_bundle(1,0,0)
print(jsonResponse)
