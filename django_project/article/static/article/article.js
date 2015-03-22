/**
 * Created by ali on 3/14/15.
 */

$(document).ready(function() {
    $("header, footer").delay(500).fadeTo(1000, 1, function() {
        $("#menu-toggle").fadeTo(1000, 1);
        $("#header-text").fadeTo(500, 1, function () {
            $("#header-subtext").delay(500).fadeTo(500, 1, function() {
                $("#header-posted").fadeTo(500, 1);
            });
        });
    });

  	//Check to find scrolling to display button/text
	$(window).scroll(function(){
		if ($(this).scrollTop() > 350) {
			$('.top').fadeIn();
            $("#main-content").fadeTo(500, 1);
		} else {
			$('.top').fadeOut();
		}
	});

	//Click event to scroll to top
	$('.top').click(function() {
		$('html, body').animate({scrollTop : 0},800);
	});

});