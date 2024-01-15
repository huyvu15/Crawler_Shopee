import scrapy
import json
from scrapy import cmdline
from json import JSONDecodeError
import logging
import pandas as pd

def read_file(file_path):
    df = pd.read_csv(file_path)
    val1 = df.iloc[:, 0].tolist()
    val2 = df.iloc[:, 1].tolist()
    return zip(val1, val2) 

class TkapiSpider(scrapy.Spider):
    name = 'shoapi'
    #start_urls = ["https://tiki.vn/api/v2/products/53434797"]
    # allowed_domains = ['s']
    # start_urls = ['http://s/']

    custom_settings = {
        'FEED_EXPORT_ENCODING' : 'utf-8',
        'DOWNLOAD_DELAY': 0.5
    }

    headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "Referer": "https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        # p_ids cào trước đấy r nên cop vào luôn
        # p_ids = [21629119012,20629525662,19223431141,16678471917,20904955764,20069617451,16683003980,18915582729,5889370218,22420455071,19034000188,3891290785,13020630143,6939920023,17576448641,13836258622,21633997839,16678443885,18669618211,19114558641,15868812301,16533708397,13044811624,13130290475,14654134203,17185278936,13029640323,16191698796,23602512114,19752207535,10759471980,14486825868,15281707071,22216000773,10990560552,18108291820,18149706578,4118825280,17717880938,17076859914,7356560914,13468609188,12867213806,21150081757,10759106184,19626432358,14308620174,3791784325,13413609496,20749487390,13719247167,17230021278,14486390461,16519730639,18921835382,21636466767,14313778244,8816262269,17082708831,15515084003,20629525662,19223431141,16678471917,20904955764,20069617451,16683003980,18915582729,5889370218,22420455071,19034000188,3891290785,13020630143,6939920023,17576448641,13836258622,21633997839,16678443885,18669618211,19114558641,15868812301,16533708397,13044811624,13130290475,14654134203,17185278936,13029640323,16191698796,23602512114,19752207535,10759471980,14486825868,15281707071,22216000773,10990560552,18108291820,18149706578,4118825280,17717880938,17076859914,7356560914,13468609188,12867213806,21150081757,10759106184,19626432358,14308620174,3791784325,13413609496,20749487390,13719247167,17230021278,14486390461,16519730639,18921835382,21636466767,14313778244,8816262269,17082708831,15515084003,2623103363,19223431141,16678471917,20904955764,20069617451,16683003980,18915582729,5889370218,22420455071,19034000188,3891290785,13020630143,6939920023,17576448641,13836258622,21633997839,16678443885,18669618211,19114558641,15868812301,16533708397,13044811624,13130290475,14654134203,17185278936,13029640323,16191698796,23602512114,19752207535,10759471980,14486825868,15281707071,22216000773,10990560552,18108291820,18149706578,4118825280,17717880938,17076859914,7356560914,13468609188,12867213806,21150081757,10759106184,19626432358,14308620174,3791784325,13413609496,20749487390,13719247167,17230021278,14486390461,16519730639,18921835382,21636466767,14313778244,8816262269,17082708831,15515084003,2623103363,11356997243,16678471917,20904955764,20069617451,16683003980,18915582729,5889370218,22420455071,19034000188,3891290785,13020630143,6939920023,17576448641,13836258622,21633997839,16678443885,18669618211,19114558641,15868812301,16533708397,13044811624,13130290475,14654134203,17185278936,13029640323,16191698796,23602512114]
        
        #yield scrapy.Request(url=url, callback=self.parser_product, headers=self.headers, dont_filter=False)
        for i, j in read_file('product_id1.csv'):
            #https://shopee.vn/api/v4/pdp/get_pc?shop_id=81075907&item_id=21629119012
            url=f"https://shopee.vn/api/v4/pdp/get_pc?shop_id={j}&item_id={i}"
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
                return
               
        #resp = json.loads(response.body) 
        yield{
            'name' : resp['name']
            # 'original_price' : resp['original_price'],
            # 'discount' :resp['discount'],
            # 'price' : resp['price'],
            # 'rating_average' : resp['rating_average'],
            # 'review_count' : resp['review_count'],
            # 'productset_group_name': resp['productset_group_name'],
            # 'sold' : sold
        }
cmdline.execute("scrapy runspider tkapi.py -O file.json".split())




   
