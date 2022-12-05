window.onscroll = function() { scrollWindow() };

function scrollWindow() {
	//check if scrolled at top of screen
	var navbar = document.getElementById('navbar');
	var mainBlock = document.getElementById('mainBlock');
	if (window.scrollY != 0) {
		navbar.classList.add("navbar_sticky")
		mainBlock.classList.add("scrolling_main")
	} else {
		navbar.classList.remove("navbar_sticky")
		mainBlock.classList.remove("scrolling_main")
	}
}
