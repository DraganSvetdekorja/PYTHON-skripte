$(document).ready(function() {
  // Perform an action when the button is clicked
  $('#myButton').click(function() {
    var inputValue = $('#myInput').val();
    alert('You entered: ' + inputValue);
  });
});