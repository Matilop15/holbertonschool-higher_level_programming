$('DIV#toggle_header').click(function() {
    var color = $("header").hasClass("red");
    if (!color) {
        $("header").toggleClass("red");
    }
    else {
        $("header").toggleClass("green");
    }
});