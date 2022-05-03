from bs4 import BeautifulSoup
import requests

def getCoinDesc(coin_name):
    if coin_name == "bitcoin":
        return """Bitcoin (₿) is a decentralized digital currency, without a \n
        central bank or single administrator, that can be sent from user to 
        user on the peer-to-peer bitcoin network without the need for 
        intermediaries.[7] Transactions are verified by network nodes 
        through cryptography and recorded in a public distributed ledger called 
        a blockchain. The cryptocurrency was invented in 2008 by an unknown 
        person or group of people using the name Satoshi Nakamoto.[9] The 
        currency began use in 2009[10] when its implementation was released 
        as open-source software.[6]"""

    elif coin_name == "ethereum":
        return """Ethereum is a decentralized, open-source blockchain with smart
        contract functionality. Ether (ETH or Ξ) is the native cryptocurrency 
        of the platform. Among cryptocurrencies, Ether is second only to 
        Bitcoin in market capitalization.[2][3]"""
    
    elif coin_name == "usdcoin":
        return """USD Coin (USDC) represents a major breakthrough in how we use money. Digital dollars work like other digital content — they move at the speed of the internet, can be exchanged in the same way we share content, and are cheaper and more secure than existing payment systems."""

    elif coin_name == "tether":
        return """Tether (often called by its symbol USDT) is a cryptocurrency that is hosted on the Ethereum and Bitcoin blockchains, among others. Its tokens are issued by the Hong Kong company Tether Limited, which in turn is controlled by the owners of Bitfinex. Tether is called a stablecoin because it was originally designed to always be worth US$1.00, maintaining $1.00 in reserves for each tether issued."""

    elif coin_name == "xrp":
        return """Ripple is a global currency exchange and remittance network that aims to lower the cost and improve the speed of international bank transfers relative to legacy financial infrastructure. Also called the Ripple Transaction Protocol (RTXP) or Ripple protocol, it is built upon a distributed open source Internet protocol, consensus ledger and native currency called XRP (ripples). Ripple's consensus is based on the Federated Byzantine Agreement (FBA) -- a kind of middle ground between public, permissionless blockchains such as Bitcoin and private, permissioned blockchains such as Hyperledger Fabric."""

    elif coin_name == "binance":
        return """Binance is a cryptocurrency exchange which is the largest 
        exchange in the world in terms of daily trading volume of 
        cryptocurrencies.[2] It was founded in 2017 and is registered in the 
        Cayman Islands."""



def curValue(coin_name):
    url = "https://coinmarketcap.com/currencies/"

    # because of how coinmarketcap's links are formatted:
    if coin_name == "usdcoin":
        url += "usd-coin"
    elif coin_name == "binance":
        url += "bnb"
    else:
        url += coin_name

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser") 

    priceClass = doc.find("div", class_="priceValue")
    if coin_name == "usdcoin":
        return priceClass.find("span").text + "00" # for consistency, cuz the scraped = 2 dec. places while stream = 4 dec. places
    return priceClass.find("span").text 
    

def eurToUsdConvert():
    url = "https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1"

    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")

    price = doc.find("div", class_="ccOutputBx")

    return price.findAll("span")[1].text[:4]

# def curValueToFile():
#     values = []
#     strings = ["bitcoin", "ethereum", "tether", "usd-coin", "xrp", "bnb"]
#     url = "https://coinmarketcap.com/currencies/"

#     for string in strings:
#         url = "https://coinmarketcap.com/currencies/" + string

#         result = requests.get(url)
#         doc = BeautifulSoup(result.text, "html.parser") 

#         priceClass = doc.find("div", class_="priceValue")
#         values.append(priceClass.find("span").text) 

#     values_file = open("coin_values.txt", "w")
#     for value in values:
#         values_file.write(value + "\n")
#     values_file.close()
#     print(values)
#     time.sleep(10)

#     curValueToFile()

def shortName(coin_name):
    if coin_name == "bitcoin":
        return "BTC"

    elif coin_name == "ethereum":
        return "ETH"
    
    elif coin_name == "tether":
        return "USDT"

    elif coin_name == "usdcoin":
        return "USDC"

    elif coin_name == "xrp":
        return "XRP"

    elif coin_name == "binance":
        return "BNB"


# update this
def getFluctuation(coin_name):
    if coin_name == "bitcoin":
        return -0.81

    elif coin_name == "ethereum":
        return -0.69
    
    elif coin_name == "tether":
        return 4.2

    elif coin_name == "usdcoin":
        return -7.77

    elif coin_name == "xrp":
        return 1.23

    elif coin_name == "binance":
        return 99.99