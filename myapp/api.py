import urllib.request
import json
#   api_key
api = 'mi455rRWCnarKNl3CQyjmfkHJBdLFbPVilB'


def search(image_query):
    #   replacing all the spaces in query with %20
    product = image_query.replace(' ', '%20')
    #   making the url dynamic
    url = 'https://price-api.datayuge.com/api/v1/compare/search?product==' + product
    #   final url
    final_url = url + "&api_key=" + api
    #   reading the json output of the url
    json_obj = urllib.request.urlopen(final_url)
    data = json.load(json_obj)
    n = 1
    for item in data['data']:
        if item['can_compare'] == True:
            print(str(n) , ". " , item['product_title'], item['product_lowest_price'], "\n")
        else:
            print("Kuch bhi Khojoge!!!")
        if n == 5:
            break
        n = n + 1