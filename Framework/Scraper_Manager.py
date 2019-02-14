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
        print(summary_table[0].text)
        try:
            print("break")
        except:
            print("Failed to parse json response")
            return {"error": "Failed to parse json response"}



# if __name__ == "__main__":
#     scraped_data = scrape_dow()
#     # print("Writing data to output file")
#     # with open('%s-ssummary.json' % (ticker), 'w') as fp:
#     #     json.dump(scraped_data, fp, indent=4)