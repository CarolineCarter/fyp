function cal ( jQuery ) {
	console.log( "!" );

	$( "#add" ).click( function ( e ) {
		var arg1 = $( "#argument1" ).val();
		var arg2 = $( "#argument2" ).val();
		calculate (arg1, arg2, 'add');
		e.preventDefault();
	});

 	function calculate( arg1, arg2, resource ) {
		var textStatus, jqXHR, errorThrown = '';
		console.log( "Calling " + resource + " on " + arg1 + " and " + arg2 );
		try {
			arg1 = Number( arg1 );
			arg2 = Number( arg2 );
			
			if ( isNaN(arg1) || isNaN(arg2) ) throw "NaN";
			
			$.ajaxSetup({
				contentType: "application/json; charset=utf-8"
			});

		$.ajax({
			type: "POST",
			url: "http://172.17.0.21:8000/add",
			data: JSON.stringify({ argument1: arg1, argument2: arg2 }),
			dataType: "json",
			crossDomain : true,
		
        		//jsonp: 'callback',
			success: function ( data ) {
				var answer = String(data[ 'answer' ]);
			console.log( "answer! " + answer );

				$( "#argument1" ).val( answer );
				$( "#argument2" ).val( '' );
			},
			error: function ( textStatus, jqXHR, errorThrown ) {
			console.log("Something has gone wrong:" + errorThrown);
				$( "#argument1" ).val( '' );
				$( "#argument2" ).val( '' );
			}
		});
	}
		catch( err ) {
			console.log("Error: " + err);
			$( "#argument1" ).val( '' );
			$( "#argument2" ).val( '' );
		}
	}
}
