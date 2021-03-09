import os
import requests
import logging
from slack_sdk import WebClient

def checkPrices():
    #COIN = os.environ['CRYPTO']
    COIN = 'litecoin'
    TARGET = 45000
    #TARGET = os.environ['TARGET']
    #API_ENDPOINT = os.environ['API_ENDPOINTS']
    API_ENDPOINT = 'https://api.coingecko.com/api/v3/simple/price'
    #FIAT = os.environ['FIAT']
    FIAT = 'usd'
    update = ''
    params = {
        'ids': COIN,
        'vs_currencies': FIAT
    }
    response = requests.get(API_ENDPOINT, params=params)
    assert response.status_code == 200
    json_resp = response.json()
    price_at = json_resp[COIN][FIAT]
    if float(price_at)>= float(TARGET):
        update += '{0} is at {1}0'.format(COIN, price_at)
    return update

def sendSlackMessage(msg):
    #token = os.environ['SLACK_API_TOKEN']
    token = 'xoxb-1425355396916-1828783679762-qJ53Z1IrCSSaZGPr1yLTbAtL'
    #channel_id = os.environ['#crypto-alerts']
    channel_id = '#crypto-alerts'
    client = WebClient(token=token)
    response = client.chat_postMessage(channel =channel_id,text=msg)
    assert response['ok'] == 'true', response ['error']
    
#sendSlackMessage(checkPrices())

if __name__ == '__main__':
    #LOG_FILE = os.environ['LOG_FILE']
    LOG_FILE = '../bot.log'
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
    update =checkPrices()
    if update:
        try:
            sendSlackMessage(update)

        except Exception as err:
            logging.error(err)
            