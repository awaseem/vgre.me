/**
 * Created by ali on 3/14/15.
 */

$(document).ready(function() {

    $("header, footer").delay(500).fadeTo(500, 1, function() {
        $("#menu-toggle").fadeTo(500, 1);
        $("#header-text").fadeTo(250, 1, function () {
            $("#header-bar").fadeTo(250, 1);
            $("#header-subtext").delay(250).fadeTo(500, 1, function() {
                $("#search-bar").fadeTo(500, 1);
            });
        });
        $(".latest-reviews").fadeTo(500, 1);
    });
});