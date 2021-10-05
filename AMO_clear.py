#!/usr/bin/env python3
# A simple script to print all updates received
#
# NOTE: To run this script you MUST have 'TG_API_ID' and 'TG_API_HASH' in
#       your environment variables. This is a good way to use these private
#       values. See https://superuser.com/q/284342.

from os import environ

# environ is used to get API information from environment variables
# You could also use a config file, pass them as arguments,
# or even hardcode them (not recommended)

from fyers_api import fyersModel
from fyers_api import accessToken
import requests
import json

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

################    FYERS CREDENTIALS ##########################

access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2MzM0NjUwNDMsImV4cCI6MTYzMzQ4MDIyMywibmJmIjoxNjMzNDY1MDQzLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaFhMTFRvVjB6R1VncG5kbkYtUDZidkpiRGxtQm9lQzVUbFhQVTNKSTF2SXZBek04b25nYVNiQmR3VTdCUjdKZjVSX0wtTzIwX1N0TUw3ZTY5UmRvZUE1aW1qNHlXSmhESzBHUGRZelNhMHVNUEpTbz0iLCJkaXNwbGF5X25hbWUiOiJSQUhVTCBWQVJNQSIsImZ5X2lkIjoiWFIxMTYwMiIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.hPvqSjE82CRBtVLDhn9bo9QmO_FMOl4FA5iATacKIrw'

client_id = '9BPNFGJHZ5-100'
secret_key = 'LJCTDO2WQY'
redirect_url = 'https://tradepop.com/TradeDhar/api-login'


api_id = 8289565
api_hash = '7e958c4c4ea8f0cea7485196733ca4ad'

phone = '+919003199379'
username = '1273828837'

BANK_NIFTY = 'BankNifty'
NIFTY = 'Nifty'
Put = 'PE'
Call = 'CE'
Buy = 'Buy'
Sell = 'Sell'

stockType = ''
optionType = ''
orders = ''
transactionType = ''
suggestedEntryPrice = 0
currentTrades = {}

tradeSignalGroupName = 'Support Signals (Platinum Batch 5)'
tradeStatusGroupName = 'Dharamik Signals Live'

messageFilter = ['Buy', 'Target']
stockFilter = ['BankNifty', 'Nifty', '#BankNifty', '#Nifty']
stopLossKeyWords = ['stoploss','sl','risk']

data = {"id":'52110059312'}

weeklyExpiryMonth = {"JAN": "1", "FEB": "2", "MAR": "3", "APR": "4", "MAY": "5", "JUN": "6", "JUL": "7", "AUG": "8", "SEP": "9", "OCT": "O", "NOV": "N", "DEC": "D"}

def main():
    # session_name = environ.get('TG_SESSION', 'session')
    # client = TelegramClient(username, api_id, api_hash)

    fyers_app_id = "9BPNFGJHZ5-100"

    # access_token = request_auth()
    
    fyers = fyersModel.FyersModel(client_id=fyers_app_id, token=access_token)
    
    ## ----- Cancel AMO order ----- ##
    
    print(fyers.get_profile())
    print(' ')
    orders = fyers.orderbook()
    
    orderBook = orders.get('orderBook')
    
    # print(orderBook)
    
    # id_var = 'id'
    
    for order in orderBook or []:
        if order["message"] == '':
            id_var = order["id"]
            data = {"id":id_var}
            print(data) 
            print('')
            respo = fyers.cancel_order(data)
            printt(respo)
            print('')
       
     #print(data)
# def update_handler(update):
#     print(update)

def request_auth():

    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe", chrome_options = options)

    # Authentication
    app_id = "9BPNFGJHZ5-100"
    app_secret = "LJCTDO2WQY"
    session=accessToken.SessionModel(client_id=app_id, secret_key=app_secret, redirect_uri=redirect_url, response_type='code', grant_type='authorization_code')
    #app_session = accessToken.SessionModel(app_id, app_secret)
    #response = app_session.auth()
    response = session.generate_authcode()
    print('Generate AuthCode response - ' + response)



    # Getting authorized code into a variable
    #authorization_code = response['data']['authorization_code']

    # Setting a Session
    #print(app_session.set_token(authorization_code))

    #access_token_url = app_session.generate_token()

    # Opening Url through Selenium
    driver.get(str(response))

    usn = driver.find_element_by_id('fyers_id')
    usn.send_keys('XR11602')
    time.sleep(2)

    pwd = driver.find_element_by_id('password')
    pwd.send_keys('Hubble2426!')
    time.sleep(2)

    driver.find_element_by_class_name('login-span-pan').click()
    time.sleep(2)

    pan = driver.find_element_by_id('pancard')
    pan.send_keys('AQCPV3101H')
    time.sleep(2)

    driver.find_element_by_id('btn_id').click()


    WebDriverWait(driver,20).until(EC.title_contains('tradepop'))
    # getting access token from browser
    
    authcode = driver.current_url.split('=', 3)[3].split('&', 1)[0]

    session.set_token(authcode)
    response = session.generate_token()
    access_token = response["access_token"]
 

   # Quiting the browser
    driver.quit()

    return access_token


if __name__ == '__main__':
    
    main()
