function random_bg_color() {
    var x = Math.floor(Math.random() * 256);
    var y = Math.floor(Math.random() * 256);
    var z = Math.floor(Math.random() * 256);
    var bgColor = "rgb(" + x + "," + y + "," + z + ")";
 console.log(bgColor);
  
    document.body.style.background = bgColor;
    }


function update(parameter, data) {
	socket.emit('update', parameter, data)
}

function remove(id) {
	var elem = document.getElementById(id);
	elem.remove();
	// document.getElementByID(id).remove();
	socket.emit('update', id, "delete")
}