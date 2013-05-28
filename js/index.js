var loaded = false;
var bg = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.png", "6.jpg", "7.png", "8.png", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg", ];
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

	var r = Math.floor(Math.random()*bg.length);
	$('body').css('backgroundImage',"url('bg/" + bg[r] + "')");
});