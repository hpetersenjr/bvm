$(document).ready(function(){

	$("#aws_icon").click(function(){

		alert("you just clicked the aws icon");

	});

	$('#aws_icon').hover(

       function(){ $(this).addClass('hover') },
       function(){ $(this).removeClass('hover') }
 
	)
});