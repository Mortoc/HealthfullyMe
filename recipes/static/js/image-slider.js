

var __active_slider_image = 0;
var __slider_images = new Array();
var __fade_time = 300;

function __activate_slider_img(index) {
    $(__slider_images[__active_slider_image]).fadeOut(__fade_time);
    __active_slider_image = index;
    $(__slider_images[__active_slider_image]).fadeIn(__fade_time);
}

function __activate_next_img() {
    var next_idx = __active_slider_image + 1;
    if( next_idx >= __slider_images.length )
        next_idx = 0;
        
    __activate_slider_img(next_idx);
}

function setup_slider(container, view_duration){
    
    container.children().each(function(idx, img) {
        __slider_images.push( $(this) );
        $(this).hide();
    });
    
    __activate_slider_img(0);
    
    if( __slider_images.length > 1 )
        setInterval(__activate_next_img, view_duration);
}