/* global instantsearch: true */
/*jshint camelcase: false */

$(document).ready(function () {


  $('.popup-trigger').on('click', function(e) {
    e.stopPropagation();
    $('body').append('<div class="algolia-pop-overlay">').css('overflow', 'hidden');
    $('body').append('<div class="local-search-pop-overlay">')
    $('.popup').toggle();
    $('#algolia-search-input').find('input').focus();
  });

  $('.popup-btn-close').click(function(){
    $('.popup').hide();
    $('.algolia-pop-overlay').remove();
    $('.local-search-pop-overlay').remove();
    $('body').css('overflow', '');
  });

});
