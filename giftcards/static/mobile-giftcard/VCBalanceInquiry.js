//***********************************************
// VerifiyCertBalance
// Description: Call Webservice
    // AJAX Call using POST
// updated to use jquery so that all browsers can be supported
//***********************************************

    function VerifiyCertBalance(strEncryptedBarCodeNr) {
        if (document.getElementById("lnkVerify")!=null && document.getElementById("lnkVerify").disabled)
        {
            alert($('#hidOnlyVerifiedTwentyMins').val());
            return;
        }

        if (document.getElementById("lnkVerifyProductBalance") != null && document.getElementById("lnkVerifyProductBalance").disabled) {
            alert($('#hidOnlyVerifiedTwentyMins').val());
            return;
        }



        if (document.getElementById("lnkVerifyImg") != null && document.getElementById("lnkVerifyImg").disabled)
        {
            alert($('#hidOnlyVerifiedTwentyMins').val());
            return;
        }


        var loadUrl = "GIEVerifyBalanceData.asmx/VerifiyCertBalance";
        $.post(loadUrl, { strEncryptedBarCodeNr: strEncryptedBarCodeNr }, function(data, response, status) {
            if (response != "success" || data == null) {
                alert($('#hidUnableToUpdateBalance').val());
            }
            if (data.text != null)      //stupid ie
            {
                if (data.text == "FAIL") {
                    alert($('#hidUnableToUpdateBalance').val());
                    return;
                }
                UpdateBalance(data.text);
            }
            else if (data.firstChild != null && data.firstChild.textContent != null)     //every other good browser
            {
                if (data.firstChild.textContent == "FAIL") {
                    alert($('#hidUnableToUpdateBalance').val());
                    return;
                }
                UpdateBalance(data.firstChild.textContent);
            }
            else
                alert($('#hidUnableToUpdateBalance').val());

        }, "xml");
    }


//***********************************************
// GetXmlHttpObject
// Description: Create XML HTTP Object
//***********************************************
function GetXmlHttpObject() {
    if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        return new XMLHttpRequest();
    }
    if (window.ActiveXObject) {
        // code for IE6, IE5
        return new ActiveXObject("Microsoft.XMLHTTP");
    }
    return null;
}

//***********************************************
// UpdateBalance()
// Description: Update the Balance and Date
//***********************************************
function UpdateBalance(data) {
    var objForm;

    if (IsIE()) {
        objForm = document.all.frmCertificate;
    }
    else {
        objForm = document.frmCertificate;
    }

    var sSplitResult = data.split("-");
    
    //products
    if (document.getElementById("lblProductBalance") != null)
        document.getElementById("lblProductBalance").innerHTML = sSplitResult[1];
    //normal
    if (document.getElementById("lblCertAmount") != null)
        document.getElementById("lblCertAmount").innerHTML = sSplitResult[1];
    if (document.getElementById("lblLastKnowBalanceDateTime") != null)
        document.getElementById("lblLastKnowBalanceDateTime").innerHTML = sSplitResult[2];
    
    alert($('#hidBalanceOfCard').val() + sSplitResult[1] + " " + $('#hidAsOf').val() + " " + sSplitResult[2] + ".");
    countdown();
}

//***********************************************
// IsIE()
// Description: Check if browser is IE.
//***********************************************
function IsIE() {
    var BrowserName = navigator.appName
    var BrowserVersion = parseInt(navigator.appVersion);

    if (BrowserName == "Microsoft Internet Explorer")
        return true;
    else
        return false;
}

var timer=1200;
function countdown() 
{
  
  timer--;
  if(timer == 0)
  {
      if (document.getElementById("lnkVerify") != null) 
      {
          document.getElementById("lnkVerify").disabled = false;
          document.getElementById("lnkVerify").title = '';
      }
      if (document.getElementById("lnkVerifyProductBalance") != null) {
          document.getElementById("lnkVerifyProductBalance").disabled = false;
          document.getElementById("lnkVerifyProductBalance").title = '';
      }
      if (document.getElementById("lnkVerifyImg") != null) 
      {
          document.getElementById("lnkVerifyImg").disabled = false;
          document.getElementById("lnkVerifyImg").title = '';
      }      
  }
  if (timer > 0) 
  {
      if (document.getElementById("lnkVerify") != null) 
      {
          document.getElementById("lnkVerify").disabled = true;
          document.getElementById("lnkVerify").title = $('#hidOnlyVerifiedTwentyMins').val();
      }
      if (document.getElementById("lnkVerifyProductBalance") != null) 
      {
          document.getElementById("lnkVerifyProductBalance").disabled = true;
          document.getElementById("lnkVerifyProductBalance").title = $('#hidOnlyVerifiedTwentyMins').val();
      }
      if (document.getElementById("lnkVerifyImg") != null) 
      {
          document.getElementById("lnkVerifyImg").disabled = true;
          document.getElementById("lnkVerifyImg").title = $('#hidOnlyVerifiedTwentyMins').val();
      }
  
  
      
      
      setTimeout('countdown()',1200);
  }
}

