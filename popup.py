import requests
from bs4 import BeautifulSoup

html = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(html.content)


tagBTC = soup.findAll("a", {"href": "/currencies/bitcoin/markets/"})
for btc in tagBTC:
	yazibtc = btc.text
	print("Bitcoin balance\t", yazibtc)





tagEth = soup.findAll("a", {"href": "/currencies/ethereum/markets/"})
for eth in tagEth:
	yazeth = eth.text
	print("Ethereum balance", yazeth)





tagbnc = soup.findAll("a", {"href": "/currencies/bnb/markets/"})
for bnc in tagbnc:
	yazbnc = bnc.text
	print("Binance balance\t", yazbnc)
