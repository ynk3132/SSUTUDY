let timerId;
let time = 0;
const stopwatch = document.getElementById("stopwatch");
let  hour, min, sec;
let study = true;

function printTime() {
    time++;
    stopwatch.innerText = getTimeFormatString();
}

//시계 시작 - 재귀호출로 반복실행
function startClock() {
    study = true;
    sendJSON();
    printTime();
    stopClock();
    timerId = setTimeout(startClock, 1000);
}

//시계 중지
function stopClock() {
    if (timerId != null) {
        clearTimeout(timerId);
    }
}

// 시계 초기화
function resetClock() {
    stopClock();
    stopwatch.innerText = "00:00:00";
    time = 0;
}

// 시간(int)을 시, 분, 초 문자열로 변환
function getTimeFormatString() {
    hour = parseInt(String(time / (60 * 60)));
    min = parseInt(String((time - (hour * 60 * 60)) / 60));
    sec = time % 60;

    return String(hour).padStart(2, '0') + ":" + String(min).padStart(2, '0') + ":" + String(sec).padStart(2, '0');
}

function sendJSON() {
    let param = {'study': study};
    $.ajax({
        type:"POST",
        url:'send',
        dataType:"json",
        data:JSON.stringify(param),
        success: function(data){
            console.log("post성공");
            console.log(data);
            console.log(data["study"]);
            if(data["study"] == false) {
                stopClock();
            }
        },
        error:function() {
            console.log("통신에러");
        }
    })
}