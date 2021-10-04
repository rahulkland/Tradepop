# INSTALLATION:
# pip3 install fyers-apiv2

# AUTHORIZATION:
from fyers_api import fyersModel
from fyers_api import accessToken
import requests
import json

client_id = '9BPNFGJHZ5-100'
secret_key = 'LJCTDO2WQY'
redirect_url = 'https://tradepop.com/TradeDhar/api-login'
response_type = 'code'
state = 'none'
API_ENDPOINT = 'https://api.fyers.in/api/v2/generate-authcode?client_id=9BPNFGJHZ5-100&redirect_uri=https%3A%2F%2Ftradepop.com%2FTradeDhar%2Fapi-login&response_type=code&state=None'

session=accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_url, response_type='code', grant_type='authorization_code')

response = session.generate_authcode()
print(response)
print(' ')

#scope=”The value in scope must be openid if being passed.
#Though this is an optional field”

#Nonce = “The value in nonce can be any random string value.
#This is also an optional field”

# ------------------------------------  AUTH CODE ---------------------------------- #

    
# print(data)
print('Break')

# sending post request and saving response as response object
r = requests.get(response)

# # extracting response text
pastebin_url = r.json()
print(r)

print('Break No 2')

print(pastebin_url)
print('Break No 3')

#auth_code = r["auth_code"]
print('auth_code')

print('Break No 4')
authex = pastebin_url["auth_code"]
print(authex)

print('Break No 5')
session.set_token(auth_code)
response = session.generate_token()
print(response)
print(' ')

access_token = response["access_token"]
print(access_token)
print(' ')

  # "You will be provided with the access_token which will have the below shown response" 

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)

# is_async = True  #(By default the async will be False, Change to True for async API calls.)

profilex = fyers.get_profile()
print(profilex)

# your source code here
# source_code = '''
# print("Hello, world!")
# a = 1
# b = 2
# print(a + b)
# '''



  # log_path = "This will create logs in the local system and that will be stored in the particular local address you have defined"

  # def PlaceOrder(tradeSignal)
  # data = {
  #     "symbol":"tradeSignal",
  #     "qty":1,
  #     "type":1,
  #     "side":1,
  #     "productType":"INTRADAY",
  #     "limitPrice":0,
  #     "stopPrice":0,
  #     "validity":"DAY",
  #     "disclosedQty":0,
  #     "offlineOrder":"False",
  #     "stopLoss":0,
  #     "takeProfit":0
  #   }

  #   fyers.place_order(data)
