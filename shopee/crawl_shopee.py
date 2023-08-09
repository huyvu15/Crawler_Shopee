import scrapy
import json
import time
import requests
import pandas  as pd

# url = 'https://shopee.vn/api/v4/pdp/hot_sales/get?item_id={}&limit=8&offset=0&shop_id={}'.format(item_id, shop_id)


# https://shopee.vn/api/v4/pdp/hot_sales/get?item_id=13394037852&limit=8&offset=0&shop_id=738752794
# https://shopee.vn/api/v4/pdp/hot_sales/get?item_id=18817660412&limit=8&offset=0&shop_id=51979390


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

params = {
    'item_id': '13394037852',
    'limit': '8',
    'offset': '0',
    'shop_id': '738752794',
}

def get_url():
    # urls = []
    # for i in range(0, 50):
    #     url = 'https://shopee.vn/api/v4/'
    #     urls.append(url)
    # return urls
    url = 'https://shopee.vn/api/v4/official_shop/get_shops'
    return url

def url_detail(url):
    req = requests.get(url, headers=headers).json()
    print(req)
    rows = req['items']
    detail_urls = []
    for i in range(0, len(rows)):
        name = req['items'][i]['item_basic']['name']
        itemid = req['items'][i]['itemid']
        shopid = req['items'][i]['item_basic']['shopid']
        detail_url = 'https://shopee.vn/api/v4/pdp/hot_sales/get?item_id={}&limit=8&offset=0&shop_id={}'.format(itemid, shopid)
        detail_urls.append(detail_url)
    return detail_urls

def scrape_product(url):
    req = requests.get(url, headers=headers).json()

def data_frame(data):
    df = pd.DataFrame(data, columns=[])
    return df

def save_to_csv(df):
    df.to_excell('Shopee_dt.csv', index = False)
    print("Load success!")

if __name__ == '__main__':
    urls = get_url()
    get_detail_urls = url_detail(urls)
    for i in range(len(get_detail_urls)):
        print(get_detail_urls[i])
        