		
/*
$(document).ready(function() {
    $(".wholePage").css("display", "none");
    // branchStart();
    $(".wholePage").fadeIn(3000);
});
*/
		

// Tricky Android rotations see:
// 	http://stackoverflow.com/questions/1649086/detect-rotation-of-android-phone-in-the-browser-with-javascript
try {
    window.addEventListener("resize", pageOrientationChange, false);
    window.addEventListener("orientationchange", pageOrientationChange, false);
}
catch (err) {
    window.console && console.log("[Error] resize or orientationchange event listener problem: " + err.message);
}

// Run when the page is fully loaded including graphics, see: http://api.jquery.com/load-event/
// to fix the first time load that does not have the correct sizes
// NOT the most efficient
$(window).load(function () {
	var activePageId = null;
	if ($.mobile.activePage) {		// no active page while loading
		activePageId = $.mobile.activePage.attr('id');
	}
			
	if ((activePageId != null) && (activePageId == 'start-page')) {
		onStartPageShow();
	}
	else {
		onCertPagePageShow("window loaded");
	}
});

$('#cert-page').bind("pagebeforeshow", function (e, data) {
	// console.log("pagebeforeshow prev: " + data.prevPage + " to: " + data.toPage);

	// hide the tap to use button
	if ($('.card-front').visible) {         // 5/4/12 was not showing card when coming back from Add to iPhone
		// 7/30/12 $('.card-tap-to-use-class').css({ "left": "-9999px", "top": "500px" });
		$('.card-back').css({ "display": "none" });
    }
	$('.card-hidden-barcodes-class').css({ "display": "none" });        // Moved out of visible, it was showing - STC 6/19/12

	if (gDisallowMobileView == "True") {
	    $('.card-tap-to-use-class').css({ "display": "none" });
	} 
  }
);
