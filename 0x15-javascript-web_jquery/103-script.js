$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      $('#btn_translate').click();
    }
  });
});

