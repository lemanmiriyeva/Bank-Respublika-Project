$(document).ready(function() {

    function myFunction(x) {
        x.classList.toggle("fa-minus-circle");
    }


})
let nav1 = document.querySelector(".first-item");
let nav2 = document.querySelector(".second-item");
let navbar1 = document.querySelector(".navbar2")
let navbar2 = document.querySelector(".navbar3")
let btn1 = document.querySelector('.btn1')
let btn2 = document.querySelector('.btn2')
nav1.style.borderBottom = "2px solid #485dc6"
btn1.style.color = "#485dc6"
let campaign1 = document.querySelector('.first-item1');
let campaign2 = document.querySelector('.second-item1');
let campaigndiv1 = document.querySelector('.campaigns')

function change1() {
    nav2.style.borderBottom = "none"
    nav1.style.borderBottom = "2px solid #485dc6"
    btn1.style.color = "#485dc6"
    btn2.style.color = "#000"
    navbar2.classList.remove("d-none")
    navbar1.classList.add("d-none")



}

function change2() {
    nav1.style.borderBottom = "none"

    nav2.style.borderBottom = "2px solid #485dc6"
    btn2.style.color = "#485dc6"
    btn1.style.color = "#000"
    navbar1.classList.remove("d-none")
    navbar2.classList.add("d-none")

}

function change3() {
    campaigndiv1.style.display = "block";
    campaign2.style.borderBottom = "none"

    campaign1.style.borderBottom = "2px solid #485dc6"
    campaign1.style.color = "#485dc6"
    campaign2.style.color = "#000"
}

function change4() {
    campaigndiv1.style.display = "none";
    campaign1.style.borderBottom = "none"

    campaign2.style.borderBottom = "2px solid #485dc6"
    campaign2.style.color = "#485dc6"
    campaign1.style.color = "#000"
}