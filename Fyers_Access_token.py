# INSTALLATION:
# pip3 install fyers-apiv2

# AUTHORIZATION:
from fyers_api import fyersModel
from fyers_api import accessToken
import requests

client_id = '9BPNFGJHZ5-100'
secret_key = 'LJCTDO2WQY'
redirect_url = 'https://tradepop.com/TradeDhar/api-login'
response_type = 'code'
state = 'none'
API_ENDPOINT = 'https://api.fyers.in/api/v2/generate-authcode?client_id=9BPNFGJHZ5-100&redirect_uri=https%3A%2F%2Ftradepop.com%2FTradeDhar%2Fapi-login&response_type=code&state=None'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2MzM0MTY4NjAsImV4cCI6MTYzMzQxNzE2MCwibmJmIjoxNjMzNDE2ODYwLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUjExNjAyIiwibm9uY2UiOiIiLCJhcHBfaWQiOiI5QlBORkdKSFo1IiwidXVpZCI6IjY0Y2JmYzMxYTlhYzRkMzViNzY1NGJkMGRlZjc5Y2FjIiwiaXBBZGRyIjoiMjcuNTkuMTc3LjE2Iiwic2NvcGUiOiIifQ.WYI70KAwv5DH4uNmLurDRWHwnb_WBFSaKzZqhmrKM9M'

# session=accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_url, response_type='code', grant_type='authorization_code')

# response = session.generate_authcode()
# print(response)
# print(' ')

# #scope=”The value in scope must be openid if being passed.
# #Though this is an optional field”

# #Nonce = “The value in nonce can be any random string value.
# #This is also an optional field”

# # ------------------------------------  AUTH CODE ---------------------------------- #

    
# # print(data)
# print('Break')

# # sending post request and saving response as response object
# # r = requests.get(response)

# # r_attribs = [c for c in dir(r) if not c.startswith("_")]
# # r_attribs

# # # # extracting response text
# # #pastebin_url = r.code
# # print(r)

# # print('Break No 2')

# # print(r_attribs)
# # print(r.content)
# # print('Break No 3')
# # print(r.headers)

# # print(r.json)

# # print(r.request)

# # print(r.links)

# # print(r.history)

# # #auth_code = r["auth_code"]
# # print('auth_code')

# # print('Break No 4')
# # #authex = pastebin_url["auth_code"]
# # #print(authex)

# # print('Break No 5')

# auth_code = input('Enter auth_code: ')

# session.set_token(auth_code)
# response = session.generate_token()
# print(response)
# print(' ')

# access_token = response["access_token"]
# print(access_token)
# print(' ')

  # "You will be provided with the access_token which will have the below shown response" 

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
is_async = True  #(By default the async will be False, Change to True for async API calls.)

data = {
      "symbol":"NSE:SBIN-EQ",
      "qty":25,
      "type":1,
      "side":1,
      "productType":"INTRADAY",
      "limitPrice":370,
      "stopPrice":0,
      "validity":"DAY",
      "disclosedQty":0,
      "offlineOrder":"False",
      "stopLoss":0,
      "takeProfit":380
    }

profilex = fyers.place_order(data)
print(profilex)

data2 = {
      "symbol":"NSE:BANKNIFTY21O0737000PE",
      "qty":25,
      "type":1,
      "side":1,
      "productType":"INTRADAY",
      "limitPrice":370,
      "stopPrice":0,
      "validity":"DAY",
      "disclosedQty":0,
      "offlineOrder":"False",
      "stopLoss":360,
      "takeProfit":0
    }

profiley = fyers.place_order(data2)
print(profiley)
