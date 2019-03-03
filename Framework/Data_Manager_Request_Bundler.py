import asyncio
from threading import Thread
from Node_Manager import Node_Manager
from Scraper_Manager import Scraper_Manager
from Perpetual_Timer import Perpetual_Timer

class Data_Manager_Request_Bundler:
    def __init__(self):
        self.sym = None
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []
        self.operation_center = None
        self.time_data_set_manager = None
        self.is_data_bundle_initialization_required = True
        self.is_init_scraped = True

        self.isGetLatestHourSet = 0
        self.isGetLatestTenMinuteSet = 0
        self.isGetLatestFiveMinuteSet = 0
        self.isGetLatestStock = 0

        self.dataBundleRecordSetInitiation = 0
        self.dataBundleDaySetInitiation = 0
        self.isHourChangeoverValue = 0
        self.isTenMinuteChangeoverValue = 0
        self.isFiveMinuteChangeoverValue = 0
        self.isStockStoreValue = 1
        self.isScrapeStoreValue = 1
        self.isInitVolumeDowProcessing = 1
        self.isInitScrape = 1



    def setup_data_manager_request_bundler(self, operation_center, time_data_set_manager):
        # self.sym = sym
        self.operation_center = operation_center
        self.time_data_set_manager = time_data_set_manager

    def create_scrape_bundle_request(self, sym_list):
        # if(self.is_init_scraped):
        #     scrape_composite = self.create_scrape_composite(sym_list)
        #     self.is_init_scraped = False
        # else:
        scrape_composite = self.create_scrape_composite(sym_list)
            # self.isInitScrape = 0
        # print(scrape_composite)
        json = self.create_scrape_request_bundle(scrape_composite)
        print("json: " + str(json))
        self.post_request_bundle(json)

    def create_scrape_composite(self, sym_list):
        scraper_manager = Scraper_Manager()
        resultsComposite = []
        for symbol in sym_list:
            resultsList = []
            industry = scraper_manager.industry_scrape(symbol)
            dow = scraper_manager.dow_scrape()
            volumeList = scraper_manager.volume_scrape(symbol)

            resultsList.append(industry)
            resultsList.append(dow)
            resultsList.append(volumeList)
            resultsList.append(symbol)

            resultsComposite.append(resultsList)
        return resultsComposite

    def create_scrape_request_bundle(self, scrape_composite):
        json = {
            "request_type": "data_manager_request_bundle",
            "isScrapeStore": 1,
            "isInitScrape": self.isInitScrape,
            "dow": scrape_composite[0][1],

            "symbol1": scrape_composite[0][3],
            "industry1": scrape_composite[0][0],
            "volume1": scrape_composite[0][2][0],
            "avgVolume1":scrape_composite[0][2][1],

            "symbol2": scrape_composite[1][3],
            "industry2": scrape_composite[1][0],
            "volume2": scrape_composite[1][2][0],
            "avgVolume2": scrape_composite[1][2][1],

            "symbol3": scrape_composite[2][3],
            "industry3": scrape_composite[2][0],
            "volume3": scrape_composite[2][2][0],
            "avgVolume3": scrape_composite[2][2][1]
        }
        return json


    def process_stock_store(self, stock):
        # print("hit process_stock_store")
        # if (self.is_data_bundle_initialization_required):
        #     # print("Value of bool bundle: " + str(self.is_data_bundle_initialization_required))
        #     self.is_data_bundle_initialization_required = False
        #     self.process_data_initialization(stock)
        #     self.reset_data_initialization_value()
        #     return
        # else:
        json = self.create_request_bundle(stock)
        # print("else json: " + str(json))
        self.post_request_bundle(json)
        self.reset_process_changeover_request()

    def process_data_initialization(self, stock):
        self.dataBundleRecordSetInitiation = 1
        json = self.create_request_bundle(stock)
        # self.reset_data_initialization_value()
        print("bundle init json: " + str(json))
        self.post_request_bundle(json)

    def reset_data_initialization_value(self):
        print("reset data intialization")
        self.dataBundleRecordSetInitiation = 0

    def process_changeover(self, type):
        if (type == "hour"):
            self.isHourChangeoverValue = 1
            return
        if (type == "ten"):
            self.isTenMinuteChangeoverValue = 1
            return
        if (type == "five"):
            self.isFiveMinuteChangeoverValue = 1

    def reset_process_changeover_request(self):
        self.isHourChangeoverValue = 0
        self.isTenMinuteChangeoverValue = 0
        self.isFiveMinuteChangeoverValue = 0

    def create_request_bundle(self, stock):
        json = {
            "request_type": "data_manager_request_bundle",
            "isGetLatestHourSet": self.isGetLatestHourSet,
            "isGetLatestTenMinuteSet": self.isGetLatestTenMinuteSet,
            "isGetLatestFiveMinuteSet": self.isGetLatestFiveMinuteSet,
            "isGetLatestStock": self.isGetLatestStock,

            "dataBundleRecordSetInitiation": self.dataBundleRecordSetInitiation,
            "dataBundleDaySetInitiation": self.dataBundleDaySetInitiation,
            "isHourChangeover": self.isHourChangeoverValue,
            "isTenMinuteChangeover": self.isTenMinuteChangeoverValue,
            "isFiveMinuteChangeover": self.isFiveMinuteChangeoverValue,
            "isStockStore": self.isStockStoreValue,

            "stock_symbol": stock.get_sym(),
            "stock_last": stock.get_last(),
            "stock_pchg": stock.get_pchg(),
            "stock_bid": stock.get_bid(),
            "stock_ask": stock.get_ask()
        }
        return json

    def post_request_bundle(self, json):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(
            self.operation_center.node_manager.async_post_data_manager_request_bundle(
                json))
