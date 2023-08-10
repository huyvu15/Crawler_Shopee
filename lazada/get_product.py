import requests
import csv
import pandas as pd
import json


cookies = {
    "__wpkreporterwid_": "fc12b95f-2f4c-4304-2e76-fcc1d1f8542e",
    "miidlaz": "miidgk2c8k1h1vhhfidf5v1",
    "lzd_cid": "6507d41a-6e39-4ef8-849b-438e1de72866",
    "t_uid": "6507d41a-6e39-4ef8-849b-438e1de72866",
    "t_fv": "1685759509573",
    "lwrid": "AQGIfxjEcZQ61kAC2REJX39uI%2Bis",
    "cna": "FJQBHVrHHj0CASp1lUBL7qoU",
    "hng": "VN|vi|VND|704",
    "hng.sig": "EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s",
    "_bl_uid": "Cyl3pkOmww5xtU91e9Xakqz7dR7X",
    "_gcl_au": "1.1.1797887586.1691173971",
    "lzd_click_id": "clkgjnmrt1h782mph93tuv",
    "lzd_sid": "18629b4aa850899e3db701998c3e0cf3",
    "_tb_token_": "36b35ee1a30f7",
    "xlly_s": "1",
    "_m_h5_tk": "088832baaaf981790b714a496feb7b74_1691604020880",
    "_m_h5_tk_enc": "60a176f913f99d44f08cfc01e3a0825b",
    "ak_bmsc": "181EA67D50A02B0D3396190C051A2BB3~000000000000000000000000000000~YAAQCh4gF/ltX8+JAQAAthIH2xQDcVPTqCx9pAaYqLAUMd2KDsbXVxPZseQPscpn7+pXJQMdLafSAWPwe1CP76mAoOp6Q+6+1zONoWzUAqFEdmRYdRTiJ2z6vTlMOtRwpZplMhWH35EI8KcjS/PYMdzdK4HxrDtk4vgAlp1lUWZMzvPHokRLcJc63YFQBsomMnX5TbLt4NJXN6hbxj43MyNEi22CO+Y60l6kRy2fBG6AA2RQPVVMHHGM2Obb4x9RjtQy5Fe9YqoT+///QkxkaO6wSHxdFtcl0gyAZqv4jDY00m+spg4CkYMw7i1/E2mZlTXMWlg0ZxpgojUJHy9gHE8WhWIhv+FRYe9DCGEzwVFUcgC/VZSEvIoRrPsbtduR7/+d9PhT78Prh/tQaww3ZtRxonhgKEBMoVojv8PH1vKHaBBQYTwUqXtjOhJIO5dyiRmqlXP2lPkBSt7S5vp4bg5ANLEsh7+E0AKoz//dix4AFdV5g5Lwe+l59LxS97sCG+bqexY=",
    "t_sid": "gEvqSPQssxN8eOK9cVaw8czQGrx76QjS",
    "utm_channel": "NA",
    "_uetsid": "e494a31036cd11eebc180dbd6fd3880c",
    "_uetvid": "c633181032f511ee8cf92de38b3edd84",
    "cto_bundle": "5zHi2V9NNllybE9CTEpydlhoY1U3NlM1ZmFQQWlPY0t0TXByWDE2Z0k3eUpLa3J1OExOJTJCRGhJN01ZMVBId2ltOSUyQjhIZG1iRlpFQzNmdCUyQlFQaFpJekxPdyUyQjRrOElwNGR1WXl1ZXVVd2lWNjRmJTJGVGs0OEVxS0xKMm5uVmlMRmxLSGpUN0ptSDhYVDBtNHo3OEdGMmhxdEtuakVRJTNEJTNE",
    "AMCVS_126E248D54200F960A4C98C6%40AdobeOrg": "1",
    "AMCV_126E248D54200F960A4C98C6%40AdobeOrg": "-1124106680%7CMCIDTS%7C19579%7CvVersion%7C5.2.0%7CMCMID%7C60421270403656023381206296984104228449%7CMCAAMLH-1692201643%7C3%7CMCAAMB-1692201643%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1691604043s%7CNONE",
    "bm_sv": "0974EECC840F14DC6ED4A61A15C0D937~YAAQMh4gF+Mkcs+JAQAAM2UK2xRjQulM9SD1/TfzLmXFVEtwgIK1jbeQAXb9z5YtwcdIwD6k4VARiD9kDwbVMYUHY9BQsPMFHkGKzPeqXNeDVGbaSMGfcRTc0lW7+EvAf3Lqjj8AK72yxJNH+oGSYEHQA0Y/mNgi2C3kPZUdNduyP+Nd7070tlvW1mrHGSGKLOQXd0HYMFKKqrtAS/vO2+2a2Oj16btJf7E9USO4ui0dsUVMu661sUL3DqCq+xtd~1",
    "tfstk": "dbX9YfbEHy4i8qOAhhF33zvOy-q3tOIapNSSnEYiGwQdVguMGZVaGKQPkIGcmdtYHabH1xXDIKev-asM1rJGMqLBCI5MoFYvHi78xz2uEGSw3paur82V8GJ2alWMW8jNbKy03rRgEnLub2WrfAhgyVkV3tK_GDScCkT5dhd9yfYKHxEDXCL5feU7PO5AET3nT40wZfZLvjl21Hrlgzwh.",
    "l": "fBSX2iZmNcXj92ZWBOfwPurza77OSIRAguPzaNbMi9fP9afp5pz1W190jo89C3MNF6r6R38PiVPBBeYBqIv8uzdMX9C7YkkmnRScdTf..",
    "isg": "BDEx7fTg8RMHrV2uJeMdCb-oQL3LHqWQxOdQjhNGLfgXOlGMW261YN9cXNZc8j3I"
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8,zh-CN;q=0.7,zh;q=0.6"
}

params = {
  "ajax": 'true',
  "clickTrackInfo": "a26cbbfe-cb35-4d6a-9867-2a12da62a6e8__4518__2016216850__20__0.098631896__333258__7253__c2i__0.0",
  "from": "hp_categories",
  "isFirstRequest": 'true',
  "item_id": 2016216850,
  "page": 1,
  "params": {
    "catIdLv1": "4402",
    "pvid": "a26cbbfe-cb35-4d6a-9867-2a12da62a6e8",
    "src": "hp_categories",
    "categoryName": "%C4%90i%E1%BB%87n+tho%E1%BA%A1i+di+%C4%91%E1%BB%99ng",
    "categoryId": "4518"
  },
  "q": "Điện thoại di động",
  "spm": "a2o4n.home.categories.4.56053bdcfdziL1",
  "src": "hp_categories",
  "up_id": 2016216850,
  "version": "v2"

}

url = 'https://www.lazada.vn/dien-thoai-di-dong/'
product_data = []
for i in range(0, 2):
    params['page'] = i
    response = requests.get(url, params=params, headers=headers, cookies=cookies)
    data = response.json()
    print(data['templates'])
    for item in data.get('templates').get('mods')['itemlist']:
        item_id = item['itemid']
        item_sold_cnt_show = item['itemSoldCntShow']  
        location = item['location']
        name = item['name']
        nid = item['nid']
        original_price = item['originalPrice']
        price = item['price']
        price_show = item['priceShow']
        rating_score = item['ratingScore']
        review = item['review']

    # In thông tin trích xuất ra màn hình
        print("Item ID:", item_id)
        print("Item Sold Count Show:", item_sold_cnt_show)
        print("Location:", location)
        print("Name:", name)
        print("NID:", nid)
        print("Original Price:", original_price)
        print("Price:", price)
        print("Price Show:", price_show)
        print("Rating Score:", rating_score)
        print("Review:", review)
        print("=" * 50)

# print(product_data)

# df = pd.DataFrame(product_data)
# df.to_csv('product_id1.csv', index= False)