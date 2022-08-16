function cap() {
    var alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

    var key1 = alpha[Math.floor(Math.random() * 62)];
    var key2 = alpha[Math.floor(Math.random() * 62)];
    var key3 = alpha[Math.floor(Math.random() * 62)];
    var key4 = alpha[Math.floor(Math.random() * 62)];
    var key5 = alpha[Math.floor(Math.random() * 62)];
    var key6 = alpha[Math.floor(Math.random() * 62)];


    var sum = key1 + key2 + key3 + key4 + key5 + key6;
    $(".captcha ").val(sum)
    console.log(sum)
}


function validCap() {
    var string1 = $('.captcha').val()
    console.log('string1: ' +
        string1)
    var string2 = $('.textinput').val()
    console.log('string2: ' +
        string2)
    if (string1 == string2) {
        // alert('Form is validated successfully!')
        return true
    } else {
        alert('Please enter valid captcha!')
        return false
    }
}

cap()