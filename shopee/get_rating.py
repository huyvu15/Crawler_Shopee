import requests
import time
import pandas as pd
import json


cookies= {
    "REC_T_ID": "bf6c9083-9b27-11ed-8fce-d26eada8f2db",
    "SPC_F": "lna25M0dSwvnUpURfx3DsWpAfwgJQcrl",
    "_hjSessionUser_868286": "eyJpZCI6IjZmOWVkNDQ5LTJhMTMtNTRiNS1iYTdlLWVlYjQ0NDhmZTcxNiIsImNyZWF0ZWQiOjE2NzQ0ODMwNTY5NDIsImV4aXN0aW5nIjp0cnVlfQ==",
    "SPC_CLIENTID": "bG5hMjVNMGRTd3Zuycnfgietfkhmgyuh",
    "_fbp": "fb.1.1682933099025.1122736867",
    "_gcl_au": "1.1.2017761758.1690531166",
    "SPC_SI": "IsHIZAAAAABYcFZHUUMwSWLXFwAAAAAAREdUR2d5cUI=",
    "_med": "affiliates",
    "csrftoken": "5rkFyxI5wVfLvIIl7plbkemfJQChn86n",
    "_gid": "GA1.2.1738251725.1691478376",
    "SPC_SC_SA_TK": "",
    "SPC_SC_SA_UD": "",
    "SPC_SC_TK": "fb692dbeae11e5d7ff80abdc02db5770",
    "SPC_SC_UD": "705109936",
    "SPC_U": "705109936",
    "SPC_STK": "hOz3sM2Aff3RWlz1XSoTp09Nbp3JDvj4esdj/g+81XVO2gW8U8H/vyPA/IIltltLXpRu4fxYdxP6mq8OC0r4Ietj0XAs9ttkkPcVtyOMiozSGcOrqx+K8ljuX4vumJMkGTAAn68vtsiNTXPmelIcqJbdqWgd0ry8keHQPKR4oNk=",
    "SC_DFP": "HZmbYolDSExHjfcFSiqCEONZQqLHVjzn",
    "SPC_ST": ".Z01iajZuVTVKNGhQVXVOcnaQzmF9uWWjm0cvZF4HhiSCN3OqlBwAe30SOIR7u29XaDXHkhi0E5KrXkdt6NvgVhlJWV7ggJsxvRfqnVYCiczQKlt37F8eBhhF0+uXsv57RPsFZXHyenp9qw0gFNMWFUiw7QtRiUw5yeyCeQKG6ig9Fh2zgC6UaVOkAy3OmBJGWN9iz+1mdyY2foktL2nxWQ==",
    "SPC_T_ID": "sT2q4gFR7Gfynxgi6k14PVtdKwxkPKNQhV48mqjwuiuexMiaPFfP4a55c+c6RdSklXGjUP1pj7+L1rCOE9wdToRuueRerwjJWoFAcCt8JKnaJ6Uihltbn6hDxgN26aocBJfZWPqjyMxAjT3XMRtdDJMONQo172M7hfbor+spovE=",
    "SPC_T_IV": "eUNWUzl4UlB4QVRqWlNHcw==",
    "SPC_R_T_ID": "sT2q4gFR7Gfynxgi6k14PVtdKwxkPKNQhV48mqjwuiuexMiaPFfP4a55c+c6RdSklXGjUP1pj7+L1rCOE9wdToRuueRerwjJWoFAcCt8JKnaJ6Uihltbn6hDxgN26aocBJfZWPqjyMxAjT3XMRtdDJMONQo172M7hfbor+spovE=",
    "SPC_R_T_IV": "eUNWUzl4UlB4QVRqWlNHcw==",
    "_ga_3XVGTY3603": "GS1.1.1691484579.2.0.1691484580.59.0.0",
    "_QPWSDCXHZQA": "0564fe23-26fe-4aea-87f5-f112b10495c9",
    "AMP_TOKEN": "$NOT_FOUND",
    "_hjIncludedInSessionSample_868286": "0",
    "_hjSession_868286": "eyJpZCI6IjFiYTgwYzM0LTJlZWItNGZjYy1iZDhiLWUwYzFjZWQ3ZGIzYiIsImNyZWF0ZWQiOjE2OTE1NzMyNzI4OTcsImluU2FtcGxlIjpmYWxzZX0=",
    "_hjAbsoluteSessionInProgress": "0",
    "_ga_M32T05RVZT": "GS1.1.1691573268.86.1.1691573951.60.0.0",
    "_ga": "GA1.1.1890700620.1674483057",
    "_dc_gtm_UA-61914164-6": "1",
    "shopee_webUnique_ccd": "Y6yTZQLznyDjIuLe0LUiUQ%3D%3D%7C9EhyAJrWI1YcVuPKbgOIZ9zKtD38g5uPpufoVIZ6So3bbwJVylcOX%2BI1VK6k0QnRBe2P9ZuTUYzP%2Bg%3D%3D%7CwzKAXkJk486P46eC%7C08%7C3",
    "ds": "82d3c928e3e6da889eeba3c6b82532c0",
    "SPC_EC": "dGsxZVY0YW9QVXV1NkpQRS8+k5OvrEaENpJbLYRrQBvjHZZTOIaHCZcLRT9/nT6XOf6O0ckogrivuQwDIiqkUw/zAoJiDvWoVUy8kFm/ExLcLbl1cXbWnxXN6NaK6Vb2AuFc//Jo6k4GTozlnW3fI7QhuSVy7pnxkOO4FT29Jhw="
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8,zh-CN;q=0.7,zh;q=0.6"
}

def read_file(file_path):
    df = pd.read_csv(file_path)
    val1 = df.iloc[:, 0].tolist()
    val2 = df.iloc[:, 1].tolist()
    return zip(val1, val2) 

params = {

  "exclude_filter": 0,
  "filter": 0,
  "filter_size": 0,
  "flag": 1,
  "fold_filter": 0,
  "itemid": 21629119012,
  "limit": 6,
  "offset": 0,
  "relevant_reviews": 'false',
  "request_source": 1,
  "shopid": 81075907,
  "tag_filter": "",
  "type": 0,
  "variation_filters": 'null'
}

response = requests.get('https://shopee.vn/api/v2/item/get_ratings', headers=headers, params=params)
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

