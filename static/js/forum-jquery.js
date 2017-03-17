$(document).ready(function(){
	$("a").hover(function(){
		$(this).animate({paddingLeft: '+=15px'}, 200);
		$(this).css({'font-size': '135%'});
	}, function(){
		$(this).animate({paddingLeft: '-=15px'}, 200);
		$(this).css({'font-size': '100%'});
	})
});