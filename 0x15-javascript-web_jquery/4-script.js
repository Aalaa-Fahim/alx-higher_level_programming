// Toggles the class of HTML tag 'HEADER' when user clicks the
// div#toggle_header tag using the JQuery API

$('div#toggle_header').click(function () {
    $('header').ToggleClass('red');
  });
