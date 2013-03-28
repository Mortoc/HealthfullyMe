

function buildCrossPlatformCssGradient(jQueryObject, startColor, endColor) {
    var webKitStr = "-webkit-gradient(linear, left top, left bottom, from(" + startColor + "), to(" + endColor + "))";
    var ieStr = "progid:DXImageTransform.Microsoft.gradient(startColorstr='" + startColor + "', endColorstr='" + endColor + "');";
    var firefoxStr = "-moz-linear-gradient(top, " + startColor + ", " + endColor + ");"; 	 // for firefox 3.6+ 
    var firefox2Str = "linear-gradient(to bottom," + startColor + ", " + endColor + ");";
    jQueryObject.css('filter', ieStr);
    jQueryObject.css('background', webKitStr);
    jQueryObject.css('background-image', firefoxStr);
    jQueryObject.css('background-image', firefox2Str);
    /*
    $(fx.elem).css('background-image', '-moz-linear-gradient(' + gradientSpecifier + ')');
    $(fx.elem).css('background-image', '-o-linear-gradient(' + gradientSpecifier + ')');
    $(fx.elem).css('background-image', 'linear-gradient(' + gradientSpecifier + ')');
                
                
    var gradientCss = {
    'filter'	 : ieStr,
    'background' : webKitStr,
    'background' : firefoxStr
    };
			
    return(gradientCss);
    */
}

function isEmpty(checkStr) {
    if ((!checkStr) || (0 === checkStr.length)) {
        return (true);
    }
    else {
        return (false);
    }
}
// Redirect iPhone/iPod visitors
//	http://jquery-howto.blogspot.com/2010/09/iphone-ipod-detection-using-jquery.html
function isiPhone() {
    // Make work if faked  return ((navigator.platform.indexOf("iPhone") != -1) || (navigator.platform.indexOf("iPod") != -1));
    var ua = navigator.userAgent.toLowerCase();
    var is_iPhone = (ua.indexOf("iphone") > -1) || (ua.indexOf("ipod") > -1);
    return (is_iPhone);
}
function isMacIntel() {
    return ((navigator.platform.indexOf("MacIntel") != -1));
}
// detect Android 
//	http://davidwalsh.name/detect-android
function isAndroid() {
    var ua = navigator.userAgent.toLowerCase();
    var isAndroid = ua.indexOf("android") > -1; //&& ua.indexOf("mobile");
    return (isAndroid);
}
//	Convert Windows/Mac end-of-line character to Html end-of-line
// 		based on http://stackoverflow.com/questions/2390038/replace-n-with-br-and-r-n-with-p-in-javascript
//
function convertCrLftoBR(inStr) {
    var result = null;
    if (inStr != null) {
        result = inStr.replace(/\r\n\r\n/g, "</p><p>").replace(/\n\n/g, "</p><p>");
        result = result.replace(/\r\n/g, "<br />").replace(/\n/g, "<br />");
    }
    return (result);
}
