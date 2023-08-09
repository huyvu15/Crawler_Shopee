import requests
import csv
import pandas as pd

cookies = {
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
    "_hjAbsoluteSessionInProgress": "0",
    "_hjIncludedInSessionSample_868286": "0",
    "_hjSession_868286": "eyJpZCI6IjI5ZGE0ZGYxLTVmNmUtNGMyYy04M2NiLTI3YjllNGZmNzY4NiIsImNyZWF0ZWQiOjE2OTE1MjUxNjcwMjMsImluU2FtcGxlIjpmYWxzZX0=",
    "AMP_TOKEN": "$NOT_FOUND",
    "_ga": "GA1.2.1890700620.1674483057",
    "_dc_gtm_UA-61914164-6": "1",
    "shopee_webUnique_ccd": "paGCFL8017QjLuZUvgFKGA%3D%3D%7CzEhyAJrWI1YcVuPKbgOIZ9zKtD38g5uPpufoVDfgIYLbbwJVylcOX%2BI1VK6k0QnRBe2P9ZuTUYw%3D%7CwzKAXkJk486P46eC%7C08%7C3",
    "ds": "67378dbfb042e82bb458b44d64c4eadc",
    "_ga_M32T05RVZT": "GS1.1.1691525164.83.1.1691525176.48.0.0",
    "SPC_EC": "eEV4ZEVSbnpQZnc4aVdaMQETg52wBm0cdNnQM3Jtq1sj9JzN4QlWGEzoy5OR",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

params = {
    "bundle": "category_landing_page",
    "cat_level": 1,
    "catid": 11035567,
    "limit": 60,
    "offset": 0,
}

url = 'https://shopee.vn/api/v4/recommend/recommend'
product_data = []
for i in range(0, 5):
    params['offset'] = i
    response = requests.get(url, params=params, headers=headers, cookies=cookies)
    n = response.json().get('data').get('sections')[0].get('data').get('item')
    for record in n:
        # product_id.append({'id':record['itemid']}, {'idshop':record['shopid']})
        product_data.append({'itemid': record['itemid'], 'shopid': record['shopid']})

print(product_data)

df = pd.DataFrame(product_data)
df.to_csv('product_id1.csv', index= False)