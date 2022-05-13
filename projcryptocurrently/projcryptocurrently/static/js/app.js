function showTime() {
    let current = new Date(); 
    let hr = current.getHours();
    let min = current.getMinutes();
    let secs = current.getSeconds();
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

    if (min == "00" && secs == "00") {
        console.log("Reloading...")
        location.reload()
    }

    let t = setTimeout(function(){ showTime() }, 1000);
}


// getting coin values

const btcElement = document.getElementById("btc-price")
var btcPrice = btcElement.textContent //+ " stock"
let btcPrices = [0, btcPrice]

const ethElement = document.getElementById("eth-price")
var ethPrice = ethElement.textContent //+ " stock"

const xrpElement = document.getElementById("xrp-price")
var xrpPrice = xrpElement.textContent //+ " stock"

const usdcElement = document.getElementById("usdc-price")
var usdcPrice = usdcElement.textContent //+ " stock"

const bnbElement = document.getElementById("bnb-price")
var bnbPrice = bnbElement.textContent //+ " stock"

const usdtElement = document.getElementById("usdt-price")
var usdtPrice = usdtElement.textContent //+ " stock"

const conversionRate = parseFloat(document.getElementById("conversionRate").textContent)


function getBtcValue() {
    let btcWs = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade')
    btcWs.onmessage = (event) => {
        let btcStockObject = JSON.parse(event.data)
        btcPrice = "$" + parseFloat(btcStockObject.p).toFixed(2)
        btcElement.innerText = btcPrice

        // getting fluctuations
        
        // btcPrices.shift()
        // btcPrices.push(btcPrice)
        // console.log(btcPrices)
        // let fluctuation = 1 - parseInt(btcPrices[0].slice(1,btcPrices.length)) / parseInt(btcPrices[1].slice(1,btcPrices.length))
        // console.log(fluctuation)
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

function getUsdtValue() {
    var usdtWs = new WebSocket('wss://stream.binance.com:9443/ws/eurusdt@trade')
    usdtWs.onmessage = (event) => {
        let tstockObject = JSON.parse(event.data)
        usdtPrice = "$" + parseFloat(tstockObject.p/conversionRate).toFixed(4)
        usdtElement.innerText = usdtPrice
    }
}

showTime();
getBtcValue()
getEthValue()
getXrpValue()
getUsdcValue()
getBnbValue()
getUsdtValue()

// filter button event

const bitcoinDIv = document.getElementById("bitcoin")
const ethDiv = document.getElementById("ethereum")
const xrpDiv = document.getElementById("xrp")
const usdcDiv = document.getElementById("usd")
const bnbDiv = document.getElementById("bnb")
const tetherDiv = document.getElementById("tether")

function filterButtonClick() {
    const selectedFilterValue = document.getElementById("crypto-filters").value 
    const coinList = ["bitcoin", "ethereum", "xrp", "usd", "bnb", "tether"]

    if (selectedFilterValue == "positive-fluctuation") {
        resetButtonClick();
        const divContent = document.getElementById("negative-fluc-filter").textContent.slice(1,-1)
        var positiveFlucsList = divContent.split(", ")
        for (var i = 0; i<positiveFlucsList.length; i++) {
            positiveFlucsList[i] = positiveFlucsList[i].slice(1,-1)
        }
        for (var j = 0; j<positiveFlucsList.length; j++) {
            document.getElementById(positiveFlucsList[j]).classList.add("filter-opacity-50")
        }
    }
    else if (selectedFilterValue == "negative-fluctuation") {
        resetButtonClick();
        const divContent = document.getElementById("positive-fluc-filter").textContent.slice(1,-1)
        var positiveFlucsList = divContent.split(", ")
        for (var i = 0; i<positiveFlucsList.length; i++) {
            positiveFlucsList[i] = positiveFlucsList[i].slice(1,-1)
        }
        for (var j = 0; j<positiveFlucsList.length; j++) {
            document.getElementById(positiveFlucsList[j]).classList.add("filter-opacity-50")
        }
    }
    else if (selectedFilterValue == "max-positive-sentiment") {
        resetButtonClick();
        const divContent = document.getElementById("max-positive-sentiment").textContent
        for (var i=0; i<coinList.length;i++) {
            if (i!=parseInt(divContent)) {
                document.getElementById(coinList[i]).classList.add("filter-opacity-50")
            }
            else {
                document.getElementById(coinList[i]).classList.add("filter-highlight-green")
            }
        }
    }
    else if (selectedFilterValue == "min-positive-sentiment") {
        resetButtonClick();
        const divContent = document.getElementById("min-positive-sentiment").textContent
        for (var i=0; i<coinList.length;i++) {
            if (i!=parseInt(divContent)) {
                document.getElementById(coinList[i]).classList.add("filter-opacity-50")
            }
            else {
                document.getElementById(coinList[i]).classList.add("filter-highlight-red")
            }
        }
    }
    else if (selectedFilterValue == "max-negative-sentiment") {
        resetButtonClick();
        const divContent = document.getElementById("max-negative-sentiment").textContent
        for (var i=0; i<coinList.length;i++) {
            if (i!=parseInt(divContent)) {
                document.getElementById(coinList[i]).classList.add("filter-opacity-50")
            }
            else {
                document.getElementById(coinList[i]).classList.add("filter-highlight-red")
            }
        }
    }
    else if (selectedFilterValue == "min-negative-sentiment") {
        resetButtonClick();
        const divContent = document.getElementById("min-negative-sentiment").textContent
        for (var i=0; i<coinList.length;i++) {
            if (i!=parseInt(divContent)) {
                document.getElementById(coinList[i]).classList.add("filter-opacity-50")
            }
            else {
                document.getElementById(coinList[i]).classList.add("filter-highlight-green")
            }
        }
    }
    else if (selectedFilterValue == "more-positive-sentiments") {
        resetButtonClick();
        const divContent = document.getElementById("more-positive-sentiments").textContent
        const listOfMorePositive = JSON.parse(divContent)
        for (var i=0;i<coinList.length;i++) {
            if (!listOfMorePositive.includes(i)) {
                document.getElementById(coinList[i]).classList.add("filter-opacity-50")
            }
        }
    }
    else if (selectedFilterValue == "more-negative-sentiments") {
        resetButtonClick();
        const divContent = document.getElementById("more-negative-sentiments").textContent
        const listOfMoreNegative = JSON.parse(divContent)
        for (var i=0;i<coinList.length;i++) {
            if (!listOfMoreNegative.includes(i)) {
                document.getElementById(coinList[i]).classList.add("filter-opacity-50")
            }
        }
    }
}

function resetButtonClick() {
    bitcoinDIv.classList.remove("filter-invi")
    ethDiv.classList.remove("filter-invi")
    xrpDiv.classList.remove("filter-invi")
    usdcDiv.classList.remove("filter-invi")
    bnbDiv.classList.remove("filter-invi")
    tetherDiv.classList.remove("filter-invi")

    
    bitcoinDIv.classList.remove("filter-opacity-50")
    ethDiv.classList.remove("filter-opacity-50")
    xrpDiv.classList.remove("filter-opacity-50")
    usdcDiv.classList.remove("filter-opacity-50")
    bnbDiv.classList.remove("filter-opacity-50")
    tetherDiv.classList.remove("filter-opacity-50")

    
    bitcoinDIv.classList.remove("filter-highlight-green")
    ethDiv.classList.remove("filter-highlight-green")
    xrpDiv.classList.remove("filter-highlight-green")
    usdcDiv.classList.remove("filter-highlight-green")
    bnbDiv.classList.remove("filter-highlight-green")
    tetherDiv.classList.remove("filter-highlight-green")

    
    bitcoinDIv.classList.remove("filter-highlight-red")
    ethDiv.classList.remove("filter-highlight-red")
    xrpDiv.classList.remove("filter-highlight-red")
    usdcDiv.classList.remove("filter-highlight-red")
    bnbDiv.classList.remove("filter-highlight-red")
    tetherDiv.classList.remove("filter-highlight-red")
}

function resetButtonClickv2() {
    resetButtonClick();
    document.getElementById("crypto-filters").value = "no-filter"
}



document.getElementById("filter-button").addEventListener("click", filterButtonClick)
document.getElementById("reset-button").addEventListener("click", resetButtonClickv2)


if (!window.localStorage.getItem("firstTime")) {
    document.getElementById("tour-modal").style = `display: block;`
    window.localStorage.setItem("firstTime", false)
}

