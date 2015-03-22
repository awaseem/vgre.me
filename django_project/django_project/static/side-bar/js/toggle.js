/**
 * Created by ali on 3/22/15.
 */
$(document).ready(function() {
    $("#menu-toggle").click(function(e) {
            e.preventDefault();
            $("#wrapper").toggleClass("toggled");
    });
});