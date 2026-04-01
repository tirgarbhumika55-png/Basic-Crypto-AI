import requests

url1 = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
url2 = "https://api.exchangerate-api.com/v4/latest/USD"
url3 = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"

response1 = requests.get(url1)

response2 = requests.get(url2)

response3 = requests.get(url3)

if response1.status_code == 200 and response2.status_code ==200 and response3.status_code == 200:
    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()

    btc_usd = data1["bitcoin"]["usd"]
    usd_inr = data2["rates"]["INR"]
    btc_inr_api = data3["bitcoin"]["inr"]
     
    print("Bitcoin price (USD):",btc_usd)
    print("USD to INR Rate is:", usd_inr)

    btc_inr = btc_usd * usd_inr
    print("Converted Bitcoin value in INR:", btc_inr)
    print("API Bitcoin INR:", btc_inr_api)

    difference = abs(btc_inr_api - btc_inr)
    print("Difference", difference)
else:
    print("Error in fetching data")