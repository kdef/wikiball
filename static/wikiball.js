console.log('wikiball js loaded');

// game controller

var start = document.getElementById('start').textContent;
var end = document.getElementById('end').textContent;
var cur = start;

var clicks = document.getElementById('clicks');
var time = document.getElementById('time');
var numClicks = -1;
var runTime = 0; // in seconds

// setup the wikipage
var iframe = document.createElement('iframe');
iframe.onload = function() {
    // if first load, start the timer
    if (numClicks === -1) {
        setInterval(updateTimer, 1000);
    }

    // otherwise the player has clicked
    numClicks++;
    clicks.textContent = numClicks;

    // check if the game is over
    var iframeDoc = iframe.contentWindow.document;
    if (iframeDoc) {
        cur = iframeDoc.getElementById('firstHeading').textContent;
        if (cur === end) {
            alert('Finished!\n' +
                    'clicks: ' + numClicks + '\n' +
                    'time: ' + time.textContent);
            window.location.href = '/';
        }
    }
};
iframe.src = '/wiki/' + start;
document.getElementById('wiki_page').appendChild(iframe);

// setup the timer
function updateTimer() {
    runTime++;
    var seconds = pad(runTime % 60);
    var minutes = pad(Math.floor(runTime / 60));
    time.textContent = minutes + ':' + seconds;
}

function pad(num) {
    // force the value to string
    num = num + '';
    if (num.length < 2) {
        return '0' + num;
    }
    return num;
}
