$(document).ready(function() {
	$(".message-new").click(function () {
		$(this).fadeOut("slow", function() {
	    	$(this).removeClass("message-new");
	    });
	});
});