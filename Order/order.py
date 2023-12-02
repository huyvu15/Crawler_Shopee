import requests
import time
import pandas as pd
import json


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


def read_file(file_path):
    df = pd.read_csv(file_path)
    val1 = df.iloc[:, 0].tolist()
    val2 = df.iloc[:, 1].tolist()
    return zip(val1, val2) 

params = {
    'limit': 15,
    'list_type': 3,
    'offset': 0
}


response = requests.get('https://shopee.vn/api/v4/order/get_order_list', headers=headers, params=params)
reviews = response.json().get('data').get('ratings')


output_reviews = []

for i in range(0, 10):
    params['offset'] = i
    for review in reviews:
        orderid = review.get("orderid")
        itemid = review.get("itemid")
        rating = review.get("rating")
        userid = review.get("userid")
        shopid = review.get("shopid")
        comment = review.get("comment")
        rating_star = review.get("rating_star")
        status = review.get("status")
        
        output_reviews.append({
            "orderid": orderid,
            "itemid": itemid,
            "rating": rating,
            "userid": userid,
            "shopid": shopid,
            "comment": comment,
            "rating_star": rating_star,
            "status": status
        })

output_file = "comment.json"
with open(output_file, "w") as f:
    json.dump(output_reviews, f, indent=4)

print(f"Dữ liệu đã được ghi vào tệp {output_file}")

