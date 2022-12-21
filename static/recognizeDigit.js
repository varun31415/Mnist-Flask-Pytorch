var canvas = document.getElementById("drawing-canvas")
var ctx = canvas.getContext("2d")

document.getElementById("run-btn").onclick = function() {
    var data = new FormData();
    var imageData = ctx.getImageData(0,0,252,252).data
    var num = 0
    var newData = []
    for (dat in imageData) {
        num += 1
        if (num == 3) {
            num = 0;
            newData.push(dat.parseInt())
        }
    }
    data.append("image", newData)

    const xhttp = new XMLHttpRequest();
    xhttp.open("POST","/get_data", true)
    xhttp.send(data)
    xhttp.onload = function() {
        document.getElementById("digit").innerHTML = xhttp.responseText;
    }
}