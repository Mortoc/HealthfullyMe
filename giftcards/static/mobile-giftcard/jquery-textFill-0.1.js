; (function($) {
	/**
	* Resizes an inner element's font so that the inner element completely fills the outer element.
	* @author Russ Painter WebDesign@GeekyMonkey.com
	* @version 0.1
	* @param {Object} Options which are maxFontPixels (default=40), innerTag (default='span')
	* @return All outer elements processed
	* @example <div class='mybigdiv filltext'><span>My Text To Resize</span></div>
	*/
	$.fn.textfill = function(options) {
		var defaults = {
			maxFontPixels: 40,
			innerTag: 'span'
		};
		var Opts = jQuery.extend(defaults, options);
		return this.each(function() {
			var fontSize = Opts.maxFontPixels;
			var ourText = $(Opts.innerTag + ':visible:first', this);
			var maxHeight = $(this).height();
			var maxWidth = $(this).width();
			var textHeight;
			var textWidth;
			do {
				ourText.css('font-size', fontSize);
				textHeight = ourText.height();
				textWidth = ourText.width();
				fontSize = fontSize - 1;
			} while ((textHeight > maxHeight || textWidth > maxWidth) && fontSize > 3);
		});
	};
	
	// STC 3/29/12 - Make better for Cert card passing in height and width
	//
	$.fn.textfillStc = function(options) {
		var defaults = {
			maxFontPixels: 40,
			maxHeight: 30,
			maxWidth: 100,
			innerTag: 'span'
		};
		var Opts = jQuery.extend(defaults, options);
		return this.each(function() {
			var fontSize = Opts.maxFontPixels;
			var ourText = $(Opts.innerTag + ':visible:first', this);
			var maxHeight = Opts.maxHeight;	 	// $(this).height();
			var maxWidth  = Opts.maxWidth;	// $(this).width();
			var textHeight;
			var textWidth;
            var constrainHeightToFont = Opts.maxHeight;
			do {
				ourText.css('font-size', fontSize);
				textHeight = ourText.height();
				textWidth = ourText.width();
				constrainHeightToFont = fontSize + (fontSize * 0.2);           // keep on a single line
                fontSize = fontSize - 2;
                
			} while (((textHeight > constrainHeightToFont) || (textWidth > maxWidth)) && fontSize > 8);
		});
	};
	
    
	// alt http://stackoverflow.com/questions/687998/auto-size-dynamic-text-to-fill-fixed-size-container
	(function($) {
		$.fn.textfillStcSingleLine = function(maxFontSize, maxWidth, maxHeight) {
			maxFontSize = parseInt(maxFontSize, 10);
			inMaxHeight = maxHeight;	// parseInt(maxHeight, 20);	 	// $(this).height();
			inMaxWidth  = maxWidth;		// parseInt(maxWidth, 30);			// $(this).width();
			minFontSize = 9;

			return this.each(function(){
				var ourText = $("span:visible:first", this),    
					parent = ourText.parent(),
					maxHeight = inMaxHeight,	// = parent.height(),
					maxWidth = inMaxWidth,		//  = parent.width(),
					fontSize = parseInt(ourText.css("fontSize"), 10),
					multiplier = maxWidth/ourText.width(),
					newSize = (fontSize*(multiplier-0.1));
                
               if (maxFontSize > 0 && newSize > maxFontSize) {
                    newSize = maxFontSize;
               } else if(minFontSize > 0 && newSize < minFontSize) {
                    newSize = minFontSize;
               }

               if (! isNaN(newSize)) {             // 7/31/12
                    ourText.css("fontSize",newSize);  
               }
               // window.console && console.log("textfillStcSingleLine size: " + newSize + " max: " + maxFontSize);
            }); 
		};
	})(jQuery);


    /* not working...

    (function($) {
		$.fn.textfillStcSecondLine = function(maxFontSize, maxWidth, maxHeight) {
			maxFontSize = parseInt(maxFontSize, 10);
			inMaxHeight = maxHeight;	// parseInt(maxHeight, 20);	 	// $(this).height();
			inMaxWidth  = maxWidth;		// parseInt(maxWidth, 30);			// $(this).width();
			minFontSize = 9;

			return this.each(function(){
				var ourText = $("#lblGiftCardNumber", this),    
					parent = ourText.parent(),
					maxHeight = inMaxHeight,	// = parent.height(),
					maxWidth = inMaxWidth,		//  = parent.width(),
					fontSize = parseInt(ourText.css("fontSize"), 10),
					multiplier = maxWidth/ourText.width(),
					newSize = (fontSize*(multiplier-0.1));
                
               if (maxFontSize > 0 && newSize > maxFontSize) {
                    newSize = maxFontSize;
               } else if(minFontSize > 0 && newSize < minFontSize) {
                    newSize = minFontSize;
               }

               if (! isNaN(newSize)) {             // 7/31/12
                    ourText.css("fontSize",newSize);  
               }
               // window.console && console.log("textfillStcSingleLine size: " + newSize + " max: " + maxFontSize);
            }); 
		};
	})(jQuery);
    */

})(jQuery);


// $(document).ready(function() {
//	$('.jtextfill').textfill({ maxFontPixels: 36, innerTag: 'h1' });
// });
 