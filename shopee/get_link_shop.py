import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

params = {
    'category_id': '11036030',
    'limit': '23',
    'offset': '0',
}

def get_urls():
    base_url = 'https://shopee.vn/api/v4/official_shop/get_shops'
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        shops = data['data']['official_shops']
        urls = [f"https://shopee.vn/{shop['username']}" for shop in shops]
        return urls
    else:
        print("Error while fetching data")
        return []

if __name__ == '__main__':
    detail_urls = get_urls()
    for url in detail_urls:
        print(url)
