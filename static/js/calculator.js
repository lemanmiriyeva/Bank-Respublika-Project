var slider1 = document.getElementById('myrange1');
var output1 = document.getElementById('value1');
var slider2 = document.getElementById('myrange2');
var output2 = document.getElementById('value2');
var answer = document.getElementById("value3")
output1.innerHTML = slider1.value
output2.innerHTML = slider2.value
answer.innerHTML = ((slider1.value * 0.03) / (1 - (1 + 0.03) ** (-slider2.value))).toFixed(2)
slider1.oninput = function() {
    output1.innerHTML = this.value
    let value2 = output2.innerHTML
    let result = (this.value * 0.03) / (1 - (1 + 0.03) ** (-value2))
    result = result.toFixed(2)
    answer.innerHTML = result
}
slider2.oninput = function() {
    output2.innerHTML = this.value
    let value1 = output1.innerHTML
    let result = (value1 * 0.03) / (1 - (1 + 0.03) ** (-this.value))
    result = result.toFixed(2)
    answer.innerHTML = result
}
var fill1 = $(".fill1 ");
var fill2 = $(".fill2 ");

function setBar1() {
    fill1.css('width', 100 / 30000 * slider1.value + '%');
}
slider1.addEventListener('input', setBar1);
setBar1()

function setBar2() {
    fill2.css('width', 100 / 36 * slider2.value + '%');
}
slider2.addEventListener('input', setBar2);
setBar2()