$('document').ready(function () {
    $('#add_item').click(function () {
      $('UL.my_list').append($('<li></li>').text('Item'));
    });
    $('#remove_item').click(function () {
      $('UL.my_list li:last').remove();
    });
    $('#clear_list').click(function () {
      $('UL.my_list').empty();
    });
  });