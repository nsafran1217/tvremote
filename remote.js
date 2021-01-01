'use strict'
 var PyServerURL = "http://tv.nsafran.com:8000"
function doIt(el) {
    var button = el.className;
    var sleeptext = document.getElementById("sleeptime").value;
    $.ajax({
        type: "POST",
        url: PyServerURL,
        data: { action: button, time: sleeptext},
        success: callbackFunc
    });

}

function checkIfSleepSched() {
    $.ajax({
        type: "POST",
        url: PyServerURL,
        data: { action: "CheckSleep", time: 0},
        success: callbackFunc
    });
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
    document.getElementById("status").innerHTML = response;
}


