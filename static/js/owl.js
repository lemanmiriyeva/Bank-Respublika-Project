$(document).ready(function() {
    // $('.largecarousel').owlCarousel({
    //     loop: true,
    //     margin: 10,
    //     nav: true,

    //     responsive: {
    //         1000: {
    //             items: 1,
    //             // loop: false
    //         }
    //     }
    // })
    $('.carouselMehsul').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        responsive: {
            // 0: {
            //     items: 1
            // },
            // 600: {
            //     items: 3
            // },
            1000: {
                items: 4,
                loop: false
            }
        }
    })


    $('.subCarousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        dots: false,
        navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
        responsive: {

            1000: {
                items: 1,
                loop: false

            }
        }
    })

    $('.carouselXeber').owlCarousel({
        loop: true,
        padding: 50,
        nav: false,
        center: true,
        dots: false,
        responsive: {

            1000: {
                items: 3
            }
        }
    })
})