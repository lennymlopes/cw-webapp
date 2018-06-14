function random_bg_color() {
    var x = Math.floor(Math.random() * 256);
    var y = Math.floor(Math.random() * 256);
    var z = Math.floor(Math.random() * 256);
    var bgColor = "rgb(" + x + "," + y + "," + z + ")";
 console.log(bgColor);
  
    document.body.style.background = bgColor;
    }


function update(id, parameter, data) {
	socket.emit('update', id, parameter, data)
}

function remove(id) {
	var elem = document.getElementById(id);
	elem.remove();
	// document.getElementByID(id).remove();
	socket.emit('delete_alarm', id)
}

function toggle_moodlight(){
	socket.emit('moodlight')
}

function set_color(color, value) {
	socket.emit('set_color', color, value)
}

 function moodlight_off() {
 	socket.emit('moodlight_off')
 }

function alarm_off() {
	socket.emit('alarm_off')
}

function alarm_on() {
	socket.emit('alarm_on')
}

// socket.on('update', (parameter, data)) {
// 	if(parameter == 'moodlight'){
// 		if(data){
// 			document.getElementById("moodlight_checkbox").checked = true;
// 		} else {
// 			document.getElementById("moodlight_checkbox").checked = false;
// 		}
		
// 	}
// }

// window.onload = moodlight_off()


// var socket = io('http://localhost');
// socket.on('update', function (parameter, data) {
//     console.log(parameter, data);
    
//     if(parameter=='moodlight'){
//     	if(data){
//     		document.getElementById("moodlight_checkbox").checked = true;
//     	} else{
//     		document.getElementById("moodlight_checkbox").checked = false;
//     	}
//     }
//   });
