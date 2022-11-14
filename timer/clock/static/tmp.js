function clicked() {
    console.log("ASDF");
    //timer = setInterval(postJSON, 1000);
    startClock();
}

function getJSON() {
        $.ajax({
        type:"get",
        url:"send.json",
        dataType:"json",
        success: function(data){
            console.log("get성공");
            console.log(data);
            console.log(typeof(data));
            console.log(data["study"]);
        },
        error:function(){
            console.log("통신에러");
        }
    })
}

function postJSON() {
    let param = {'study': false};
    $.ajax({
        type:"POST",
        url:'send',
        //dataType:"json",
        data:JSON.stringify(param),
        success: function(data){
            console.log("post성공");
            console.log(data);
            console.log(data["study"]);
        },
        error:function() {
            console.log("통신에러");
        }
    })
}
