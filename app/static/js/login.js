var dashData;

$(document).ready(function(){

	$("#passIcon").click(function() {

		$(this).toggleClass("fa-eye fa-eye-slash");

		if ($('#passfield').attr("type") == "password") {
			$('#passfield').attr("type", "text");
		} else {
			$('#passfield').attr("type", "password");
		}
		
	});

	$("#login").click(function( event ){

		if ( ! $('.login-form')[0].checkValidity() ) {
			$('.login-form')[0].reportValidity();
			return false;
		}

		event.preventDefault();
		//console.log("clicked");

		var jqxhr = $.post( "/login/", $('.login-form').serialize() , function() {
				//console.log( "connected" );
			})
			.done(function( data ) {

				var json = data;
				$.each(jQuery.parseJSON(json), function() {
				 	//console.log(this['status']);
				 	loginStatus = this['status']

				});

				if ( loginStatus == "Authentication_Failed" ) {

					$("#authFailed").remove();
					$(".form").append(" <div id='authFailed'><b>Authentication Failed</b></div>");

				} else {
				  
				  	$(".login-page").remove();
				  	$("#dashboard").show();
					//prep the initial dashboard layout


				}

			})
			.fail(function() {
				console.log( "error" );
			})
			.always(function() {
				$('.login-form').trigger("reset");
			});
	});

});