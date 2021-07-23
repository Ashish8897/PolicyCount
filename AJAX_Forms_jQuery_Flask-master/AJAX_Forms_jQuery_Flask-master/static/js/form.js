$(document).ready(function() {

	$('form').on('submit', function(event) {
	var date1=$('#From').val();
	var a=String(date1);
	

		$.ajax({
			data : {
				name : $('#nameInput').val(),
				email : $('#emailInput').val()
                dat1:a;
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
				
			}

		});

		event.preventDefault();

	});

});