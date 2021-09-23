// JavaScript script that updates the text color of the
// <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:
let element = document.getElementById("red_header");
element.addEventListener("click", clikear);

function clikear() {
      document.getElementById("red_header").style.color= "red";
}
