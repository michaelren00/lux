// Fade in on Arrival
$(document).ready(function(){
  $("#textbox-container").fadeIn(1200);
  $("#landingpage").fadeIn(1200);
});


function getInputValue() {
  var phoneNumber = document.getElementById("phoneNumber").value
fetch('http://127.0.0.1:5000/sendMessage', {method:"POST", mode: 'no-cors', headers: {'Content-Type': 'application/json'},body:JSON.stringify({to: phoneNumber})}).then( response => console.log(response));
}

// Get the input field
var input = document.getElementById("phoneNumber");

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

var personalize_questions = document.getElementById("personalize_questions")

$(document).ready(function(){
      $('input[type="checkbox"]').click(function(){
          if($(this).prop("checked") == true){
            personalize_questions.style.height = "auto";
          }
          else if($(this).prop("checked") == false){
            personalize_questions.style.height = "0";
          }
      });
  });