function showTime() {
    let current = new Date(); 
    let hr = current.getHours();
    let min = current.getMinutes();
    let dt = current.getDate();
    let mon = current.getMonth();
    let session = "AM";
    let day = document.getElementById("dayOfTheWeek").textContent;
  
    if (hr === 0) {
        hr = 12;
    }
    if (hr > 12) {
        hr = hr - 12;
        session = "PM";
    }
  
    hr = (hr < 10) ? "0" + hr : hr;
    min = (min < 10) ? "0" + min : min;
    dt = (dt < 10) ? "0" + dt : dt;
    mon = (mon < 10) ? "0" + mon : mon;
    
    let date = mon + "/" + dt;
    let time = hr + ":" + min + " " + session;

    document.getElementById("date").innerText = date;
    document.getElementById("time").innerText = day + ", " + time;

    let t = setTimeout(function(){ showTime() }, 1000);
}


// getting coin values

const btcElement = document.getElementById("btc-price")
var btcPrice = btcElement.textContent + " stock"

const ethElement = document.getElementById("eth-price")
var ethPrice = ethElement.textContent + " stock"

const xrpElement = document.getElementById("xrp-price")
var xrpPrice = xrpElement.textContent + " stock"

const usdcElement = document.getElementById("usdc-price")
var usdcPrice = usdcElement.textContent + " stock"

const bnbElement = document.getElementById("bnb-price")
var bnbPrice = bnbElement.textContent + " stock"

const usdtElement = document.getElementById("usdt-price")
var usdtPrice = usdtElement.textContent + " stock"



function getBtcValue() {
    let btcWs = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade')
    btcWs.onmessage = (event) => {
        let btcStockObject = JSON.parse(event.data)
        btcPrice = "$" + parseFloat(btcStockObject.p).toFixed(2)
        btcElement.innerText = btcPrice
    }
}

function getEthValue() {
    let ethWs = new WebSocket('wss://stream.binance.com:9443/ws/ethusdt@trade')
    ethWs.onmessage = (event) => {
        let ethStockObject = JSON.parse(event.data)
        ethPrice = "$" + parseFloat(ethStockObject.p).toFixed(2)
        ethElement.innerText =  ethPrice
    }
}

function getXrpValue() {
    let xrpWs = new WebSocket('wss://stream.binance.com:9443/ws/xrpusdt@trade')
    xrpWs.onmessage = (event) => {
        let xrpStockObject = JSON.parse(event.data)
        xrpPrice = "$" + parseFloat(xrpStockObject.p).toFixed(4)
        xrpElement.innerText =  xrpPrice
    }
}

function getUsdcValue() {
    let usdcWs = new WebSocket('wss://stream.binance.com:9443/ws/usdcusdt@trade')
    usdcWs.onmessage = (event) => {
        let usdcStockObject = JSON.parse(event.data)
        usdcPrice = "$" + parseFloat(usdcStockObject.p).toFixed(4)
        usdcElement.innerText =  usdcPrice
    }
}

function getBnbValue() {
    let bnbWs = new WebSocket('wss://stream.binance.com:9443/ws/bnbusdt@trade')
    bnbWs.onmessage = (event) => {
        let bnbStockObject = JSON.parse(event.data)
        bnbPrice = "$" + parseFloat(bnbStockObject.p).toFixed(2)
        bnbElement.innerText =  bnbPrice
    }
}

showTime();
getBtcValue()
getEthValue()
getXrpValue()
getUsdcValue()
getBnbValue()
