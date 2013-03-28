gIsFrontLoaded = false;
gIsBackLoaded = false;
gIsFront = true;

// show objects hidden for no JavaScript
$(".no_javascript_hide_objects").show(); 	//.css({"display:block;"});		
//  Listen for any attempts to call changePage() and
//	show/hide splash page when coming from outside Jquery Mobile page
//	Replaces branchStart()
//
$(document).bind("pagebeforechange", function (e, data) {
    // no $('#cert-page').bind("pagebeforechange", function( e, data ) {
    // console.log("pagebeforechange prev: " + data.prevPage + " to: " + data.toPage);
    var showSplash = shouldShowSplash();
    var activePageId = null;
    var toPageId = null;
    if ($.mobile.activePage) {		// no active page while loading
        activePageId = $.mobile.activePage.attr('id');
        // console.log("  active page: " + activePageId);
    }
    loadColors(); 		// <--- load the gradient colors
    if (activePageId == null) {
        // We only want to handle changePage() calls where the caller is
        // asking us to load a page by URL.
        if (typeof data.toPage === "string") {
        }
        else {
            if (data.toPage) {
                toPageId = data.toPage.attr('id');
                // console.log("  toPageId: " + toPageId);
            }
            if (showSplash) {
                // console.log("  show splash");
                if ((toPageId != null) && (toPageId != 'start-page')) {
                    // Show Splash
                    //data.toPage = '#start-page';
                    // e.preventDefault()
                    data.options.transition = "none";
                    data.options.changeHash = false;
                    data.options.reverse = true;
                    data.toPage = '#start-page';
                    // data.deferred.resolve(data.toPage, data.options);
                }
            }
            else {
                // console.log("  no splash");
                if ((toPageId == null) || (toPageId != 'cert-page')) {
                    // No Splash
                    // data.toPage = '#cert-page';
                    //e.preventDefault()
                    data.options.transition = "none";
                    data.options.changeHash = false;
                    data.toPage = '#cert-page';
                    // data.deferred.resolve(data.toPage, data.options);
                }
            }
        }
    }
    /*
			else {
				// if going back to the splash, there is a double back jump back another
				if ((activePageId) && (activePageId == 'cert-page')) {
					if ( typeof data.toPage === "string" ) {
						toPageId = data.toPage;
					}
					else {
						if (data.toPage) {
							toPageId = data.toPage.attr('id');
							console.log("  toPageId: " + toPageId);
						 }
					}
					if ((toPageId) && (toPageId == 'cert-page')) {
						// if going to and from cert-page, go back 
						
					}
				}
			}
			*/
});

/* If want to set by device...
		if (isAndroid()) {
			<!--  Android - no zooming at all. Mess on out, basic Jquery Mobile tables mess up on zoom in then rotate -->
			$('head').append('<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;">');
		}
		else {
			$('head').append('<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=2.0; minimum-scale=1.0;">');
		}
		*/
// Put in main aspx file
// 	var gShowSplashPage = "<%=this.shouldShowSplashScreen%>";
function shouldShowSplash() {
    var showSplashPage = true;
    var splashInUrl = $(document).getUrlParam("splash");
    if (splashInUrl) {
        // from Url parameter
        if (splashInUrl == "no") {
            showSplashPage = false;
        }
        else {
            showSplashPage = true;
        }
    }
    else {
        // from db
        if (gShowSplashPage == "True") {
            showSplashPage = true;
        }
        else {
            showSplashPage = false;
        }
    }
    return (showSplashPage);
}
/*
		function branchStart() {
			
			var splashInUrl = shouldShowSplash();
			
			var activePageId = null;
			if ($.mobile.activePage) {		// no active page while loading
				activePageId = $.mobile.activePage.attr('id');
			}
			
			if (showSplashPage) {
				// only need to change if not the initial load
				if ((activePageId != null) && (activePageId != 'start-page') ||
					(activePageId == null))  {
					window.location = '#start-page';
				}
			}
			else {
				// need to skip to cert-page if no splash initially OR later
				if ((activePageId == null) || (activePageId != 'cert-page')) {
					window.location = '#cert-page';
				}
			}
		}
		*/

// ------------------------------------------------------------------------
//	Start Page
//
// based on http://stackoverflow.com/questions/318630/get-real-image-width-and-height-with-javascript-in-safari-chrome
//
function LoadImage(imgSrc, callback) {
    var image = new Image();
    image.src = imgSrc;
    if (image.complete) {
        callback(image);
        image.onload = function () { };
    } else {
        image.onload = function () {
            callback(image);
            // clear onLoad, IE behaves erratically with animated gifs otherwise
            image.onload = function () { };
        }
        image.onerror = function () {
            // alert("Could not load image.");
            callback(null);
        }
    }
    return (image);
}
// Async callback on image load
// because logo.height is not valid until loaded 
//
function centerImageOnPage(anImage) {
    // $(window).height();   // returns height of browser viewport
    // $(document).height(); // returns height of HTML document
    // console.log("CenterImageOnPage window:" + $(window).height() + " doc:" + $(document).height());
    // fit the start page to the viewport
    // does not work $(document).height($(window).height());
    // 2 gradients in table with logo in middle
    var darkColor = gDarkColor; 	// "<%=colors.PASSDarkColor%>" in Subscribe was $("#darkColor").val();
    // var topGradient = "-webkit-gradient(linear, left top, left bottom, from(" + darkColor + "), to(#FFF))";		
    // var bottomGradient = "-webkit-gradient(linear, left top, left bottom, from(#FFF), to(" + darkColor + "))";
    buildCrossPlatformCssGradient($(".start-page-top-class"), darkColor, "#FFFFFF");
    buildCrossPlatformCssGradient($(".start-page-bottom-class"), "#FFFFFF", darkColor);
    // gradient - dark to white to dark
    // var backGradient = "-webkit-gradient(linear, left top, left bottom, from(" + darkColor + "), color-stop(0.33, #FFF), color-stop(0.66, #FFF), to(" + darkColor + "))";
    // 
    // Window fits better, but document is more reliable on rotate
    // because you don't fill and leave bands on the bottom.
    var imageHeight = 4;
    if (anImage) {
        imageHeight = anImage.height(); 	// as JS object image.Height; 			// do not want an error if no image
    }
    if (imageHeight < 10) {     // added to avoid the large gradient shifting on load
       imageHeight = 50;
    }

    // pre 7/6/12 useAvailHeight was just  $(document).height()
    var useAvailHeight;
    var isSample = false;
    var sampleInUrl = $(document).getUrlParam("sample");
    if ($.isArray(sampleInUrl))  {
        sampleInUrl = sampleInUrl[0];
    }
    if (sampleInUrl) {
        // from Url parameter
        if (sampleInUrl== "true") {
            isSample = true;
        }
    }
    if (isSample) {
        useAvailHeight = 450;          // sample fixed height (was 424 pre 8/17/12)
    }
    else {
        useAvailHeight = window.innerHeight ? window.innerHeight : $(window).height();  // too short iOS4  $(window).height();    // 1/23/13 Windows 8 - screen.availHeight;
        /* 1/23/13
        if (isiPhone()) {       // using screen.availHeight, not $(document).height() Android does not have the bottom - 7/17/12 
            useAvailHeight = useAvailHeight - 44;
        }
        */
    }

    // window.console && console.log("logo height: " + imageHeight + " doc height: " + useAvailHeight);

    gradientHeight = (useAvailHeight - imageHeight) / 2;
    var topGradientHeight = gradientHeight;            // 24 shift logo higher - 7/6/12
    var bottomGradientHeight = gradientHeight;
    $(".start-page-top-class").css({ height: topGradientHeight });
    $(".start-page-bottom-class").css({ height: bottomGradientHeight });
    // *** Watch loading the card page ***
    $(".ui-loader").css({ top: "80%" });
    $.mobile.showPageLoadingMsg("b", "loading...", false);
    setTimeout("showCertPage()", 3000); 		// 3 seconds later
    // old updateCertPageInfo();
}
function showCertPage() {
    $.mobile.changePage('#cert-page', { transition: 'fade' }); // 'slide'});
}
function onStartPageShow() {
    var logoImage = $('#start-page-logo-image'); // document.getElementById('start-page-logo-image');
    if (logoImage) {
        centerImageOnPage(logoImage);
    }
}
// ------------------------------------------------------------------------
//	Cert Page
//
function onCertPagePageShow(fromStr) {
    // console.log("onCertPagePageShow " + fromStr);
    // 5/7/12 $.mobile.hidePageLoadingMsg(); 		// because the splash may not be shown
    
    // Note that jQuery does not support getting the position coordinates of hidden elements.
    //
    var updatePlacement = true;
    var tapImage = $('#card-tap-to-use-image');
    var tapImageSize = tapImage.width();
    if (tapImageSize <= 0) {
        // could be the back of the card..
        tapImage = $('#card-tap-if-done-image');
        tapImageSize = tapImage.width();
        if (tapImageSize <= 0) {
            // card-tap-to-use-image AND card-tap-if-done-image not loaded yet...this should get called again when loading is finished
            // console.log("Do not update, no image sizes.");
            updatePlacement = false;
        }
        else {
            // back of card
        }
    }
    
    if (updatePlacement) {

        iPhone = false;
        android = false;

        try {
            // if both lblGiftCardNumber and lblPartnerCertId add a <br>
            var lblGiftCardNumber = $('#lblGiftCardNumber');
            var lblPartnerCertId = $('#lblPartnerCertId');
            if ((lblGiftCardNumber) && (lblPartnerCertId)) {
                if ((lblGiftCardNumber.text().length > 0) && (lblPartnerCertId.text().length > 0)) {
                    $('.cert-page-cardnumber-w-partner-class').css({ "display": "block" });
                }
            }
        }
        catch (err) {
            window.console && console.log("[Error] onCertPagePageShow lblGiftCardNumber: " + err.message);
        }

        try {
            // Message - To/From
            //		if no text in the message, to, and from then hide the message section.
            var shouldHideMessage = true;
            var msgText = $('#personalMessage').text();
            if (msgText) {
                msgText = msgText.trim();
                if (msgText.length > 0) {
                    shouldHideMessage = false;
                }
            }
            if (shouldHideMessage) {
                var fromText = $("#personalMessageFrom").text();
                if (fromText) {
                    fromText = fromText.trim();
                    if (fromText.length > 0) {
                        shouldHideMessage = false;
                    }
                }
            }
            if (shouldHideMessage) {
                var toText = $("#personalMessageTo").text();
                if (toText) {
                    toText = toText.trim();
                    if (toText.length > 0) {
                        shouldHideMessage = false;
                    }
                }
            }
            if (shouldHideMessage) {
                $('#litCustomMsg-section').hide();
            }
            else {
                $('#litCustomMsg-section').show();
            }
        }
        catch (err) {
            window.console && console.log("[Error] onCertPagePageShow litCustomMsg-section: " + err.message);
        }

        try {
            // Instructions - convert /r/n to <br> or <p>
            //
            var hideTermsInstrSection = true;
            var hide_textOnlyInstructionsLi = true;
            var hide_textOnlyTermsLi = true;
            var hide_htmlInstructionsLi = true;
            var hide_htmlTermsLi = true;
            //
            var rawInstructionText = $('.gift-instructions').html();
            var htmlInstructions = convertCrLftoBR(rawInstructionText);
            $('.gift-instructions').html(htmlInstructions);
            if (htmlInstructions) {
                htmlInstructions = htmlInstructions.trim();
                if (htmlInstructions.length > 0) {
                    hideTermsInstrSection = false;
                    hide_textOnlyInstructionsLi = false;
                }
            }
            // Terms and Conditions - convert /r/n to <br> or <p>
            //
            var rawTermsText = $('.gift-terms').html();
            var htmlTerms = convertCrLftoBR(rawTermsText);
            $('.gift-terms').html(htmlTerms);
            if (htmlTerms) {
                htmlTerms = htmlTerms.trim();
                if (htmlTerms.length > 0) {
                    hideTermsInstrSection = false;
                    hide_textOnlyTermsLi = false;
                }
            }
            if (hideTermsInstrSection) {
                // product page can also use Html htmlInstructionsLi or htmlTermsLi
                var checkHtml = $('#htmlInstructionsLi').html();
                if (checkHtml) {
                    checkHtml = checkHtml.trim();
                    if (checkHtml.length > 0) {
                        hideTermsInstrSection = false;
                        hide_htmlInstructionsLi = false; 
                    }
                }
            }
            if (hideTermsInstrSection) {
                // product page can also use Html htmlInstructionsLi or htmlTermsLi
                var checkHtml = $('#htmlTermsLi').html();
                if (checkHtml) {
                    checkHtml = checkHtml.trim();
                    if (checkHtml.length > 0) {
                        hideTermsInstrSection = false;
                        hide_htmlTermsLi = false;
                    }
                }
            }
            if (hideTermsInstrSection) {
                $('#termsInstructionSectionId').hide();     // hide the whole section
            }
            else {
                // add partial hide - 6/19/22
                if (hide_textOnlyInstructionsLi) {
                    $('#textOnlyInstructionsLi').hide();        // hide the line
                }
                else {
                    // if textOnlyInstructionsLi is the ONLY item in this section, then need to add bottom corners - 7/10/12
                    if (hide_textOnlyTermsLi && hide_htmlInstructionsLi && hide_htmlTermsLi) {
                        $('#textOnlyInstructionsLi').addClass('ui-corner-bottom');
                    }
                }

                if (hide_textOnlyTermsLi) {
                    $('#textOnlyTermsLi').hide();
                }
                else {
                    // if textOnlyTermsLi is the FIRST item in this section, then need to add top corners - 7/10/12
                    if (hide_textOnlyInstructionsLi) {
                        $('#textOnlyTermsLi').addClass('ui-corner-top');
                    }
                    // if textOnlyTermsLi is the LAST item in this section, then need to add bottom corners - 7/11/12
                    if (hide_htmlInstructionsLi && hide_htmlTermsLi) {
                        $('#textOnlyTermsLi').addClass('ui-corner-bottom');
                    }
                }

                if (hide_htmlInstructionsLi) {
                    $('#htmlInstructionsLi').hide();
                }
                else {
                    // if htmlInstructionsLi is the FIRST item in this section, then need to add top corners - 7/10/12
                    if (hide_textOnlyInstructionsLi && hide_textOnlyTermsLi) {
                        $('#htmlInstructionsLi').addClass('ui-corner-top');
                    }
                    // if htmlInstructionsLi is the LAST item in this section, then need to add bottom corners - 7/11/12
                    if (hide_htmlTermsLi) {
                        $('#htmlInstructionsLi').addClass('ui-corner-bottom');
                    }
                }

                if (hide_htmlTermsLi) {
                    $('#htmlTermsLi').hide();
                }
                else {
                    // if htmlTermsLiis the FIRST item in this section, then need to add top corners - 7/10/12
                    if (hide_textOnlyInstructionsLi && hide_textOnlyTermsLi && hide_htmlInstructionsLi) {
                        $('#htmlTermsLi').addClass('ui-corner-top');
                    }
                }
            }
        }
        catch (err) {
            window.console && console.log("[Error] onCertPagePageShow termsInstructionSectionId: " + err.message);
        }

        UpdatePlacementOnCard(true, tapImageSize);     // true to injectObjectsToBack - broken out 5/4/12

    } 	// updatePlacement
}

function UpdatePlacementOnCard(injectObjectsToBack, tapImageSize) {
    try {
        // dynamically duplicate back of card fields, because ASP 
        //						
        var hasBarcode = true;
        var imgCertBarCode = $('#imgCertBarCode');
        if ((imgCertBarCode) && (imgCertBarCode.size() > 0)) {
            // console.log("Barcode = imgCertBarCode");
        }
        else {
            imgCertBarCode = $('#imgCertBarCodeVCardTop');
            if ((imgCertBarCode) && (imgCertBarCode.size() > 0)) {
                // console.log("Barcode = imgCertBarCodeVCardTop");
            }
            else {
                imgCertBarCode = $('#imgCertBarCodeVCardBelow');
                if ((imgCertBarCode) && (imgCertBarCode.size() > 0)) {
                    // console.log("Barcode = imgCertBarCodeVCardBelow");
                }
                else {
                    hasBarcode = false;
                    // console.log("No Barcode");
                }
            }
        }
        // console.dir(imgCertBarCode);
        // inject COPIES of the objects into the HTML
        //
        $('.inject-barcode-back-class').html(""); 		// clear old image injection
        $('.inject-key-back-class').html(""); 			// clear old key injection
        if (hasBarcode) {
            var barcodeCopy = imgCertBarCode.clone();
            var barcodeLink = $("<a href='' onClick='showCardFront(2)'></a>");
            barcodeCopy.addClass("inject-barcode-back-image-class");       // barcode too wide bug - set the max-width for barcode image, Staging 'Mort - 7/26/12
            barcodeCopy.appendTo(barcodeLink);
            $('.inject-barcode-back-class').html(barcodeLink);
        }
        else {
            var keyCopy = $('.gift-key').clone();
            $('.inject-key-back-class').html(keyCopy.html());
        }
        $('.inject-pin-back-class').html(""); 		// clear old injection
        var pinHtml = $('.gift-pin').html(); 		// using html will not carry .gift-pin, like var pinCopy = $('.gift-pin').clone();
        $('.inject-pin-back-class').html(pinHtml);

        //
        //	Placement
        //
        var frontImage = $('#giftCardImage');
        var backImage = $('#backCardEmptyImage');
        var showingImage;
        var showingImageOffset;
        var imageHeight;
        var imageWidth;
        // var tmp = frontImage.attr("src");
        if ((frontImage) && (frontImage.height() > 30)) {			// missing images will be small
            showingImage = frontImage;
        }
        else {
            if ((backImage) && (backImage.width() > 30)) {
                // back of card
                showingImage = backImage;
            }
            else {
                showingImage = null;
                window.console && console.log("Warning - No front or back image ");
            }
        }
        if (showingImage) {
            showingImageOffset = showingImage.position();
            imageHeight = showingImage.height();
            imageWidth = showingImage.width();
        }
        if ((!showingImage) || (imageHeight < 50)) {			// missing images will be small
            // no valid image - show as white square
            showingImage = $("#divVCardWithGraphic"); 		// Watch Div, not image
            showingImageOffset = showingImage.position();
            if (!showingImageOffset) {
                // null
                showingImageOffset = "270 208";
            }
            imageHeight = showingImage.height();
            imageWidth = showingImage.width() - 10.0;
            // debug $('.card-wrapper-class').css({"background-color":"#FF0"});
        }
        var left = showingImageOffset.left + imageWidth - (tapImageSize / 2);
        var top = showingImageOffset.top + imageHeight - (tapImageSize / 2);
        if (left > 0) {				// iPhone coming through with negative values first, so skip it if bad placement
            // 7/30/12 $(".card-tap-to-use-class").css({ "position": "absolute", "left": left, "top": top });
            // 7/30/12 $(".card-tap-if-done-class").css({ "position": "absolute", "left": left, "top": top });
        }
        // Uncomment and load on device to get initial placement without jumping around
        // alert("Default placement: " + left + ", " + top);
        // Place with absolute positioning over the back card image
        //
        var fillWidth = imageWidth * 0.90; 		// fill 90% for the gray edges
        left = showingImageOffset.left + ((imageWidth * 0.10) / 2);
        // should be adding fontHeight, looks bad on iPhone
        top = showingImageOffset.top + (imageHeight * 0.08); // 8% down from the top
        // no longer used 7/31/12 $('.back-table-class').css({ "top": top, "left": left, "width": fillWidth });      
        if (hasBarcode) {
            // show barcode
            $('.inject-barcode-back-class').css({ "display": "block"});       
            // hide key
            $(".inject-key-back-class").css({ "display": "none" });
        }
        else {
            // hide barcode
            $('.inject-barcode-back-class').css({ "display": "none" });
            // show key
            // Need  better way to resize products...
            // var lineCnt = $('.inject-key-back-class br').length;
            // if (lineCnt <= 1) {
                $('.inject-key-back-class').textfillStcSingleLine(70, (fillWidth), 65);
            
            $('#lblPartnerCertIdSpan').textfillStcSingleLine(70, (fillWidth), 65);             // problem with added Partner Cert, this resizes the FIRST one
        }
        // barcode full width test
        var limitHeight = imageHeight / 3;
        $('#imgCertBarCodeVCardBelow').css({ "left": left, "width": (fillWidth - 40), "max-height": limitHeight });
    }
    catch (err) {
        window.console && console.log("[Error] onCertPagePageShow placement: " + err.message);
    }
}

function showCardFront(sourceOfClick) {
    if (gDisallowMobileView == "True") {
        // mobile view not allowed, do not show bar code flip buttons
        $('.card-front').show();
        $('.card-tap-to-use-class').hide();
        $('.card-back').hide();
        $('.card-tap-if-done-class').hide();
    }
    else {
        // show front buttons
        $('.card-front').show();
        $('.card-tap-to-use-class').show();
        $('.card-back').hide();
        $('.card-tap-if-done-class').hide();
    }
}
function showCardBack(sourceOfClick) {
    if (gDisallowMobileView == "True") {
        // mobile view not allowed, do not show bar code flip buttons
        $('.card-front').show();
        $('.card-tap-to-use-class').hide();
        $('.card-back').hide();
        $('.card-tap-if-done-class').hide();
    }
    else {
        // show back buttons
        $('.card-back').show();
        $('.card-tap-if-done-class').show();
        $('.card-front').hide();
        $('.card-tap-to-use-class').hide();

        tapImage = $('#card-tap-if-done-image');    // added 5/4/12
        tapImageSize = tapImage.width();            // added 5/4/12
        UpdatePlacementOnCard(false, tapImageSize);               // added 5/4/12
    }
}
function useCertCard() {
    var titleStr = $("merchantName")
}
// ------------------------------------------------------------------------
var gPreviousOrientation = 0;
var gPreviousWidth = 0;
//
// Tricky Android rotation:
// 	http://stackoverflow.com/questions/1649086/detect-rotation-of-android-phone-in-the-browser-with-javascript
//		
function pageOrientationChange() {		// (orientation) {
    // console.log("start page OrientationChange");

    var activePageId;
    if ($.mobile.activePage) {
        activePageId = $.mobile.activePage.attr('id');
    }
    else {
        activePageId = 0;
    }
    // used to have orientation property equal to either "portrait" or "landscape", but only worked on iPhone
    //
    if ((window.orientation != gPreviousOrientation) || (window.innerWidth != gPreviousWidth)) {
        var needFullReload = false;
        /* locked down Android
				if (window.orientation != gPreviousOrientation) {
					if (isAndroid()) {
						needFullReload = true;
					}
				}
				*/
        gPreviousOrientation = window.orientation;
        gPreviousWidth = window.innerWidth; 	// use window.innerWidth to catch zooms, not screen.width;
        // orientation changed, do your magic here	
        // alert('Orientation:' + window.orientation + "  gPreviousOrientation:" + gPreviousOrientation + "  width: " + screen.width);
        if (activePageId == 'start-page') {
            logoImage = $('#start-page-logo-image'); // document.getElementById('start-page-logo-image');
            if (logoImage) {
                centerImageOnPage(logoImage);
            }
        }
        // can be resized anywhere!
        onCertPagePageShow("pageOrientationChange");
    }
}

// ------------------------------------------------------------------------
//	Glue for Add to Wallet
//
var gWalletDevice;
function goto_wallet_page(forDevice) {
    // android or ios
    gWalletDevice = forDevice;

    var destUrlStr = '/Cert/T2/AddCardRoundhouse.aspx';
    var bcnId = $(document).getUrlParam("BCNID");
    if ((bcnId != null) && (bcnId.length > 0)) {
        destUrlStr = destUrlStr + "?BCNID=" + bcnId;
    }
    // $.mobile.changePage(destUrlStr, { transition: 'slide', data-ajax: "false" });     // '#wallet-page'
    window.location.href = destUrlStr;
}

// ------------------------------------------------------------------------

// use built in confirm to have Cancel button
function okDialog(withStr) {
    if (true) {
        alert(withStr);
    }
    else {
        $('#ok-dialog-text').html(withStr);
        $.mobile.changePage('#ok-dialog', { transition: 'pop', role: 'dialog' });
    }
}

// Add to main page:
//	var gDarkColor = "<%=colors.PASSDarkColor%>";
//	var gMediumColor = "<%=colors.PASSMediumColor%>";
//	var gLightColor = "<%=colors.PASSLightColor%>";
//
function loadColors() {
    var darkColor = gDarkColor;
    if ((!darkColor) || (darkColor == "")) {
        darkColor = "#000000";
    }
    var mediumColor = gMediumColor;
    if ((!mediumColor) || (mediumColor == "")) {
        mediumColor = "#666666";
    }
    var lightColor = gLightColor;
    if ((!lightColor) || (lightColor == "")) {
        lightColor = "#DDDDDD";
    }
    var lighterDark = new Color(darkColor);
    lighterDark = lighterDark.getLighter();
    lighterDark = lighterDark.getLighter();
    // var darkGradient = "-webkit-gradient(linear, left top, left bottom, from(" + lighterDark + "), to(" + darkColor + "))";
    var darkGradientMap = buildCrossPlatformCssGradient($(".giftango-header"), lighterDark, darkColor);
    var lighterMedium = new Color(mediumColor);
    lighterMedium = lighterMedium.getLighter();
    //var mediumGradient = "-webkit-gradient(linear, left top, left bottom, from(" + lighterMedium + "), to(" + mediumColor + "))";
    var mediumGradientMap = buildCrossPlatformCssGradient($(".giftango-button"), lighterMedium, mediumColor);
    // override the colors on the css for custom colors
    textShadow = lightColor + " 0px -1px 1px";
    // gradients
    // $(".giftango-header").css(darkGradientMap);
    // $(".giftango-button").css(mediumGradientMap);
    // $(".giftango-header").css({"background": darkGradient, color:"#FFF"});
    // $(".giftango-button").css({"background": mediumGradient, "color":"white"});
    $(".main-text").css({ "color": darkColor });
}

// This DOES NOT work well on the iPhone, but it stops the flip click, so I left it.
// based on http://stackoverflow.com/questions/1173194/select-all-div-text-with-single-mouse-click
//
//
function onClick_SelectBackCardNumberText() 
{
   if (document.selection) {
        var range = document.body.createTextRange();
        range.moveToElementText(document.getElementById('backCardNumberTextId'));
        range.select();
    }
    else if (window.getSelection) {
        var range = document.createRange();
        range.selectNode(document.getElementById('backCardNumberTextId'));
        window.getSelection().addRange(range);
    }
}