// JavaScript script that adds the class red to the <header>
// element when the user clicks on the tag DIV#red_header
const element = document.getElementById('toggle_header');
element.addEventListener('click', clikear);

function clikear () {
  $('header').toggleClass('red green');
}
