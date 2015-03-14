/**
 * Created by Ali Waseem on 3/13/15.
 */

$(document).ready(function() {
    $("header, footer").css({opacity: 0}).fadeTo(1000, 1);
    $(".latest-reviews").css({opacity: 0}).delay(1000).fadeTo(1000, 1);
    console.log($(window).height())
});