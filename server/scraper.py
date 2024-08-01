from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as uReq

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' ,
    'Accept-Language': 'en-US'
}

def dollar_to_rupee(dollar):
    money = dollar.split(',')
    var = "".join(money)
    rupee = float(var) * 83.75
    return rupee


def amazon(query):
    words = query.split()
    var = len(words)
    query_str = "+".join(words)
    url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + query_str

    r = requests.get(url , headers=HEADERS)
    soup = bs(r.content , 'html.parser')

    titles = soup.find_all('span' , attrs={'class': 'a-size-medium a-color-base a-text-normal'})
    prices_whole = soup.find_all('span' , attrs={'class': 'a-price-whole'})
    prices_fraction = soup.find_all('span' , attrs={'class': 'a-price-fraction'})
    data = {'items': []}

    for i in range(min(len(titles) , len(prices_fraction) , len(prices_whole))):
        cost = dollar_to_rupee(prices_whole[i].text + prices_fraction[i].text)
        cost_str = f"{cost:.2f}"
        item = {
            'name': titles[i].text ,
            'price': "₹" + cost_str
        }
        data['items'].append(item)

    return data


def snapdeal(query):


    # Hacky fix
    words = query.split()
    var = len(words)
    str = "+".join(words)

    url = ("https://www.snapdeal.com/search?keyword=" +str +
               "&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")

    r = requests.get(url)

    soup = bs(r.content , 'html.parser')

    data = {
        'items': []
    }
    if not soup.find_all('p' , attrs={'class': 'product-title'}):
        data = {'message': 'Item not on snapdeal'}
    else:
        names = soup.find_all('p' , attrs={'class': 'product-title'})
        prices = soup.find_all('span' , attrs={'class': 'lfloat product-price'})
        for i in range(min(len(names) , len(prices))):
            item = {
                'name': names[i].text ,
                'price': prices[i].text
            }
            data['items'].append(item)

    return data


def flipkart(query):
    flipkart_url = "https://www.flipkart.com/search?q=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' ,
        'Accept-Language': 'en-US,en;q=0.9' ,
        'Accept-Encoding': 'gzip, deflate, br' ,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,
        'Referer': 'https://www.flipkart.com/' ,
        'Connection': 'keep-alive'
    }

    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(flipkart_url)
        response.raise_for_status()
        flipkartPage = response.text
        soup = bs(flipkartPage , 'html.parser')

        names = []
        prices = soup.find_all('div' , attrs={'class': 'Nx9bqj'})
        if soup.find('div' , attrs={'class': 'KzDlHZ'}):
            names = soup.find_all('div' , attrs={'class': 'KzDlHZ'})
        else:
            names = soup.find_all('a' , attrs={'class': 'wjcEIp'})

        data = {
            'items': []
        }

        for i in range(min(len(names) , len(prices))):
            item = {
                'name': names[i].text ,
                'price': prices[i].text
            }
            data['items'].append(item)

        return data

    except requests.exceptions.HTTPError as http_err:
        return {'message': f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {'message': f"An error occurred: {err}"}


if __name__ == '__main__':
    url_str = input("Enter the product category you want to search for: ")
    data1 = snapdeal(url_str)
    data2 = amazon(url_str)
    data3 = flipkart(url_str)
    if 'message' in data1.keys():
        print(data1['message'])
    else:
        for i , item in enumerate(data1['items']):
            print(i + 1 , ' --> ' , item['name'] , ' : ' , item['price'])

    for i , item in enumerate(data2['items']):
        print(i + 1 , ' --> ' , item['name'] , ' : ' , item['price'])

    for i , item in enumerate(data3['items']):
        print(i + 1 , ' --> ' , item['name'] , ' : ' , item['price'])
