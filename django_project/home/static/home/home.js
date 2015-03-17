/**
 * Created by Ali Waseem on 3/13/15.
 */

$(document).ready(function() {

    $("#header-text, #header-bar, #header-subtext, #menu-toggle").css({opacity: 0});
    $(".latest-reviews").css({opacity: 0});
    $("header, footer").css({opacity: 0}).delay(500).fadeTo(1000, 1, function() {
        $("#menu-toggle").fadeTo(1000, 1);
        $("#header-text").fadeTo(500, 1, function () {
            $("#header-bar").fadeTo(500, 1);
            $("#header-subtext").delay(500).fadeTo(500, 1);
        });
    });

    $(window).on("scroll", function() {
        if ($(this).scrollTop() >= 200){
            $(".latest-reviews").fadeTo(1000, 1);
        }
    });
});