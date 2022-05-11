function getExchangeRate() {
    const exchangeRateDiv = document.getElementById("exchange-rate")
    const conversionRate = parseFloat(document.getElementById("conversionRate").textContent)
    const coinName = window.location.href.slice(27)
    
    if (coinName == "bitcoin") {
        var ws = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade')
        var decimals = 2
    }
    else if (coinName == "ethereum") {
        var ws = new WebSocket('wss://stream.binance.com:9443/ws/ethusdt@trade')
        var decimals = 2
    }
    else if (coinName == "xrp") {
        var ws = new WebSocket('wss://stream.binance.com:9443/ws/xrpusdt@trade')
        var decimals = 4
    }
    else if (coinName == "usdcoin") {
        var ws = new WebSocket('wss://stream.binance.com:9443/ws/usdcusdt@trade')
        var decimals = 4
    }
    else if (coinName == "binance") {
        var ws = new WebSocket('wss://stream.binance.com:9443/ws/bnbusdt@trade')
        var decimals = 2
    }
    else if (coinName == "tether") {
        var ws = new WebSocket('wss://stream.binance.com:9443/ws/eurusdt@trade')
        var decimals = 4
    }
    
    ws.onmessage = (event) => {
        let stockObject = JSON.parse(event.data)
        if (coinName == "tether") {
            exchangeRate = "$" + parseFloat(stockObject.p/conversionRate).toFixed(decimals)
        }
        else {
            exchangeRate = "$" + parseFloat(stockObject.p).toFixed(decimals)
        }
        exchangeRateDiv.innerText =  exchangeRate
        
    }
    
    // var tws = new WebSocket('wss://stream.binance.com:9443/ws/eurusdt@trade')

    // tws.onmessage = (event) => {
    //     let tstockObject = JSON.parse(event.data)
    //     exchangeRate = "$" + parseFloat(tstockObject.p).toFixed(decimals)
    //     console.log((tstockObject.p/conversionRate).toFixed(4))
    // }




}

getExchangeRate()