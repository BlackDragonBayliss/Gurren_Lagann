import asyncio
from threading import Thread
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
        self.is_init_scraped = False

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
        self.isInitVolumeDowProcessing = 1
        self.isInitScrape = 1




    def setup_data_manager_request_bundler(self, sym, operation_center, time_data_set_manager):
        self.sym = sym
        self.operation_center = operation_center
        self.time_data_set_manager = time_data_set_manager

    def create_scrape_bundle_request(self, symList):
        if(self.is_init_scraped):
            scrape_composite = self.create_scrape_composite(symList)
            # self.
            # pep_scrape_timer = Perpetual_Timer()
            # self.pep_scrape_timer.setup_timer_stock(1, 1000000, self.init_scrape_stats, symList)

    def create_scrape_composite(self, symList):
        scraper_manager = Scraper_Manager()
        resultsComposite = []
        for symbol in symList:
            resultsList = []
            industry = scraper_manager.industry_scrape(symbol)
            dow = scraper_manager.dow_scrape()
            volumeList = scraper_manager.volume_scrape(symbol)

            resultsList.append(industry)
            resultsList.append(dow)
            resultsList.append(volumeList)
            resultsComposite.append(resultsList)
        return resultsComposite

    # def getDowVolumeIndustryList(self, symbol):
    #     scraper_manager = Scraper_Manager()
    #     dow_volume_list = []
    #     dow_volume_list.append(scraper_manager.dow_scrape())
    #     listVolume = scraper_manager.volume_scrape(symbol)
    #     dow_volume_list.append(listVolume[0])
    #     dow_volume_list.append(listVolume[1])
    #     print(dow_volume_list)


    def process_stock_store(self, stock):
        print("hit process_stock_store")
        if (self.is_data_bundle_initialization_required):
            print("Value of bool bundle: " + str(self.is_data_bundle_initialization_required))
            self.is_data_bundle_initialization_required = False
            self.process_data_initialization(stock)
            self.reset_data_initialization_value()
            return
        else:
            json = self.create_request_bundle(stock)
            print("else json: " + str(json))
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
            return
        # self.isStockStoreValue = 1

    def reset_process_changeover_request(self):
        self.isHourChangeoverValue = 0
        self.isTenMinuteChangeoverValue = 0
        self.isFiveMinuteChangeoverValue = 0
        # self.isStockStoreValue = 0

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
            "stock_ask": stock.get_ask(),
        }
        return json

    def post_request_bundle(self, json):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(
            self.operation_center.node_manager.async_post_data_manager_request_bundle(
                json))
