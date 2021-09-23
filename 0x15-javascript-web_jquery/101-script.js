//  JavaScript script that adds, removes and 
//  clears LI elements from a list when the user clicks:
$(function () {
	let element = document.getElementById("add_item");
	element.addEventListener("click", clikear);

function clikear() {
	$("UL.my_list").append("<li>Item</li>")
}
});
$(function () {
	let element = document.getElementById("remove_item");
	element.addEventListener("click", clikear);

	function clikear() {
		let list = $('ul.my_list li');
      	list[list.length - 1].remove();
	}
});
$(function () {
	let element = document.getElementById("clear_list");
	element.addEventListener("click", clikear);

	function clikear() {
		$("UL.my_list").empty();
	}
});
