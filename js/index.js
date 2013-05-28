var loaded = false;

$( function() {

  $(window).resize(function(){

    $('.main').css({
        position:'absolute',
        left: ($(window).width() - $('.main').outerWidth())/2,
        top: ($(window).height() - $('.main').outerHeight())/2
    });

    if (!loaded)
    {
    	loaded = true;
    	$(window).resize();
    }
  });
});


$(document).ready(function () {
	$(window).resize();
});