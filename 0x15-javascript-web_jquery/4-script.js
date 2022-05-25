$('DIV#toggle_header').click(function () {
  const color = $('header').hasClass('red');
  if (!color) {
    $('header').toggleClass('red');
  } else {
    $('header').toggleClass('green');
  }
});
