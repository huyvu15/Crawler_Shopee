import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

params = {
    'category_id': '11036030',
    'limit': '23',
    'offset': '0',
}

def get_shops_data():
    base_url = 'https://shopee.vn/api/v4/official_shop/get_shops'
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        shops = data['data']['official_shops']
        return shops
    else:
        print("Error while fetching data")
        return []

def extract_shop_info(shop):
    shop_info = {
        "userid": shop["userid"],
        "username": shop["username"],
        "shopid": shop["shopid"],
        "shop_name": shop["shop_name"],
        "shop_link": f"https://shopee.vn/{shop['username']}"
    }
    return shop_info

if __name__ == '__main__':
    shops_data = get_shops_data()
    print(type(shops_data))
    # extracted_data = [extract_shop_info(shop) for shop in shops_data]
    # # print(extracted_data)
    
    # df = pd.DataFrame(extracted_data)
    # df.to_csv("shopee_shops.csv", index=False)
    
    # print("Data saved to shopee_shops.csv")



