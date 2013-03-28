
// appBusId - Mobile Card Wallet and Skratch are mapped to a Business
// targetLink - should come from BusinessWalletInfo.TargetLink, like '/Cert/T2/AddGiftangoCard.aspx'
//
function addTo_GiftangoWallet(appBusId, targetLink) {
    var destUrlStr; 
    var bcnId = $(document).getUrlParam("BCNID");
    if ((bcnId != null) && (bcnId.length > 0)) {
        destUrlStr = targetLink + "?BCNID=" + bcnId + "&APP_BUSID=" + appBusId;
    }
    else {
        alert("Error: The BCNID is missing from the URL.");
    }
    window.location.href = destUrlStr;
}

function cannot_AddTo_GiftangoWallet() {
    alert("I'm sorry, the card has already been added to a wallet.");
}

/* -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  

function onSelectWallet_Success(data, textStatus, errorThrown) {

    var activeFlags = data.d;
            
    if ((activeFlags & 1) == 1) {
        // enable Add for Mobile Card Wallet
        gIsMobileCardWalletValid = true;
        $('.mobile-card-wallet-class').css({"color":"blue"});
    }
    else {
        // disable Add for Mobile Card Wallet
        gIsMobileCardWalletValid = false;
        $('.mobile-card-wallet-class').css({"color":"red"});
    }
}

// parse errors, timeouts, errors (HTTP) 
//
function onSelectWallet__Failed(jqXHR, textStatus, errorThrown) {
    //hide the page loader
    $.mobile.hidePageLoadingMsg();

    $('#error_page_err_id').html(errorThrown);        // show user error...not for release?
    $.mobile.changePage('#error_page_id', { transition: 'slide' });
}

function onSelectWallet_PageShow() {
    gBcnIdStr = $(document).getUrlParam("BCNID");
    var vStr = $(document).getUrlParam("v");
    // TODO: Steve pass in the appBusId
            
    $.ajax({
        type: "POST",
        data: '{"bcnIdStr": "' + gBcnIdStr
        + '", "vStr": "' + vStr
        + '"}',
        dataType: "json",
        url: "AddGiftangoCardService.svc/AreCardsAvailable",
        contentType: "application/json; charset=utf-8",
        success: onSelectWallet_Success,
        error: onSelectWallet__Failed
    });
}
*/