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
    
    elif coin_name == "cardano":
        return """Cardano is a public blockchain platform. It is open-source and
        decentralized, with consensus achieved using proof of stake. It can 
        facilitate peer-to-peer transactions with its internal cryptocurrency, 
        ADA"""

    elif coin_name == "dogecoin":
        return """Dogecoin (/ˈdoʊ(d)ʒkɔɪn/ DOHJ-koyn or DOHZH-koyn,[2] code: 
        DOGE, symbol: Ð) is a cryptocurrency created by software engineers Billy
        Markus and Jackson Palmer, who decided to create a payment system as a 
        "joke", making fun of the wild speculation in cryptocurrencies at the
        time."""

    elif coin_name == "stellar":
        return """Stellar, or Stellar Lumens, is an open source, decentralized 
        protocol for digital currency to fiat money low-cost transfers which 
        allows cross-border transactions between any pair of currencies.[2] 
        The Stellar protocol is supported by a Delaware nonprofit corporation, 
        the Stellar Development Foundation, though this organization does not 
        enjoy 501(c)(3) tax-exempt status with the IRS."""

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
    
    elif coin_name == "cardano":
        return 33

    elif coin_name == "dogecoin":
        return 44

    elif coin_name == "stellar":
        return 55

    elif coin_name == "binance":
        return 66