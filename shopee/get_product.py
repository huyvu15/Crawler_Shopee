import requests
import time
import pandas as pd
import json

cookies = {
    'REC_T_ID': 'f3304d85-43c9-11ed-a22b-b47af14b5674', 
    'SPC_F': '8svj7SInezqJadZboDBcHT2uA9znUBJR', 
    '_hjSessionUser_868286':'eyJpZCI6IjIzMzBhNWNlLWE3ZDQtNTUxYS1iYzBlLWQxYmQzNWE4OWQ2YSIsImNyZWF0ZWQiOjE2NjQ4NzcwMjEzNTQsImV4aXN0aW5nIjp0cnVlfQ==', 
    'SC_DFP': 'eSmynoZSVafdoFbHSwnChdDsmsNPgzfi', 
    'SPC_U': '-', 
    'SPC_EC':'-', 
    'SPC_T_IV':'SFBIeVpoeVR5aHVOZjRtYg==', 
    'SPC_R_T_ID':'XhNL0KH9Mho6dVyMiLcekmv+tMR0XcIEDSCaTPmsJltCLAtzeJiJNZ4doDvbFEmyt7vHEFeOa01WmouDKc1sB1hQJDaJOKZKujm5XCKjo2xzMdJSVNfXlxNdLpwwmHWSncvCEw22UKsOMA1i10SeFwNbqPNO3vJT7sMG+3r+8Hg=', 
    'SPC_R_T_IV':'SFBIeVpoeVR5aHVOZjRtYg==', 
    'SPC_T_ID':'XhNL0KH9Mho6dVyMiLcekmv+tMR0XcIEDSCaTPmsJltCLAtzeJiJNZ4doDvbFEmyt7vHEFeOa01WmouDKc1sB1hQJDaJOKZKujm5XCKjo2xzMdJSVNfXlxNdLpwwmHWSncvCEw22UKsOMA1i10SeFwNbqPNO3vJT7sMG+3r+8Hg=', 
    '_fbp':'fb.1.1678150441980.1401009225', 
    '_gcl_au':'1.1.332219217.1686153963', 
    '_gcl_aw':'GCL.1688226763.Cj0KCQjwnf-kBhCnARIsAFlg492VF7DZo-1HApWXwLwwtkeZ0aFvXV_TVmBtMesBnI36lRtNFfrsS1AaAlGqEALw_wcB', 
    '_gac_UA-61914164-6':'1.1688226766.Cj0KCQjwnf-kBhCnARIsAFlg492VF7DZo-1HApWXwLwwtkeZ0aFvXV_TVmBtMesBnI36lRtNFfrsS1AaAlGqEALw_wcB', 
    'SPC_SI':'Br7IZAAAAABvdU5QSzhtNzVWHAAAAAAAcUN3SXhQWXU=', 
    '_med':'refer', 
    '_gid':'GA1.2.1226405583.1691090604', 
    '_ga_3XVGTY3603': 'GS1.1.1691091385.1.1.1691091446.60.0.0', 
    'csrftoken': 'keJhGwf0tjCiFPsRDFsBSiXU7qCZpS3s', 
    '_QPWSDCXHZQA':'cf3e4018-a2bd-4ce1-947f-06a951c70e48', 
    '_hjSession_868286':'eyJpZCI6ImYzNDU0YjMxLWY4MzYtNGNhMC04YWUzLWJlZDRhMmVmNzc2ZCIsImNyZWF0ZWQiOjE2OTExMTc2MDg0MDUsImluU2FtcGxlIjpmYWxzZX0=', 
    '_hjAbsoluteSessionInProgress':'0', 
    'AMP_TOKEN':'%24NOT_FOUND', 
    'shopee_webUnique_ccd':'PwgcZnXduFnxsGI1ffKCyA%3D%3D%7C5kRubrum0Oj%2FDMmB7tMABHzucFa0%2Bj933nG6Yju8Zal9kD9F%2BXFdji%2Fn65FqQst02SSildCJQhM%3D%7CRppsXpgMiWuzapDU%7C08%7C3', 
    'ds':'6c0e8e889a2dd46ef62ff797a3ad0d3c', 
    '_ga':'GA1.1.462356251.1678150443', 
    '_hjIncludedInSessionSample_868286':'0', 
    '_ga_M32T05RVZT':'GS1.1.1691117608.14.1.1691118937.60.0.0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, /',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Referer': 'https://shopee.vn/Nh%C3%A0-C%E1%BB%ADa-%C4%90%E1%BB%9Di-S%E1%BB%91ng-cat.11036670',
    'X-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'X-Api-Source':'pc',
    'Z=Requested-With':'XMLHttpRequest',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
    'X-Shopee-Language':'vi',
    'X-Csrftoken':'keJhGwf0tjCiFPsRDFsBSiXU7qCZpS3s',
    'X-Sz-Sdk-Version':'2.9.2-2&1.4.1',
    'X-Sap-Ri':'b9afcc64ae2254c798a1ad3c38b4253d2bcdc80e4a4a8a99',
}

params = {
    'shop_id':22018518,
    'item_id': 2115755495,
    'limit':8,
    'offset':0,
    #('include', 'tag,images,gallery,promotions,badges,stock_item,variants,product_links,discount_tag,ranks,breadcrumbs,top_features,cta_desktop'),
}
def read_file(file_path):
    df = pd.read_csv(file_path)
    val1 = df.iloc[:, 0].tolist()
    val2 = df.iloc[:, 1].tolist()
    return zip(val1, val2)  # Return pairs of values


def comment_parser(json):
    d = dict()
    json = json.get('data')
    d['itemid'] = json.get('itemid')
    d['shopid'] = json.get('shopid')
    return d

product_data = []
dem = 0
for i, j in read_file('product_id1.csv'):
    params['shop_id'] = j
    params['item_id'] = i
    response = requests.get(f'https://shopee.vn/api/v4/pdp/get_pc?shop_id={j}&item_id={i}', headers=headers, params=params,cookies=cookies)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(data) 
    else:
        print(response.json())
    dem +=1
    if dem == 5:
        break
print(product_data)
df = pd.DataFrame(product_data)
df.to_csv('product_data.csv', index=False)

