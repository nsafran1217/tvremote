'use strict'
 
var button;

function doIt(el) {
    button = el.className;
    var sleeptext = document.getElementById("sleeptime").value;
    $.ajax({
        type: "POST",
        url: "http://tv.nsafran.com:8000",
        data: { action: button, time: sleeptext},
        success: callbackFunc
    });

}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
    document.getElementById("status").innerHTML = response;
    if (button == 'Sleep'){
        document.getElementById("sleepstatus").innerHTML = response;
    }
    window.setTimeout((setStatusBack), 3000);
}

function setStatusBack() {
    (document.getElementById("status").innerHTML = "Make a selection")
}
