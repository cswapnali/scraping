import requests
import json
import sys
sys.stdout.reconfigure(encoding='UTF-8')
import pymysql.cursors

connection = pymysql.connect(host = 'localhost', 
                       user = 'root', 
                       password = 'mysql123',
                       cursorclass=pymysql.cursors.DictCursor)

cookies = {
    '__SW': 'HmiUJ_5o5infUwGxsBoU9VLPI1YZQcMu',
    '_device_id': '101e8257-d0b3-4b0c-52cf-05e846034560',
    'order_source': 'Google-Sok',
    'order_medium': 'CPC',
    'order_campaign': 'google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v1_v2_brand_em',
    '_gcl_au': '1.1.1532265239.1673274583',
    'fontsLoaded': '1',
    '_gid': 'GA1.2.753156182.1673274584',
    'WZRK_G': 'f93553ef09154cb98a85814f2e0534d3',
    '_session_tid': '1e3387fb07e7198b60df8ee47f512a5bbfab66429075228703b75283630704f227980b25c9c9b8ffda0c8f50efe570ded0cdfbef82c0c8a6ad741d4de1b4c8922cacca2cf6935992f64081f5ea753890c4911c384688314886975df8248e93d73b1c438e683a9c5404172b670cd05c62',
    '_gcl_aw': 'GCL.1673376911.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB',
    '_gac_0': '1.1673376912.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB',
    'dadl': 'true',
    'userLocation': '{%22address%22:%2232%2C%20JijaMata%20Colony%2C%20Industrial%20Area%2C%20Kalyan%2C%20Maharashtra%20421004%2C%20India%22%2C%22area%22:%22Industrial%20Area%22%2C%22id%22:%22335775159%22%2C%22lat%22:%2219.2403305%22%2C%22lng%22:%2273.1305395%22}',
    '_is_logged_in': '1',
    '_sid': '4taf8c75-6c58-40ce-adcf-aa1025b19e63',
    '_ga': 'GA1.1.626327621.1673274584',
    '_ga_34JYJ0BCRN': 'GS1.1.1673632615.18.1.1673632707.0.0.0',
    'WZRK_S_W86-ZZK-WR6Z': '%7B%22p%22%3A1%2C%22s%22%3A1673632616%2C%22t%22%3A1673632751%7D',
}

headers = {
    'authority': 'www.swiggy.com',
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    # 'cookie': '__SW=HmiUJ_5o5infUwGxsBoU9VLPI1YZQcMu; _device_id=101e8257-d0b3-4b0c-52cf-05e846034560; order_source=Google-Sok; order_medium=CPC; order_campaign=google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v1_v2_brand_em; _gcl_au=1.1.1532265239.1673274583; fontsLoaded=1; _gid=GA1.2.753156182.1673274584; WZRK_G=f93553ef09154cb98a85814f2e0534d3; _session_tid=1e3387fb07e7198b60df8ee47f512a5bbfab66429075228703b75283630704f227980b25c9c9b8ffda0c8f50efe570ded0cdfbef82c0c8a6ad741d4de1b4c8922cacca2cf6935992f64081f5ea753890c4911c384688314886975df8248e93d73b1c438e683a9c5404172b670cd05c62; _gcl_aw=GCL.1673376911.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB; _gac_0=1.1673376912.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB; dadl=true; userLocation={%22address%22:%2232%2C%20JijaMata%20Colony%2C%20Industrial%20Area%2C%20Kalyan%2C%20Maharashtra%20421004%2C%20India%22%2C%22area%22:%22Industrial%20Area%22%2C%22id%22:%22335775159%22%2C%22lat%22:%2219.2403305%22%2C%22lng%22:%2273.1305395%22}; _is_logged_in=1; _sid=4taf8c75-6c58-40ce-adcf-aa1025b19e63; _ga=GA1.1.626327621.1673274584; _ga_34JYJ0BCRN=GS1.1.1673632615.18.1.1673632707.0.0.0; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A1%2C%22s%22%3A1673632616%2C%22t%22%3A1673632751%7D',
    'if-none-match': 'W/"9a34-h6Rwh23X8kBOJZcFkKJXNIRmUEo"',
    'referer': 'https://www.swiggy.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

params = {
    'lat': '19.2403305',
    'lng': '73.1305395',
    'offset': '0',
    'sortBy': 'RELEVANCE',
    'pageType': 'SEE_ALL',
    'page_type': 'DESKTOP_SEE_ALL_LISTING',
}

response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', params=params, cookies=cookies, headers=headers)
response = response.text
data = json.loads(response)
offset = data['data']['totalSize']
offset = offset//16

off=0
for i in range(offset):
    cookies = {
    '__SW': 'HmiUJ_5o5infUwGxsBoU9VLPI1YZQcMu',
    '_device_id': '101e8257-d0b3-4b0c-52cf-05e846034560',
    'order_source': 'Google-Sok',
    'order_medium': 'CPC',
    'order_campaign': 'google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v1_v2_brand_em',
    '_gcl_au': '1.1.1532265239.1673274583',
    'fontsLoaded': '1',
    '_gid': 'GA1.2.753156182.1673274584',
    'WZRK_G': 'f93553ef09154cb98a85814f2e0534d3',
    '_session_tid': '1e3387fb07e7198b60df8ee47f512a5bbfab66429075228703b75283630704f227980b25c9c9b8ffda0c8f50efe570ded0cdfbef82c0c8a6ad741d4de1b4c8922cacca2cf6935992f64081f5ea753890c4911c384688314886975df8248e93d73b1c438e683a9c5404172b670cd05c62',
    '_gcl_aw': 'GCL.1673376911.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB',
    '_gac_0': '1.1673376912.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB',
    'dadl': 'true',
    'userLocation': '{%22address%22:%2232%2C%20JijaMata%20Colony%2C%20Industrial%20Area%2C%20Kalyan%2C%20Maharashtra%20421004%2C%20India%22%2C%22area%22:%22Industrial%20Area%22%2C%22id%22:%22335775159%22%2C%22lat%22:%2219.2403305%22%2C%22lng%22:%2273.1305395%22}',
    '_is_logged_in': '1',
    '_sid': '4taf8c75-6c58-40ce-adcf-aa1025b19e63',
    '_ga': 'GA1.1.626327621.1673274584',
    '_ga_34JYJ0BCRN': 'GS1.1.1673632615.18.1.1673632707.0.0.0',
    'WZRK_S_W86-ZZK-WR6Z': '%7B%22p%22%3A1%2C%22s%22%3A1673632616%2C%22t%22%3A1673632751%7D',
    }
    
    headers = {
    'authority': 'www.swiggy.com',
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    # 'cookie': '__SW=HmiUJ_5o5infUwGxsBoU9VLPI1YZQcMu; _device_id=101e8257-d0b3-4b0c-52cf-05e846034560; order_source=Google-Sok; order_medium=CPC; order_campaign=google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v1_v2_brand_em; _gcl_au=1.1.1532265239.1673274583; fontsLoaded=1; _gid=GA1.2.753156182.1673274584; WZRK_G=f93553ef09154cb98a85814f2e0534d3; _session_tid=1e3387fb07e7198b60df8ee47f512a5bbfab66429075228703b75283630704f227980b25c9c9b8ffda0c8f50efe570ded0cdfbef82c0c8a6ad741d4de1b4c8922cacca2cf6935992f64081f5ea753890c4911c384688314886975df8248e93d73b1c438e683a9c5404172b670cd05c62; _gcl_aw=GCL.1673376911.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB; _gac_0=1.1673376912.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB; dadl=true; userLocation={%22address%22:%2232%2C%20JijaMata%20Colony%2C%20Industrial%20Area%2C%20Kalyan%2C%20Maharashtra%20421004%2C%20India%22%2C%22area%22:%22Industrial%20Area%22%2C%22id%22:%22335775159%22%2C%22lat%22:%2219.2403305%22%2C%22lng%22:%2273.1305395%22}; _is_logged_in=1; _sid=4taf8c75-6c58-40ce-adcf-aa1025b19e63; _ga=GA1.1.626327621.1673274584; _ga_34JYJ0BCRN=GS1.1.1673632615.18.1.1673632707.0.0.0; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A1%2C%22s%22%3A1673632616%2C%22t%22%3A1673632751%7D',
    'if-none-match': 'W/"9a34-h6Rwh23X8kBOJZcFkKJXNIRmUEo"',
    'referer': 'https://www.swiggy.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    
    params = {
    'lat': '19.2403305',
    'lng': '73.1305395',
    'offset': off,
    'sortBy': 'RELEVANCE',
    'pageType': 'SEE_ALL',
    'page_type': 'DESKTOP_SEE_ALL_LISTING',
    }
    
    response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', params=params, cookies=cookies, headers=headers)
    response = response.text
    off = off + 16
    data1 = json.loads(response)
    data1 = data1['data']['cards']
    #print(len(data1))
    
    rest_Id = []
    rest_name = []
    rest_area = []
    rest_timing = []
    rest_distance = []
    rest_discount = []
    rest_ratings = []
    item_Id = []
    item_name = []
    item_price = []
    res_name = []
    res_id = []
    
    #Scraping restaurant details
    for i in range(len(data1)):
        Id = data1[i]['data']['data']['id']
        rest_Id.append(Id)
        name = data1[i]['data']['data']['name']
        rest_name.append(name)
        area = data1[i]['data']['data']['area']
        rest_area.append(area)
        timing = data1[i]['data']['data']['deliveryTime']
        rest_timing.append(timing)
        distance = data1[i]['data']['data']['lastMileTravel']
        distance = round(distance)
        rest_distance.append(distance)
        discount = data1[i]['data']['data']['aggregatedDiscountInfoV2']['header']
        rest_discount.append(discount)
        ratings = data1[i]['data']['data']['avgRating']
        rest_ratings.append(ratings)
        #print(Id)    
        #print(Id+' '+name+' '+area+' '+str(timing)+' '+str(distance)+' '+discount+' '+str(ratings))   
        
        cookies = {
            '__SW': 'HmiUJ_5o5infUwGxsBoU9VLPI1YZQcMu',
            '_device_id': '101e8257-d0b3-4b0c-52cf-05e846034560',
            'order_source': 'Google-Sok',
            'order_medium': 'CPC',
            'order_campaign': 'google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v1_v2_brand_em',
            '_gcl_au': '1.1.1532265239.1673274583',
            'fontsLoaded': '1',
            '_gid': 'GA1.2.753156182.1673274584',
            'WZRK_G': 'f93553ef09154cb98a85814f2e0534d3',
            '_session_tid': '1e3387fb07e7198b60df8ee47f512a5bbfab66429075228703b75283630704f227980b25c9c9b8ffda0c8f50efe570ded0cdfbef82c0c8a6ad741d4de1b4c8922cacca2cf6935992f64081f5ea753890c4911c384688314886975df8248e93d73b1c438e683a9c5404172b670cd05c62',
            'dadl': 'true',
            'userLocation': '{%22address%22:%2232%2C%20JijaMata%20Colony%2C%20Industrial%20Area%2C%20Kalyan%2C%20Maharashtra%20421004%2C%20India%22%2C%22area%22:%22Industrial%20Area%22%2C%22deliveryLocation%22:%22JijaMata%20Colony%2C%20Industrial%20Area%22%2C%22lat%22:19.2403305%2C%22lng%22:73.1305395}',
            '_gcl_aw': 'GCL.1673376911.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB',
            '_gac_0': '1.1673376912.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB',
            '_is_logged_in': '1',
            '_sid': '4roc2de7-8141-413b-870c-b62b7a0b3a98',
            '_gat_0': '1',
            'WZRK_S_W86-ZZK-WR6Z': '%7B%22p%22%3A13%2C%22s%22%3A1673419643%2C%22t%22%3A1673420476%7D',
            '_ga': 'GA1.2.626327621.1673274584',
            '_gat_UA-53591212-4': '1',
            '_ga_34JYJ0BCRN': 'GS1.1.1673419655.7.1.1673420492.0.0.0',
        }
        headers = {
            'authority': 'www.swiggy.com',
            '__fetch_req__': 'true',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            # 'cookie': '__SW=HmiUJ_5o5infUwGxsBoU9VLPI1YZQcMu; _device_id=101e8257-d0b3-4b0c-52cf-05e846034560; order_source=Google-Sok; order_medium=CPC; order_campaign=google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v1_v2_brand_em; _gcl_au=1.1.1532265239.1673274583; fontsLoaded=1; _gid=GA1.2.753156182.1673274584; WZRK_G=f93553ef09154cb98a85814f2e0534d3; _session_tid=1e3387fb07e7198b60df8ee47f512a5bbfab66429075228703b75283630704f227980b25c9c9b8ffda0c8f50efe570ded0cdfbef82c0c8a6ad741d4de1b4c8922cacca2cf6935992f64081f5ea753890c4911c384688314886975df8248e93d73b1c438e683a9c5404172b670cd05c62; dadl=true; userLocation={%22address%22:%2232%2C%20JijaMata%20Colony%2C%20Industrial%20Area%2C%20Kalyan%2C%20Maharashtra%20421004%2C%20India%22%2C%22area%22:%22Industrial%20Area%22%2C%22deliveryLocation%22:%22JijaMata%20Colony%2C%20Industrial%20Area%22%2C%22lat%22:19.2403305%2C%22lng%22:73.1305395}; _gcl_aw=GCL.1673376911.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB; _gac_0=1.1673376912.Cj0KCQiAtvSdBhD0ARIsAPf8oNmBJCSeCqlI2-_oa209M5K4YOiSKj-iInWotvyWGBBMt_Y36jR0ZZsaAuO8EALw_wcB; _is_logged_in=1; _sid=4roc2de7-8141-413b-870c-b62b7a0b3a98; _gat_0=1; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A13%2C%22s%22%3A1673419643%2C%22t%22%3A1673420476%7D; _ga=GA1.2.626327621.1673274584; _gat_UA-53591212-4=1; _ga_34JYJ0BCRN=GS1.1.1673419655.7.1.1673420492.0.0.0',
            'referer': 'https://www.swiggy.com/restaurants/gourmet-ice-cream-cakes-by-baskin-robbins-central-avenue-powai-mumbai-382680',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }
        params = {
            'lat': '19.2403305',
            'lng': '73.1305395',
            'menuId': Id,
        }
        respo = requests.get('https://www.swiggy.com/dapi/menu/v4/full', params=params, cookies=cookies, headers=headers)
        respo = respo.text
        data_ = json.loads(respo)
        data2 = data_['data']['menu']['items']
        #print(len(data2))
        
        #Scraping item details 
        for i in range(len(data2)):
            item_id = data2.keys()
            #print(len(item_id))
            for x in item_id:
                id = x
                item_Id.append(id)
                item = data2[x]['name']
                item_name.append(item)
                price = data2[x]['price']
                if len(str(price))>4:
                    price = price//100
                    item_price.append(price)
                elif price == 0:
                    price = data2[x]['defaultPrice']
                    item_price.append(price)
                else:
                    item_price.append(price)
                id_rest = data_['data']['id']
                res_id.append(id_rest)
                #print(Id+': '+id+' '+item+' '+str(price))    

#Storing Restaurant & Item details
try:
    with connection.cursor() as cursor:
        cursor.execute("USE swiggy_data")
        index = 0
        min_price = 150     
        for i in range(len(item_price)):
            if item_price[i] < min_price:
                index = i
                #print('Item Details:')
                print(item_Id[index]+' '+item_name[index]+' '+str(item_price[index])+' '+res_id[index])
                sql = "INSERT INTO swiggy_items(Item_ID, Item_Name, Price, Rest_ID) VALUES (%s, %s, %s, %s)"
                val = (item_Id[index], item_name[index], str(item_price[index]), res_id[index])
                cursor.execute(sql, val)
        res_id = list(set(res_id))
        for x in range(len(res_id)):
            restaurant_id = res_id[x]
            for y in range(len(rest_Id)):
                if rest_Id[y] == restaurant_id:
                    ind = rest_Id.index(restaurant_id)
                    #print('Restaurant Details:')
                    print(rest_Id[ind]+' '+rest_name[ind]+' '+rest_area[ind]+' '+str(rest_timing[ind])+' '+rest_discount[ind]+' '+str(rest_ratings[ind]))  
                    sql = "INSERT INTO swiggy_rest(Rest_ID, Rest_Name, Rest_Area, Delivery_Time, Distance, Discount, Rating) values (%s, %s, %s, %s, %s, %s, %s)"
                    val = (rest_Id[ind], rest_name[ind], rest_area[ind], rest_timing[ind], rest_discount[ind], rest_discount[ind], rest_ratings[ind])
                    cursor.execute(sql, val)
    connection.commit()
finally:
    connection.close()
