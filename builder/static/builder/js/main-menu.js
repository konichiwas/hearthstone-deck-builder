var $header= $('header');

$header.find('.js-burger-button').on('click', function(){
	$header.toggleClass('open');
});