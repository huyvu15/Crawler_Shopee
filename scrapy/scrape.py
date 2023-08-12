import scrapy
import json
from scrapy import cmdline
from json import JSONDecodeError
import logging


class TkapiSpider(scrapy.Spider):
    name = 'tkapi'
    #start_urls = ["https://tiki.vn/api/v2/products/53434797"]
    # allowed_domains = ['s']
    # start_urls = ['http://s/']

    custom_settings = {
        'FEED_EXPORT_ENCODING' : 'utf-8',
        'DOWNLOAD_DELAY': 0.5
    }

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://tiki.vn/he-mien-dich-kiet-tac-cua-su-song-p48895045.html?spid=48895046',
    'sec-ch-ua': '"Opera";v="95", "Chromium";v="109", "Not;A=Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0',
    'x-guest-token': 'tYnAkieDWjgsyPu8om1Fr9fI2RzJSlZB'
    }

    def start_requests(self):
        # p_ids cào trước đấy r nên cop vào luôn
        p_ids = [53434797, 10005245, 2380007, 550167, 196201375, 74021317, 184466860, 189643105, 207841114, 3304875, 167940010, 109017985, 106863963, 52789367, 73787185, 8848897, 93249305, 213736028, 130327841, 106863963, 75953557, 198414891, 199216988, 117238177, 209891492, 15267827, 46240929, 147920903, 3954355, 188940817, 69764541, 26114399, 1476937, 121635152, 117254517, 206840682, 71345381, 4780917, 204078065, 207841170, 2380007, 8848897, 197337637, 91998790, 199684637, 72459686, 72882553, 3639597, 111285062, 17336364, 207256575, 57325187, 205942269, 106318762, 124767703, 174377494, 151591896, 50359874, 135552451, 45211100, 127844385, 157240665, 85763211, 194959173, 8885999, 197629362, 87226756, 168283405, 70016692]
        
        #yield scrapy.Request(url=url, callback=self.parser_product, headers=self.headers, dont_filter=False)
        for i in p_ids:
            url=f"https://tiki.vn/api/v2/products/{i}?platform=web&spid={i}"
            yield  scrapy.Request(url=url, callback=self.parser_product, headers=self.headers, dont_filter=False)
    
    def parser_product(self, response):
        if response.body == None or response.body == '':
            print('I got a null or empty string value for data in a file')
        else:
            try:
                resp = json.loads(response.body)
                if 'all_time_quantity_sold'  in resp:
                    sold = resp['all_time_quantity_sold']
                else:
                    sold = "No info"
            except ValueError:
                self.log("Error catch ValueError!!!")
               
        #resp = json.loads(response.body) 
        yield{
            'name' : resp['name'],
            'original_price' : resp['original_price'],
            'discount' :resp['discount'],
            'price' : resp['price'],
            'rating_average' : resp['rating_average'],
            'review_count' : resp['review_count'],
            'productset_group_name': resp['productset_group_name'],
            'sold' : sold
        }
        


cmdline.execute("scrapy runspider tkapi.py -O file.json".split())




   
