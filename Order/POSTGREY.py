import requests
from bs4 import BeautifulSoup
import psycopg2
import json
import time
    
cookies = {
    'REC_T_ID': 'bf6c9083-9b27-11ed-8fce-d26eada8f2db',
    'SPC_F': 'lna25M0dSwvnUpURfx3DsWpAfwgJQcrl',
    '_hjSessionUser_868286': 'eyJpZCI6IjZmOWVkNDQ5LTJhMTMtNTRiNS1iYTdlLWVlYjQ0NDhmZTcxNiIsImNyZWF0ZWQiOjE2NzQ0ODMwNTY5NDIsImV4aXN0aW5nIjp0cnVlfQ==',
    'SPC_CLIENTID': 'bG5hMjVNMGRTd3Zuycnfgietfkhmgyuh',
    '_fbp': 'fb.1.1682933099025.1122736867',
    '_gcl_au': '1.1.2017761758.1690531166',
    'SPC_SI': 'IsHIZAAAAABYcFZHUUMwSWLXFwAAAAAAREdUR2d5cUI=',
    '_med': 'affiliates',
    'csrftoken': '5rkFyxI5wVfLvIIl7plbkemfJQChn86n',
    '_gid': 'GA1.2.1738251725.1691478376',
    'SPC_SC_SA_TK': '',
    'SPC_SC_SA_UD': '',
    'SPC_SC_TK': 'fb692dbeae11e5d7ff80abdc02db5770',
    'SPC_SC_UD': '705109936',
    'SPC_STK': 'hOz3sM2Aff3RWlz1XSoTp09Nbp3JDvj4esdj/g+81XVO2gW8U8H/vyPA/IIltltLXpRu4fxYdxP6mq8OC0r4Ietj0XAs9ttkkPcVtyOMiozSGcOrqx+K8ljuX4vumJMkGTAAn68vtsiNTXPmelIcqJbdqWgd0ry8keHQPKR4oNk=',
    'SC_DFP': 'HZmbYolDSExHjfcFSiqCEONZQqLHVjzn',
    '_ga_3XVGTY3603': 'GS1.1.1691484579.2.0.1691484580.59.0.0',
    '_QPWSDCXHZQA': '0564fe23-26fe-4aea-87f5-f112b10495c9',
    'AMP_TOKEN': '%24NOT_FOUND',
    'SPC_ST': '.dGtZd0ZhSFBBekVIeE0xVOrGpK9LZU7JooCfgw/NoVDXOUOSocAJWGWHrmeus1ycY5TRCeMi9RHmXet07LroYQQenQ2EZlpNq9Towv8WbbnrC2DrFMz/3TsKuv7iPzEYUhoBRoXC6izZ+j5Kxl2cpVaYFV8SxABQ7uctWBi3gI84+eTQnMmgY6l0O+Z9UYsR88CRwAkb9tyIV/HnXNTS+A==',
    'SPC_U': '392197148',
    'SPC_R_T_ID': 'kC+DIDhYU9nr9xKaAwfgGLEQzP4Qb/bCbDnQU976gWD6zM84esGP2aEctQB6AhWIqZl9KvceBe7ndl1qumEt5Id9sL+nfZs4SdIsCTLGzjLXtugQQzKil9lVL/2znaE/dKp+rB24nyjmwHPAc+IRVoUQiffdpRTFCaJ5of4RyQI=',
    'SPC_R_T_IV': 'T29RQXZ4Nk51SnM3bmU1cA==',
    'SPC_T_ID': 'kC+DIDhYU9nr9xKaAwfgGLEQzP4Qb/bCbDnQU976gWD6zM84esGP2aEctQB6AhWIqZl9KvceBe7ndl1qumEt5Id9sL+nfZs4SdIsCTLGzjLXtugQQzKil9lVL/2znaE/dKp+rB24nyjmwHPAc+IRVoUQiffdpRTFCaJ5of4RyQI=',
    'SPC_T_IV': 'T29RQXZ4Nk51SnM3bmU1cA==',
    'SPC_IA': '1',
    '_ga': 'GA1.1.1890700620.1674483057',
    'shopee_webUnique_ccd': 'trZPQ36ePm%2B2WOQ7hpN5kg%3D%3D%7CF0hyAJrWI1YcVuPKbgOIZ9zKtD38g5uPpufoVNtakYnbbwJVylcOX%2BI1VK6k0QnRBe2P9ZuTUYzP%2Bg%3D%3D%7CwzKAXkJk486P46eC%7C08%7C3',
    'ds': 'e9c1d4d5e0d6361a5dfbdc18f7a1db9d',
    '_ga_M32T05RVZT': 'GS1.1.1691639125.92.0.1691639125.60.0.0',
    'SPC_EC': 'SE9KQUVDelduS3F6MHBEYuG5vh7HLILZE9yZyo7RsO1MXVGy3uq26ZMSsZYAXfJS2T47RCYy9xPbm6yCvOMiO2GPYtLfJ/lax/N2MCXD2cQVQwCs+EFLCTRofKIpaJTShwXIo/91/0xxAs/PopjvSDi+pLCI9y6vnIk6vuto1Os' 
}

headers = {
    'Referer': 'https://shopee.vn/user/purchase/?type=3',
    'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Api-Source': 'pc',
    'X-Csrftoken': '5rkFyxI5wVfLvIIl7plbkemfJQChn86n',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Shopee-Language': 'vi',
    'X-Sz-Sdk-Version': 'unknown'
}

params = {
    'limit': 6,
    'list_type': 3,
    'offset': 0
}
def crawl_data():
    response = requests.get('https://shopee.vn/api/v4/order/get_order_list?limit=5&list_type=3&offset=0', headers=headers, params=params, cookies = cookies)

    datas = response.json()

    products = []
    details_list = datas['data']['details_list']
    for i in range(0, 10):
        params['offset'] = i
        for details in details_list:
            status = details['status']
            shipping = details['shipping']
            info_card = details['info_card']
            #product_info = details['product_info']

            order_id = info_card['order_id']

            shop_info = info_card['order_list_cards'][0]['shop_info']
            shop_id = shop_info['shop_id']
            shop_name = shop_info['shop_name']

            parcel_cards = info_card['order_list_cards'][0]['parcel_cards']
            for parcel_card in parcel_cards:
                product_info = parcel_card['product_info']['item_groups'][0]['items'][0]
                item_id = product_info['item_id']
                name = product_info['name']
                item_price = product_info['item_price']
                amount = product_info['amount']
                description = shipping['tracking_info']['description']
                shop_id = product_info['shop_id']
                status = product_info['status']

                print(f"Item ID: {item_id}")
                print(f"Shop ID: {shop_id}")
                print(f"Name: {name}")
                print(f"Item Price: {item_price}")
                print(f"Amount: {amount}")
                print(f"Description: {description}")
                print(f"Shop Name: {shop_name}")
                print(f"Order ID: {order_id}")
                print(f"Status: {status}")
                print("---"*10)
                products.append({
                    'item_id':item_id,
                    'shop_id':shop_id,
                    'shop_name':shop_name,
                    'name':name,
                    'item_price':item_price,
                    'amount':amount,
                    'order_id':order_id,
                    'status':status
                })
    return products


def create_movie_db(connection, table_name, data_field): # data_field đang là 1 list
    cursor = connection.cursor()
    
    list_str_field_name_and_field_type = [f"{field[0]} {field[1]}" for field in data_field]
    # kết quả thu đc sau dòng này là field_name và data type
    # thêm tất cả thông tin vào bảng
    result_field = ','.join(list_str_field_name_and_field_type) # từng  phẩn tử đc ngăn cách bởi dấu,
    
    create_sql = f"""
    create table if not exists {table_name} (
        {result_field}
    );
    
    """
    cursor.execute(create_sql)
    connection.commit()
    
table_name = "Order_details"

def insert_db(connection, table_name, data_field, list_data):
    cursor = connection.cursor()
    list_str_field_name = [f"{field[0]}" for field in data_field]
    #item_id,shop_id,shop_name,name,item_price,amount,order_id,status
    data_insert = [f"({item_id}, {shop_id}, '{shop_name}', '{name}', {item_price}, {amount}, {order_id}, '{status}')" for idx, (item_id, shop_id, shop_name, name, item_price, amount, order_id, status) in enumerate(list_data)]
    
    result_field = ','.join(list_str_field_name) # từng  phẩn tử đc ngăn cách bởi dấu,
    result_data = ','.join(data_insert) # từng  phẩn tử đc ngăn cách bởi dấu,
    
    insert_sql = f"""
    insert into {table_name} ({result_field})
    values
        {result_data};
    """
    cursor.execute(insert_sql)
    connection.commit()

data_field = [
    ("item_id", "integer"),
    ("shop_id", "integer"),
    ("shop_name", "varchar"),
    ("name", "varchar"),
    ("item_price", "interger"),
    ("amount", "integer"),
    ("order_id", "integer"),
    ("status", "status")
]
movies_info = crawl_data()
insert_db(connection,table_name,data_field, movies_info)
connection.close()