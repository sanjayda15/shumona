var scroll = new SmoothScroll('a[href*="#"]', {
speed: 1000
});


$('.js--fashion').waypoint(function(direction) {
       $('.js--fashion').addClass('animate__animated animate__fadeInUp');
   }, {
       offset: '100%'
   });

$('.js--product').waypoint(function(direction) {
    $('.js--product').addClass('animate__animated animate__fadeIn animate__slow');
}, {
    offset: '100%'
});

$('.js--card').waypoint(function(direction) {
       $('.js--card').addClass('animate__animated animate__fadeIn animate__slower');
   }, {
       offset: '100%'
   });

 if ($(window).width() < 992) {
     $('#hovers').addClass('phonenav text-center');
 } else {
     $('#hovers').removeClass('phonenav text-center');
 }

 if ($(window).width() < 992) {
     $('#navlist').addClass('text-center');
 } else {
     $('#navlist').removeClass('text-center');
}

 if ($(window).width() > 992) {
     $('#nave').addClass('mynav');
 } else {
     $('#nave').removeClass('mynav');
 }

 if ($(window).width() > 992) {
     $('#nave').addClass('navbar-dark');
     $('#nave').removeClass('navbar-light');
 } else {
     $('#nave').removeClass('navbar-dark');
     $('#nave').addClass('navbar-light');
 }
