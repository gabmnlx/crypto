-- database setup
/* needed if database needs resetting
DROP TABLE coin;
DROP TABLE tweet;
*/
DROP DATABASE cryptodb;

-- create database
CREATE DATABASE cryptodb;
\c cryptodb

-- create tables here
CREATE TABLE coin(
    coinname VARCHAR(255) NOT NULL PRIMARY KEY,
    currentvalue FLOAT NOT NULL,
    coindescription VARCHAR(1024) NOT NULL,
    keywords VARCHAR(255) NOT NULL,
    fluctuation FLOAT NOT NULL,
    positivescore INT NOT NULL,
    negativescore INT NOT NULL,
    compoundscore FLOAT NOT NULL
);

CREATE TABLE tweet(
    tweetcoin VARCHAR(255) NOT NULL PRIMARY KEY,
    tweetid INT NOT NULL,
    handle VARCHAR(255) NOT NULL,
    datecreated TIMESTAMP NOT NULL,
    tweettext VARCHAR(1024) NOT NULL,
    cleanedtext VARCHAR(255) NOT NULL,
    keywords VARCHAR(255) NOT NULL,
    FOREIGN KEY(tweetcoin) REFERENCES coin(coinname)
);

-- insert or populate tables here
INSERT INTO coin
VALUES ('BITCOIN', 0.0, 'Bitcoin (₿) is a decentralized digital currency, without a \n
        central bank or single administrator, that can be sent from user to 
        user on the peer-to-peer bitcoin network without the need for 
        intermediaries.[7] Transactions are verified by network nodes 
        through cryptography and recorded in a public distributed ledger called 
        a blockchain. The cryptocurrency was invented in 2008 by an unknown 
        person or group of people using the name Satoshi Nakamoto.[9] The 
        currency began use in 2009[10] when its implementation was released 
        as open-source software.[6]', 'BTC', -0.81, 69, 96, 1.0);

INSERT INTO coin
VALUES ('ETHEREUM', 0.0, 'Ethereum is a decentralized, open-source blockchain with smart
        contract functionality. Ether (ETH or Ξ) is the native cryptocurrency 
        of the platform. Among cryptocurrencies, Ether is second only to 
        Bitcoin in market capitalization.[2][3]', 'ETH', -0.69, 69, 96, 1.0);

INSERT INTO coin
VALUES ('USDCOIN', 0.0, 'USD Coin (USDC) represents a major breakthrough in how we use money. 
        Digital dollars work like other digital content — 
        they move at the speed of the internet, 
        can be exchanged in the same way we share content, 
        and are cheaper and more secure than existing payment systems.', 'USDC', -7.77, 69, 96, 1.0);

INSERT INTO coin
VALUES ('TETHER', 0.0, 'Tether (often called by its symbol USDT) is a cryptocurrency that is hosted on the Ethereum and Bitcoin blockchains, among others. 
        Its tokens are issued by the Hong Kong company Tether Limited, 
        which in turn is controlled by the owners of Bitfinex. 
        Tether is called a stablecoin because it was originally designed to always be worth US$1.00, 
        maintaining $1.00 in reserves for each tether issued.', 'TET', 4.2, 69, 96, 1.0);

INSERT INTO coin
VALUES ('XRP', 0.0, 'Ripple is a global currency exchange and remittance network that aims to lower the cost and 
        improve the speed of international bank transfers relative to legacy financial infrastructure. 
        Also called the Ripple Transaction Protocol (RTXP) or Ripple protocol, 
        it is built upon a distributed open source Internet protocol, 
        consensus ledger and native currency called XRP (ripples). 
        Ripples consensus is based on the Federated Byzantine Agreement (FBA) - 
        a kind of middle ground between public, 
        permissionless blockchains such as Bitcoin and private, 
        permissioned blockchains such as Hyperledger Fabric.', 'XRP', 1.23, 69, 96, 1.0);

INSERT INTO coin
VALUES ('BINANCE', 0.0, 'Binance is a cryptocurrency exchange which is the largest 
        exchange in the world in terms of daily trading volume of 
        cryptocurrencies.[2] It was founded in 2017 and is registered in the 
        Cayman Islands.', 'BIN', 99.99, 69, 96, 1.0);