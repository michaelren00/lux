// Fade in on Arrival
$(document).ready(function(){
  $("#textbox-container").fadeIn(1200);
  $("#landingpage").fadeIn(1200);
});


function getInputValue() {
  var phoneNumber = document.getElementById("textbox").value
fetch('http://127.0.0.1:5000/sendMessage', {method:"POST", mode: 'no-cors', headers: {'Content-Type': 'application/json'},body:JSON.stringify({to: phoneNumber})}).then( response => console.log(response));
  // xhr.send(phoneNumber);
  alert(phoneNumber)
}

// Get the input field
var input = document.getElementById("textbox");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("button").click();
  }
});

