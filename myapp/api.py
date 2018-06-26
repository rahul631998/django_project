import urllib.request
import json
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
    n = 1
    for item in data['data']:
        if item['can_compare'] == True:
            print(str(n) , ". " , item['product_title'], item['product_lowest_price'], "\n")
        else:
            print("Kuch bhi Khojoge!!!")
            break
        if n==5:
            break
        n = n + 1