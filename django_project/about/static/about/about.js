/**
 * Created by Ali Waseem on 3/21/15
 */

$(document).ready(function() {

    $("header, footer").delay(500).fadeTo(1000, 1, function() {
        $("#menu-toggle").fadeTo(1000, 1);
        $("#header-text").fadeTo(500, 1, function () {
            $("#header-bar").fadeTo(500, 1);
            $("#header-subtext").delay(500).fadeTo(500, 1);
        });
    });

    $(window).on("scroll", function(){
        if ($(this).scrollTop() >= 200) {
            $("#main-content").fadeTo(500, 1);
        }
    });
});