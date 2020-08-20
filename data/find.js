console.log("载体,飞行,起源,状态,到来");

function getarrivals(){
    for (let i = 1; i < 9; i++) {
        setTimeout(() => {
            var timeperiod = document.getElementsByClassName("timeperiod");
            var timeperiodNode = timeperiod[0].childNodes
            var shouldClick = timeperiodNode[i * 2];
            shouldClick.click();
            setTimeout(() => {
                var arrivals = document.getElementById("arrivals");
                var nodeColl = arrivals.childNodes;
                for (let j = 0; j < nodeColl.length; j++) {
                    var subTempText = "";
                    var airData = nodeColl[j].childNodes;
                    for (let k = 0; k < airData.length - 1; k++) {
                        var text = airData[k].childNodes[0].textContent;
                        subTempText += '"' + text + '"' + ',';
                    }
                    subTempText += '"' + airData[airData.length - 1].childNodes[0].textContent + '"';
                    console.log(subTempText);
                }
            }, 5000);
        }, i * 6000);
    }    
}

function getdepartures(){
    for (let i = 1; i < 9; i++) {
        setTimeout(() => {
            var timeperiod = document.getElementsByClassName("timeperiod");
            var timeperiodNode = timeperiod[0].childNodes
            var shouldClick = timeperiodNode[i * 2];
            shouldClick.click();
            setTimeout(() => {
                var departures = document.getElementById("departures");
                var nodeColl = departures.childNodes;
                for (let j = 0; j < nodeColl.length; j++) {
                    var subTempText = "";
                    var airData = nodeColl[j].childNodes;
                    for (let k = 0; k < airData.length - 1; k++) {
                        var text = airData[k].childNodes[0].textContent;
                        subTempText += '"' + text + '"' + ',';
                    }
                    subTempText += '"' + airData[airData.length - 1].childNodes[0].textContent + '"';
                    console.log(subTempText);
                }
            }, 5000);
        }, i * 6000);
    }    
}
