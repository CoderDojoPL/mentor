$(document).ready(function() {
	$(".message-new").click(function () {
	    $(this).removeClass("message-new");
	});

	$("#registerForm").submit(function (event) {
		event.preventDefault();

		var output = $(this).serializeArray();

		//Umiejętności
		var skills = new Array();		
		$.each($(".skills input:checked"), function() {
		  skills.push($(this).val());
		});
		output.push(skills);

		//Dodatkowe
		var info = new Array();
		$.each($(".info input:checked"), function() {
		  info.push($(this).val());
		});
		output.push(info);

		console.log(output);
		$.post('0.0.0.0:4000/register',output);
	});
});