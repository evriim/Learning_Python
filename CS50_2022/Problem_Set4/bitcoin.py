"""Calculating current bitcoin value"""
import sys
import requests
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
try:
    amount = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit()

o = response.json()
btc = float(o["bpi"]["USD"]["rate_float"])
value = btc* amount
print(f"${value:,.4f}")
