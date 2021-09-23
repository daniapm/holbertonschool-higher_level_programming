// JavaScript script that adds a <li> element to a list
//  when the user clicks on the tag DIV#add_item
let element = document.getElementById("add_item");
element.addEventListener("click", clikear);

function clikear() {
	$("UL.my_list").append("<li>Item</li>")
}
