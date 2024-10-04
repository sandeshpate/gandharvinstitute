// function menuopen(){
//     let menubtn = document.querySelector(".links").getAttribute('class');
//     let hamburger = document.querySelector(".hamburger");
//     if(menubtn=="links closed"){
//         document.querySelector(".links").setAttribute('class','links');
//         hamburger.setAttribute('class','fa-solid fa-close hamburger');
//     }
//     else{
//         document.querySelector(".links").setAttribute('class','links closed');
//         hamburger.setAttribute('class','fa-solid fa-bars hamburger');
//     }
     
// } 

// // to use login button
// function loginredirect(){
//     window.location.href="../../login page/login.html";
// }


// // to disable old dates from calender  
// let today = new Date().toISOString().split('T')[0];
// document.querySelector('.hasDatepicker').setAttribute('min',today);

// // to show submit pop up
// let myform = document.querySelector('.myform');
// myform.addEventListener('submit',(e)=>{
//     let popup = document.querySelector(".popup-cnt");
//     popup.style.display = "flex";
//     e.preventDefault();
//     let btn = document.querySelector(".popup-btn").addEventListener('click',(c)=>{
//         popup.style.display = "none";
//         myform.submit();
//     })
// })

let currentStep = 1;

function nextStep(step) {
    document.getElementById(`step${currentStep}`).style.display = "none";
    document.getElementById(`step${step}`).style.display = "block";
    currentStep = step;
}

function prevStep(step) {
    document.getElementById(`step${currentStep}`).style.display = "none";
    document.getElementById(`step${step}`).style.display = "block";
    currentStep = step;
}

document.getElementById("admissionForm").addEventListener("submit", function (event) {
    event.preventDefault();
    document.getElementById("successMessage").style.display = "block";
});
