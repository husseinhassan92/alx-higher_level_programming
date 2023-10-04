$('document').ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $('#btn_translate').click(function () {
      $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
        $('#hello').html(data.hello);
      });
    });
  });