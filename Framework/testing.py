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


# scraper_manager = Scraper_Manager()
# # print(scraper_manager.industry_scrape("aapl"))
# sleep(2)
# # print(scraper_manager.dow_scrape())
# print(scraper_manager.volume_scrape("aapl"))



# scraper_manager.industry_scrape("aapl")


# dmrb = Data_Manager_Request_Bundler()
# dmrb.create_scrape_bundle_request(["aapl","nvda","ko"])



# dmrb.on_time_interval_retrieve_dow_volume("aapl")

# sm = Scraper_Manager()
# dowResult = sm.dow_scrape()
# result = sm.volume_scrape("aapl")
# print(result["Volume"])
# print(dowResult)


# internalIndex = 1
# a = [0, 1, 2]
# endSliceIndex = internalIndex + 1
# del a[internalIndex:endSliceIndex]
# print(a)

# old_list = ["A","B"]
# chosen_sym = "C"
# new_list = ["F","B","C"]
#
# match_results = []
# for new_sym in new_list:
#     for old_sym in old_list:
#         if(new_sym == old_sym):
#             match_results.append(new_sym)
# for new_sym in new_list:
#     if(chosen_sym == new_sym):
#         match_results.append(chosen_sym)
#
# print("Match results: " + str(match_results))
#
#
# for match_item in match_results:
#     new_list.remove(match_item)
#
# print("Finalized new_list: "+str(new_list))


chosen_sym = "0"

if(chosen_sym != "0"):
    print("hit")