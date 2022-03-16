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
    if coin_name == "bitcoin":
        return 11

    elif coin_name == "ethereum":
        return 22
    
    elif coin_name == "tether":
        return 33

    elif coin_name == "usdcoin":
        return 44

    elif coin_name == "xrp":
        return 55

    elif coin_name == "binance":
        return 66