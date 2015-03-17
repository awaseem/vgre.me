/**
 * Created by ali on 3/14/15.
 */

$(document).ready(function() {
    $("#header-text, #header-posted, #header-subtext, #menu-toggle").css({opacity: 0});
    $("header, footer").css({opacity: 0}).delay(500).fadeTo(1000, 1, function() {
        $("#menu-toggle").fadeTo(1000, 1);
        $("#header-text").fadeTo(500, 1, function () {
            $("#header-subtext").delay(500).fadeTo(500, 1, function() {
                $("#header-posted").fadeTo(500, 1);
            });
        });
    });

  	//Check to see if the window is top if not then display button
	$(window).scroll(function(){
		if ($(this).scrollTop() > 350) {
			$('.top').fadeIn();
		} else {
			$('.top').fadeOut();
		}
	});

	//Click event to scroll to top
	$('.top').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});

});