import requests
import pandas as pd
import json
import mysql.connector

db_config = {
    'host': "localhost", 
    'user': "root", 
    'password': "12345",
    'database': 'TEST' 
}

def create_table(connection):
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS order_detail (
            id INT AUTO_INCREMENT PRIMARY KEY,
            item_id BIGINT,
            shop_id INT,
            shop_name VARCHAR(255),
            name VARCHAR(255),
            item_price DECIMAL(16),  
            amount INT,
            description VARCHAR(10000),
            order_id DECIMAL(20),
            status INT
        )
        """
    # cursor.execute(create_table_query)
    # connection.commit()
    cursor.execute(create_table_query)

    # Tạo chỉ mục duy nhất cho cột order_id
    create_index_query = """
        CREATE UNIQUE INDEX index_order_id ON order_detail(order_id)
    """
    cursor.execute(create_index_query)

    connection.commit()

cookies = {
    'REC_T_ID': 'bf6c9083-9b27-11ed-8fce-d26eada8f2db',
    'SPC_F': 'lna25M0dSwvnUpURfx3DsWpAfwgJQcrl',
    '_hjSessionUser_868286': 'eyJpZCI6IjZmOWVkNDQ5LTJhMTMtNTRiNS1iYTdlLWVlYjQ0NDhmZTcxNiIsImNyZWF0ZWQiOjE2NzQ0ODMwNTY5NDIsImV4aXN0aW5nIjp0cnVlfQ==',
    'SPC_CLIENTID': 'bG5hMjVNMGRTd3Zuycnfgietfkhmgyuh',
    '_fbp': 'fb.1.1682933099025.1122736867',
    '_gcl_au': '1.1.2017761758.1690531166',
    '_med': 'affiliates',
    'SC_DFP': 'HZmbYolDSExHjfcFSiqCEONZQqLHVjzn',
    'SPC_ST': '.UENTbkFqUXpQZjdZVE9NbKOBe5oy7DGXLH4E+dAKrJSBM6e6744UHmMtSqrNqcfUIDqZTUtIqeDaICsN5Wwda49BYHnCRniVFfdzXVk/oS/JzkOiUyQ+ecV87+CRz8L7FNC6tqR0WTHQLrtyFpvms6swKXFsg2MaUSADF6waw1cTQVtpqiE7QWdVik/9jw9r8cEgwyIzMc1Othep66i6eA==',
    'SPC_U': '502837064',
    'SPC_R_T_ID': 'cwBVq4oW7xRyCS1OVeul6DcpQATxr0x7KwPzL83y+WMh327czKWTtyj4OexZ1rcwjupPzvQSjj2gaJZmtBSaMxxi1qfSAolbKwkIeKvFZF0sfWdbgIvLq0BYaF1q3lJ6//7lxPAHijtPgC/FHs+QqececXKuzs3fo9Jv4safqr4=',
    'SPC_R_T_IV': 'WDNxREZqSlRWZXNGTWRUWA==',
    'SPC_T_ID': 'cwBVq4oW7xRyCS1OVeul6DcpQATxr0x7KwPzL83y+WMh327czKWTtyj4OexZ1rcwjupPzvQSjj2gaJZmtBSaMxxi1qfSAolbKwkIeKvFZF0sfWdbgIvLq0BYaF1q3lJ6//7lxPAHijtPgC/FHs+QqececXKuzs3fo9Jv4safqr4=',
    'SPC_T_IV': 'WDNxREZqSlRWZXNGTWRUWA==',
    '_gid': 'GA1.2.6627279.1692160471',
    'SPC_SC_TK': '06fc1d2b7dbf573e77737508858ea755',
    'SPC_SC_UD': '502837064',
    'SPC_STK': 'ds8wnx9JG9SX78/EZi9lpBREmQDn65KPN8SFbbF4tYoSKTv/enLyqVLyV9gWZ2FoFfggVwy3R07yWLvSF46Q4txbVhZLvPtQtPjLRs+bO3SkdgyjJWXO6U+rbtatahPINnFib1BdEGP4oVF9cVXU0/uyHbYdsJggxjX23fBaO9lY3k7yKkb10mIEyjfDJaQn',
    'SPC_SI': 'yzXbZAAAAABreHE3ZEF6UXfLEwAAAAAAcmdTYUVsVWg=',
    '_ga_3XVGTY3603': 'GS1.1.1692160470.3.1.1692160483.47.0.0',
    'csrftoken': 'I1xQFYn7pXNQwPfXQ0o0F3YTthKr80RF',
    'SPC_IA': '1',
    '_QPWSDCXHZQA': '0564fe23-26fe-4aea-87f5-f112b10495c9',
    '_hjIncludedInSessionSample_868286': '0',
    '_hjSession_868286': 'eyJpZCI6Ijc3ZTJiY2Y1LTZjZGMtNDJhZS1iYWViLTRmNTk0ZGNmMWY0YSIsImNyZWF0ZWQiOjE2OTIxNzYwNTk0ODksImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'shopee_webUnique_ccd': 'i5EFqfZaXg5%2FfGgF2L9hDg%3D%3D%7CyQCtZfabQv1G58zxV4iDH8WVOlXovTrGDul8eeBcu5ft4bNTZMZ8K8ZAkDafur3CtwRsw9tL%2FS4%3D%7CqRgiX87at70thwJ7%7C08%7C3',
    'ds': '3428f973e60ad61ed826c6e30075e077',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_ga': 'GA1.2.1890700620.1674483057',
    '_dc_gtm_UA-61914164-6': '1',
    '_ga_M32T05RVZT': 'GS1.1.1692176059.110.1.1692176067.52.0.0',
    'SPC_EC': 'TWhESDZqTllIYzZmYnhvZs3jN8ZWnG1mR1D7G74E9oveb7JjhI4UkpqJKo+utYtwG1nzDtMwUk4pvIcPHKVScyDoQOyzs0OdXG3UC82Z87j8yqwhizXG1QqMNa3RNi2k+z7QNIgTgQ6zKlbXg4hmDxM4g1PrdgK06q1Zpme9p/k=',
}

headers = {
    'authority': 'shopee.vn',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'af-ac-enc-sz-token': '',
    'content-type': 'application/json',
    # 'cookie': 'REC_T_ID=bf6c9083-9b27-11ed-8fce-d26eada8f2db; SPC_F=lna25M0dSwvnUpURfx3DsWpAfwgJQcrl; _hjSessionUser_868286=eyJpZCI6IjZmOWVkNDQ5LTJhMTMtNTRiNS1iYTdlLWVlYjQ0NDhmZTcxNiIsImNyZWF0ZWQiOjE2NzQ0ODMwNTY5NDIsImV4aXN0aW5nIjp0cnVlfQ==; SPC_CLIENTID=bG5hMjVNMGRTd3Zuycnfgietfkhmgyuh; _fbp=fb.1.1682933099025.1122736867; _gcl_au=1.1.2017761758.1690531166; _med=affiliates; SC_DFP=HZmbYolDSExHjfcFSiqCEONZQqLHVjzn; SPC_ST=.UENTbkFqUXpQZjdZVE9NbKOBe5oy7DGXLH4E+dAKrJSBM6e6744UHmMtSqrNqcfUIDqZTUtIqeDaICsN5Wwda49BYHnCRniVFfdzXVk/oS/JzkOiUyQ+ecV87+CRz8L7FNC6tqR0WTHQLrtyFpvms6swKXFsg2MaUSADF6waw1cTQVtpqiE7QWdVik/9jw9r8cEgwyIzMc1Othep66i6eA==; SPC_U=502837064; SPC_R_T_ID=cwBVq4oW7xRyCS1OVeul6DcpQATxr0x7KwPzL83y+WMh327czKWTtyj4OexZ1rcwjupPzvQSjj2gaJZmtBSaMxxi1qfSAolbKwkIeKvFZF0sfWdbgIvLq0BYaF1q3lJ6//7lxPAHijtPgC/FHs+QqececXKuzs3fo9Jv4safqr4=; SPC_R_T_IV=WDNxREZqSlRWZXNGTWRUWA==; SPC_T_ID=cwBVq4oW7xRyCS1OVeul6DcpQATxr0x7KwPzL83y+WMh327czKWTtyj4OexZ1rcwjupPzvQSjj2gaJZmtBSaMxxi1qfSAolbKwkIeKvFZF0sfWdbgIvLq0BYaF1q3lJ6//7lxPAHijtPgC/FHs+QqececXKuzs3fo9Jv4safqr4=; SPC_T_IV=WDNxREZqSlRWZXNGTWRUWA==; _gid=GA1.2.6627279.1692160471; SPC_SC_TK=06fc1d2b7dbf573e77737508858ea755; SPC_SC_UD=502837064; SPC_STK=ds8wnx9JG9SX78/EZi9lpBREmQDn65KPN8SFbbF4tYoSKTv/enLyqVLyV9gWZ2FoFfggVwy3R07yWLvSF46Q4txbVhZLvPtQtPjLRs+bO3SkdgyjJWXO6U+rbtatahPINnFib1BdEGP4oVF9cVXU0/uyHbYdsJggxjX23fBaO9lY3k7yKkb10mIEyjfDJaQn; SPC_SI=yzXbZAAAAABreHE3ZEF6UXfLEwAAAAAAcmdTYUVsVWg=; _ga_3XVGTY3603=GS1.1.1692160470.3.1.1692160483.47.0.0; csrftoken=I1xQFYn7pXNQwPfXQ0o0F3YTthKr80RF; SPC_IA=1; _QPWSDCXHZQA=0564fe23-26fe-4aea-87f5-f112b10495c9; _hjIncludedInSessionSample_868286=0; _hjSession_868286=eyJpZCI6Ijc3ZTJiY2Y1LTZjZGMtNDJhZS1iYWViLTRmNTk0ZGNmMWY0YSIsImNyZWF0ZWQiOjE2OTIxNzYwNTk0ODksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; shopee_webUnique_ccd=i5EFqfZaXg5%2FfGgF2L9hDg%3D%3D%7CyQCtZfabQv1G58zxV4iDH8WVOlXovTrGDul8eeBcu5ft4bNTZMZ8K8ZAkDafur3CtwRsw9tL%2FS4%3D%7CqRgiX87at70thwJ7%7C08%7C3; ds=3428f973e60ad61ed826c6e30075e077; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1890700620.1674483057; _dc_gtm_UA-61914164-6=1; _ga_M32T05RVZT=GS1.1.1692176059.110.1.1692176067.52.0.0; SPC_EC=TWhESDZqTllIYzZmYnhvZs3jN8ZWnG1mR1D7G74E9oveb7JjhI4UkpqJKo+utYtwG1nzDtMwUk4pvIcPHKVScyDoQOyzs0OdXG3UC82Z87j8yqwhizXG1QqMNa3RNi2k+z7QNIgTgQ6zKlbXg4hmDxM4g1PrdgK06q1Zpme9p/k=',
    'referer': 'https://shopee.vn/user/purchase/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'x-csrftoken': 'I1xQFYn7pXNQwPfXQ0o0F3YTthKr80RF',
    'x-requested-with': 'XMLHttpRequest',
    'x-shopee-language': 'vi',
    'x-sz-sdk-version': 'unknown',
}

params = {
    'limit': '5',
    'offset': '0',
}

response = requests.get(
    'https://shopee.vn/api/v4/order/get_all_order_and_checkout_list',
    params=params,
    cookies=cookies,
    headers=headers,
)

datas = response.json()

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


def crawl_data(connection, datas):
    details_list = datas.get('data')['order_data']['details_list']
    for i in range(0, 10):
        params['offset'] = i
        for details in details_list:
            status = details['status']
            shipping = details['shipping']
            info_card = details['info_card']
            # product_info = details['product_info']

            order_id = info_card['order_id']

            shop_info = info_card['order_list_cards'][0]['shop_info']
            shop_id = shop_info['shop_id']
            shop_name = shop_info['shop_name']

            parcel_cards = info_card['order_list_cards'][0]['parcel_cards']
            for parcel_card in parcel_cards:
                product_info = parcel_card['product_info']['item_groups'][0]['items'][0]
                item_id = product_info['item_id']
                name = product_info['name']
                item_price = product_info['item_price']/100000
                amount = product_info['amount']
                #description = shipping['tracking_info']['description']
                shop_id = product_info['shop_id']
                status = product_info['status']


                insert_query = """
                    INSERT INTO order_detail (item_id, shop_id, shop_name, name, item_price, amount, order_id, status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                insert_values = (item_id, shop_id, shop_name, name, item_price, amount, order_id, status)

                cursor.execute(insert_query, insert_values)
                connection.commit()

create_table(connection)
crawl_data(connection, datas)              


# df = pd.DataFrame(products)
# df.to_csv('order1.csv', index= False)
# print("Dữ liệu đã được ghi vào tệp order1.csv")