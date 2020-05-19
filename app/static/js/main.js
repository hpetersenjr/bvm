$(document).ready(function(){

	$("#navMenu").click(function() {

		$(this).parent().toggleClass("navFunctionC navFunctionR");
		$("nav").toggleClass("closed open");
		$(this).toggleClass("fa-bars fa-times");
		$("#navSelection").toggleClass("navSelectionClosed navSelectionOpen");

	});

});