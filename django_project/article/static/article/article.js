/**
 * Created by ali on 3/14/15.
 */

$(document).ready(function() {
    $("#header-text, #header-posted, #header-subtext, #menu-toggle").css({opacity: 0});
    $(".latest-reviews").css({opacity: 0});
    $("header, footer").css({opacity: 0}).delay(500).fadeTo(1000, 1, function() {
        $("#menu-toggle").fadeTo(1000, 1);
        $("#header-text").fadeTo(500, 1, function () {
            $("#header-subtext").delay(500).fadeTo(500, 1, function() {
                $("#header-posted").fadeTo(500, 1);
            });
        });
        $(".latest-reviews").fadeTo(1000, 1);
    });
});