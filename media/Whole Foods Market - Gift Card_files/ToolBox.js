//Comment #1 below
//To keep the css class.  For some reason a css class cannot be added after you loose all visible space in the html.  

//Does not work
function addLongWordSplits(inputString, maxLength) {
    var c = 3;
    while (c < inputString.length) {
        c++;
        if (c % maxLength == 0) {
            inputString = inputString.substring(0, c) + "&shy;" + inputString.substring(c, inputString.length);
            c = c + 3;
        }
    }
}

function showModalCloseConfirmation() {
    var r = confirm("Press a button!");
    if (r == true) {
        alert("You pressed OK!");
        $.modal.close();
    }
    else {
        alert("You pressed Cancel!");
    }
}



function splitLongWords(inputString, splitLength) {
    returnString = "";
    words = inputString.split(' ');
    word = "";
    for (wordIndex = 0; wordIndex < words.length; wordIndex++) {
        word = words[wordIndex];
        if (word.length > splitLength) {
            for (c = splitLength; c < word.length; c += splitLength) {
                if (c == splitLength * 2 && c < word.length - 2) {
                    splitLength++;
                    c = c + 2;
                }
                word = word.substring(0, c) + " " + word.substring(c, word.length);
            }
        }
        if (wordIndex != 0)
            returnString += ' ' + word;
        else
            returnString = word;
    }
    return returnString;
}