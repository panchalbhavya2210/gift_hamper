(function ($) {
"use strict";

/*--
	Menu Sticky
-----------------------------------*/
var windows = $(window);
var sticky = $('.header-bottom');
 
var headerHeight = $('.header-section').height();
var headerTop = $('.header-top').height();

$('#main-wrapper').css('padding-top', headerHeight );

windows.on('scroll', function() {
    var scroll = windows.scrollTop();
    if (scroll < headerTop) {
        sticky.removeClass('stick');
    }else{
        sticky.addClass('stick');
    }
});
/*-- Menu Sticky In Windows Resize --*/
windows.on('resize', function(){
    var headerHeight = $('.header-section').height();
    var headerTop = $('.header-top').height();
    
    $('#main-wrapper').css('padding-top', headerHeight );

    windows.on('scroll', function() {
        var scroll = windows.scrollTop();
        if (scroll < headerTop) {
            sticky.removeClass('stick');
        }else{
            sticky.addClass('stick');
        }
    });
});
    

/*--
	Mobile Menu
------------------------*/
$('#main-menu').meanmenu({
    meanScreenWidth: '767',
    meanMenuContainer: '.mobile-menu',
    meanMenuClose: '<i class="ion-android-close"></i>',
    meanMenuOpen: '<i class="ion-navicon"></i>',
    meanRevealPosition: 'left',
    meanMenuCloseSize: '30px',
});

    
/*-- 
    Search Toggle
-----------------------------------*/
var headerSearchForm = $('.header-search-form');
var searchToggle = $('.search-toggle');
searchToggle.on('click', function(){
    if( headerSearchForm.hasClass('open') ) {
        headerSearchForm.removeClass('open');
        $(this).html('<i class="ion-ios-search-strong"></i>');
    }else{
        headerSearchForm.addClass('open');
        $(this).html('<i class="ion-android-close"></i>');
    }
});
    
/*-- 
    Checkout Login/Register Form Toggle
-----------------------------------*/
var checkoutMethodList = $('.checkout-method-list li');
checkoutMethodList.on('click', function(){
    var form = $(this).data('form');
    if( !$(this).hasClass('active') ) {
        $('.checkout-method-list li').removeClass('active');
        $(this).addClass('active');
        $('.checkout-method form').slideUp(500);
        $('.' + form).delay(500).slideDown();
    }
});

/*-- 
    Checkout Shipping Form Toggle
-----------------------------------*/
var shipingFormToggle = $('.shipping-form-toggle');
var shipingForm = $('.shipping-form');
shipingFormToggle.on('click', function(){
    if( $(this).hasClass('active') ) {
        $(this).removeClass('active');
        shipingForm.slideUp();
    } else {
        $(this).addClass('active');
        shipingForm.slideDown();
    }
});
    
/*-- 
    Payment Method Toggle
-----------------------------------*/
var paymentMethodList = $('.payment-method-list li');
var paymentFormToggle = $('.payment-form-toggle');
var paymentForm = $('.payment-form');
paymentMethodList.on('click', function(){
    paymentMethodList.removeClass('active');
    $(this).addClass('active');
    if( $(this).hasClass('payment-form-toggle') ) {
        paymentForm.slideDown()
    } else {
        paymentForm.slideUp()
    }
});

/*--
	Hero Slider
-----------------------------------*/
$('.hero-slider').slick({
    arrows: false,
    autoplay: false,
    dots: true,
    fade: true,
    infinite: true,
    slidesToShow: 1,
});
    
/*--
	Testimonial Slider
-----------------------------------*/
$('.testimonial-slider').slick({
    arrows: false,
    autoplay: false,
    dots: true,
    infinite: true,
    slidesToShow: 1,
});
    
/*--
	Client Slider
-----------------------------------*/
$('.client-slider').slick({
    arrows: false,
    autoplay: true,
    infinite: true,
    slidesToShow: 5,
    slidesToScroll: 1,
    responsive: [
        {
          breakpoint: 991,
          settings: {
            slidesToShow: 4,
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 350,
          settings: {
            slidesToShow: 2,
          }
        }
    ]
});
    
/*--
	Single Product Thubmnail & Image Slider
-----------------------------------*/
$('.product-thumbnail-slider').slick({
    autoplay: false,
    infinite: true,
    vertical: true,
    centerMode: true,
    centerPadding: '0px',
    focusOnSelect: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.product-image-slider',
    prevArrow: '<button type="button" class="slick-prev"><i class="fa fa-angle-up"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="fa fa-angle-down"></i></button>',
});
    
$('.product-image-slider').slick({
    arrows: false,
    autoplay: false,
    infinite: true,
    slidesToShow: 1,
    asNavFor: '.product-thumbnail-slider',
});

/*--
	Counter UP
-----------------------------------*/
$('.counter').counterUp({
    delay: 20,
    time: 3000
});

/*--
	Scroll Up
-----------------------------------*/
$.scrollUp({
	easingType: 'linear',
	scrollSpeed: 900,
	animation: 'fade',
	scrollText: '<i class="fa fa-angle-up"></i>',
});

/*----- 
	Cart Plus Minus
--------------------------------*/
$('.product-quantity').prepend('<span class="dec qtybtn"><i class="fa fa-angle-left"></i></span>');
$('.product-quantity').append('<span class="inc qtybtn"><i class="fa fa-angle-right"></i></span>');
$('.qtybtn').on('click', function() {
	var $button = $(this);
	var oldValue = $button.parent().find('input').val();
	if ($button.hasClass('inc')) {
	  var newVal = parseFloat(oldValue) + 1;
	} else {
	   // Don't allow decrementing below zero
	  if (oldValue > 0) {
		var newVal = parseFloat(oldValue) - 1;
		} else {
		newVal = 0;
	  }
	  }
	$button.parent().find('input').val(newVal);
});
    
/*--
    Magnific Video Popup
--------------------------------*/
var videoPopup = $('.video-popup');
videoPopup.magnificPopup({
	type: 'iframe',
	mainClass: 'mfp-fade',
	removalDelay: 160,
	preloader: false,
	zoom: {
		enabled: true,
	}
});



})(jQuery);	