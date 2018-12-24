
import aiohttp
import asyncio
from threading import Thread
from Request_Factory import Request_Factory


# from Request_Factory import Request_Factory
# from Type_Converter import Type_Converter
from Thread_Task import Thread_Task
class HTTP_Utility:

    def __init__(self,):#typeConverter,requestFactory):
        self.name = ''
        self.request_factory = Request_Factory()

    async def fetch(self,session, url, data):
        async with session.post(url, data=data) as response:
            return await response.text()

    async def async_post_stock(self,data,requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.query_stock_symbol(data)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    # async def async_post_top_stock(self,requestFactory):
    #     async with aiohttp.ClientSession() as session:
    #         jsonRequest = requestFactory.top_stock_pull()
    #         url = 'http://localhost:3000/api/brokerage'
    #         responseReturned = await self.fetch(session, url, jsonRequest)
    #         return responseReturned

#Top Stock
    async def async_post_stock_top_phase_internal(self,requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.lookup_top_stocks_phase_internal()
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_stock_top_phase1(self, data, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.lookup_top_stocks_phase2(data)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_stock_top_phase2(self, topStockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.lookup_top_stocks_phase3(topStockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned




#Query
    async def async_post_stock_query_phase1(self, stockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_stock_query_phase1(stockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_query_stock(self, symbol):
        async with aiohttp.ClientSession() as session:
            jsonRequest = self.request_factory.async_query_stock(symbol)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned
    # async def async_post_stock_query_phase1(self, stockComposite, requestFactory):
    #     async with aiohttp.ClientSession() as session:
    #         jsonRequest = requestFactory.async_post_stock_query_phase1(stockComposite)
    #         url = 'http://localhost:3000/api/brokerage'
    #         responseReturned = await self.fetch(session, url, jsonRequest)
    #         return responseReturned




#Account
    async def async_post_account_information_phase2(self, account_information, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_account_information_phase2(account_information)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_account_information_phase3(self, stockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_account_information_phase3(stockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned


#Buy
    async def async_post_market_buy_phase1(self, data, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_buy_phase1(data)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_buy_phase2(self, stock, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_buy_phase2(stock)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_buy_phase3(self, stock, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_buy_phase3(stock)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)


#Sell
    async def async_post_market_sell_phase1(self, data, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_sell_phase1(data)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_sell_phase2(self, DM_Action, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_sell_phase2(DM_Action)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned

    async def async_post_market_sell_phase3(self, stockComposite, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.async_post_market_sell_phase3(stockComposite)
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)





    async def test(self, requestFactory):
        async with aiohttp.ClientSession() as session:
            jsonRequest = requestFactory.test()
            url = 'http://localhost:3000/api/brokerage'
            responseReturned = await self.fetch(session, url, jsonRequest)
            return responseReturned
    # async def async_post_stock_top_simple(self, data, requestFactory):
    #     async with aiohttp.ClientSession() as session:
    #         jsonRequest = requestFactory.query_stock_symbol_top_simple(data)
    #         url = 'http://localhost:3000/api/brokerage'
    #         responseReturned = await self.fetch(session, url, jsonRequest)
    #         return responseReturned
            # request_type == "store_top_stock_symbol"

    # async def async_post_top_stock_DB(self,json_to_DB):
    #     async with aiohttp.ClientSession() as session:
    #         print(json_to_DB)
    #         responseReturned = await fetch(session, 'http://localhost:3000/api/brokerage', json_to_DB)
    #         print(responseReturned)
    #         # topStockComposite.set_jsonTopStocks(jsonConverted)

    # def post_request_top_stocks(requestCode, topStockComposite):
    #     typeConverter = Type_Converter()
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(async_post_top_stock(requestCode, topStockComposite))
    #     topStockComposite.set_highest_chosen()
    #     topStockComposite.calc_highest_chosen()
    #     topStockComposite.collect_top_stock_results_in_list()
    #     data_list = topStockComposite.get_listChosenStocks()
    #     json_to_DB = typeConverter.top_stocks_convert_to_JSON(data_list)
    #     print(json_to_DB)
    #
    #     # print(data_to_post)
    #     # topStockComposite.convert_to_JSON
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(async_post_top_stock_DB(json_to_DB))







    # {"request_type": "query_stock",
    #  "symbol": "BMA"
    #  }

    # Give it some async work
    # future = asyncio.run_coroutine_threadsafe(
    #     fetch(),
    #     new_loop
    # )
    # Wait for the result
    # print(future.result())
# Do it again but with a callback
# def test_thread_async:
#     asyncio.run_coroutine_threadsafe(
#         fetch(),
#         new_loop
#     ).add_done_callback(lambda future: print(future.result()))
















# def post_request(url, jsonPayload):
#     internalUrl = url
#     payload = jsonPayload
#     # Adding empty header as parameters are being sent in payload
#     headers = {"Content-Type": "application/json"}
#     r = requests.post(internalUrl, data=json.dumps(jsonPayload), headers=headers)
#     print(r.content)
#     return r.content
