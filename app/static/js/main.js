$(document).ready(function() {
  // Toggle password visibility
  $('.fa-eye').on('click', function() {
    $(this).toggleClass('fa-eye-slash');

    if ($(this).hasClass('fa-eye-slash')) {
      $(this).prev().attr('type', 'text');
    }
    else {
      $(this).prev().attr('type', 'password');
    }
 });
});
