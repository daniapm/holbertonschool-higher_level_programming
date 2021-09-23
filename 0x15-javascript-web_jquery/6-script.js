// JavaScript script that updates the text of the <header> element
// to New Header!!! when the user clicks on DIV#update_header
let element = document.getElementById("update_header");
element.addEventListener("click", clikear);

function clikear() {
	$("header").html("New Header!!!");
}
