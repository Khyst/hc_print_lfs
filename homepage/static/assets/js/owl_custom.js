
$('.loop').owlCarousel({
    center: true,
    items:1,
    margin:0,
    autoplay: true,
    responsive:{ 
        1200:{
            items:5
        },
        992:{
            items:3,
            loop:true,
        },
        760:{
            items:2,
            loop:true,
        }
    }
});
    
$(".product_view").owlCarousel({
    center: true,
    items: 1,
    nav:false,
    loop:true,
    responsive:{
        1200:{
            items: 8,
        },
        992:{
            items:5,
        },
        760:{
            items:3
        }
    }
});