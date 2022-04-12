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

showTime();