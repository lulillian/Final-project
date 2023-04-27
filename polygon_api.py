import urllib.request
import json 
import requests
# from twilio.rest import Client

# account_sid = 'ACe80acc1f799264efa60d041e1a09f0a1'
# auth_token = 'd1d68ae9a07296f59ab450a1eeb205d6'
# client = Client(account_sid, auth_token)
# # def send_message():
# message = client.messages.create(
#     body='Hello, World!',
#     from_='+18449492451',
#     to='+13477310296')
    
# print(message.sid)

# # send_message()




#URLS

#APIKEYS
APIKEY='4AWAZvbBUZLt_Yz8NpMMiKuUWbSqaUqe'



def get_json(url:str):
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    """
    # f=urllib.request.urlopen(url)
    # response_text=f.read().decode('utf-8')
    # response_data=json.loads(response_text)
    # return (response_data)
    response = requests.get(url)
    data = response.json()
    return data

def get_daily_open_close(TICKER:str):
    """
    Returns the price of a given ticker.
    """
    TICKER=TICKER.upper()
    url=f'https://api.polygon.io/v1/open-close/{TICKER}/2023-01-09?adjusted=true&apiKey={APIKEY}'
    data=get_json(url)
    # print(data)
    open=float(data['open'])
    close=float(data['close'])
    open_close_tup=(open,close)
    change = ((close-open)/open)*100
    change_rounded=round(change,2)
    print(f'The openning price of {TICKER} is {open}, and the market closed at {close}, changing {change_rounded} %.')

def get_open(TICKER:str):
    """
    Returns the price of a given ticker.
    """
    TICKER=TICKER.upper()
    url=f'https://api.polygon.io/v1/open-close/{TICKER}/2023-01-09?adjusted=true&apiKey={APIKEY}'
    data=get_json(url)
    # print(data)
    open=data['open']
    print(open) 

get_open('aapl')

def get_company_info(TICKER:str):
    """
    Given a company ticker,return basic info on the company.
    """
    TICKER=TICKER.upper()
    url=f'https://api.polygon.io/v3/reference/tickers/{TICKER}?apiKey={APIKEY}'
    data=get_json(url)
    # print(data)
    company_description=data['results']['description']
    market_cap=data['results']['market_cap']
    homepage_url=data['results']['homepage_url']
    name=data['results']['name']
    shares_outstanding=data['results']['share_class_shares_outstanding']
    print(shares_outstanding)

# get_company_info('hd')

def get_shares_out(TICKER:str):
    """
    Given a company ticker,return basic info on the company.
    """
    TICKER=TICKER.upper()
    url=f'https://api.polygon.io/v3/reference/tickers/{TICKER}?apiKey={APIKEY}'
    data=get_json(url)
    # print(data)
    shares_outstanding=data['results']['share_class_shares_outstanding']
    return shares_outstanding

# print(get_shares_out('AAPL'))


def ticker_news(TICKER:str):
    """Returns recent news links given a ticker."""
    TICKER=TICKER.upper()
    url=f'https://api.polygon.io/v2/reference/news?ticker={TICKER}&apiKey={APIKEY}'
    data=get_json(url)
    # print(data)
    article_dict=data['results']
    print(article_dict)
    links=[]
    for articles in article_dict:
        article_link=articles['article_url']
        # print(article_link)
        links.append(article_link)
    return links
# print(ticker_news('tsla'))



def balance_sheet(TICKER:str):
    """Returns balance sheet info of a company given its ticker."""
    TICKER=TICKER.upper()
    url=f'https://api.polygon.io/vX/reference/financials?ticker={TICKER}&apiKey={APIKEY}'
    data=get_json(url)
    # print(data)
    # noncurrent_liabilities=data['results'][0]['financials']['balance_sheet']['noncurrent_liabilities']['value']
    # current_liabilities=data['results'][0]['financials']['balance_sheet']['current_liabilities']['value']
    assets=float(data['results'][0]['financials']['balance_sheet']['assets']['value'])
    liabilities=float(data['results'][0]['financials']['balance_sheet']['liabilities']['value'])
    oustanding_stock=float(data['results'][0]['financials']['balance_sheet']['liabilities']['value'])
    book_value=float(assets-liabilities)
    print(book_value)
    shares_outstanding=float(get_shares_out(TICKER))
    book_value_shareprice=book_value/shares_outstanding
    # print(book_value_shareprice)



# balance_sheet('AAPL')