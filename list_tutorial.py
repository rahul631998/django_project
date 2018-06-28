# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 22:51:09 2018

@author: Rahul Chaudhary
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:56:22 2018
@author: Rahul
"""

import urllib.request
import json
import requests

#   api_key
api = 'mi455rRWCnarKNl3CQyjmfkHJBdLFbPVilB'


def search(image_query, min_range, max_range):
    #   replacing all the spaces in query with %20
    product = image_query.replace(' ', '%20')
    #   making the url dynamic  //remember to add brand later using &product=Iphone&filter=brand%3Aapple&price_start
    url = 'https://price-api.datayuge.com/api/v1/compare/search?api_key=' + api + '&product=' + product + '&price_start=' + min_range + '&price_end=' + max_range
    #   reading the json output of the url
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
    n = 0
    list = [[]]*5
    for item in data['data']:
        if item['can_compare'] == True:
            list[n] = [item['product_title'],item['product_image'], item['product_lowest_price']]

            urlforlink = "https://price-api.datayuge.com/api/v1/compare/detail?api_key=" + api + "&id=" + item[
                "product_id"]
            newjson_obj = urllib.request.urlopen(urlforlink)
            newdata = json.load(newjson_obj)
            i = 0
            for newitem in newdata["data"]["stores"]:
                store = ["amazon", "flipkart", "snapdeal", "ebay", "paytm", "croma", "yebhi", "indiatimes",
                         "homeshop18", "naaptol", "infibeam", "tatacliq", "shopclues"]
                if type(newitem[store[i]]) is dict:
                    list[n].append(newitem[store[i]]["product_store_url"])
                    break
                else:
                    i = i + 1
                    if i==13:
                        print("item", n, "not found")
                        break

        else:
            print("Kuch bhi Khojoge!!!")
            break
        if n == 4:
            break
        n = n + 1
    return list
list = search("mobile", "50000", "100000")

for x in range(len(list)):
    for y in range(len(list[x])):
        print(list[x][y])
        
print(list[1][2])