import os
import request
import logging
from slack import WebClient

def checkPrices():
    COIN = os.environ['COIN']
    TARGET = os.environ['TARGET']
    API_ENDPOINT = os.environ['API_ENDPOINT']
    FIAT = os.environ['FIAT']
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
        token = os.environ['SLACK_API_TOKEN']
        channel_id = os.environ['SLACK_CHANNEL_ID']
        client = WebClient(token=token)
        response = client.chat_postMessage(channel =channel_id,text=msg)
        assert response['ok'] == 'true', response ['error']
    

    if __name__ == '__main__':
        LOG_FILE = os.environ['LOG_FILE']
        logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
        update =checkPrices()
        if update:
            try:
                sendSlackMessage(update)

            except Exception as err:
                logging.error(err)
            