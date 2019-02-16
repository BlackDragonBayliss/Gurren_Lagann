from lxml import html
import requests
from time import sleep
import json
import argparse
from collections import OrderedDict
from time import sleep

class Scraper_Manager:

    def dow_scrape(self):
        url = "https://finance.yahoo.com/quote/%5EDJI/"
        response = requests.get(url, verify=False)
        parser = html.fromstring(response.text)
        summary_table = parser.xpath('// *[ @ id = "quote-header-info"] / div[3] / div / span')
        # print(summary_table[0].text)
        try:
            print("break")
            return summary_table[0].text
        except:
            print("Failed to parse json response")
            return {"error": "Failed to parse json response"}

    def volume_scrape(self, ticker):
        url = "http://finance.yahoo.com/quote/%s?p=%s" % (ticker, ticker)
        response = requests.get(url, verify=False)
        # print("Parsing %s" % (url))
        # sleep(2)
        parser = html.fromstring(response.text)
        # print(response.text)
        summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
        summary_data = []
        try:
            for table_data in summary_table:
                raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()')
                raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
                if(raw_table_key[0] == 'Volume'):
                    table_value = ''.join(raw_table_value).strip()
                    summary_data.append(table_value)
                if (raw_table_key[0] == 'Avg. Volume'):
                    table_value = ''.join(raw_table_value).strip()
                    summary_data.append(table_value)
            return summary_data
        except:
            print("Failed to parse json response")
            return {"error": "Failed to parse json response"}

    def industry_scrape(self, ticker):
        url = "https://finance.yahoo.com/quote/%s/profile?ltr=1" % (ticker)
        response = requests.get(url, verify=False)
        # sleep(0)
        parser = html.fromstring(response.text)
        summary_table = parser.xpath('//div[contains(@class, "asset-profile-container")] / div / div / p[2] / span[4]')
        # print(summary_table[0].text)
        return summary_table[0].text