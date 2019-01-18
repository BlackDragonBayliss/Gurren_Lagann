import aiohttp
import asyncio
from threading import Thread
from Request_Factory import Request_Factory

class Node_Manager:
    __instance = None
    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
            self.request_factory = Request_Factory()
        return self.__instance

    async def fetch(self,session, url, data):
        async with session.post(url, data=data) as response:
            return await response.text()

    async def async_post_node_manager_query(self, sym):
        async with aiohttp.ClientSession() as session:
            json_request = self.request_factory.async_post_node_manager_query(sym)
            url = 'http://localhost:3000/api/brokerage'
            response_returned = await self.fetch(session, url, json_request)
            return response_returned
            # data_manager.handle_stock_response(response_returned)

    async def async_post_stock_statistics_composite(self,stock_statistics_composite):
        async with aiohttp.ClientSession() as session:
            json_request = self.request_factory.async_post_stock_statistics_composite(sym)
            url = 'http://localhost:3000/api/brokerage'
            response_returned = await self.fetch(session, url, json_request)
            return response_returned

    async def async_post_data_manager_request_bundle(self,bundle):
        async with aiohttp.ClientSession() as session:
            url = 'http://localhost:3000/api/brokerage'
            response_returned = await self.fetch(session, url, bundle)
            return response_returned


    async def async_post_data_manager_action(self, data_manager_action):
        async with aiohttp.ClientSession() as session:
            json_request = self.request_factory.async_post_data_manager_action(data_manager_action)
            url = 'http://localhost:3000/api/brokerage'
            response_returned = await self.fetch(session, url, json_request)
            return response_returned
    #Query stocks, (One request for many? Or multiple aysnc?
    #More effiecient but a lot more work.



