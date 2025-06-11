import requests
import json
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    numberOfBTC = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

while True:
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=38518ce7ccdb9b7fbbacdf177232f42def18cc265bb32a41e25e5958f266b5dc")
        break
    except requests.RequestException:
        continue
    
data = response.json()

innerData = data["data"]
priceInUSD = float(innerData['priceUsd'])
totalPrice = numberOfBTC * priceInUSD
print(f"${totalPrice:,.4f}")
#print('price :', priceInUSD)

