// const forms = document.querySelector(".forms"),
// pwShowHide = document.querySelectorAll(".eye-icon"),
// links = document.querySelectorAll(".link");

// pwShowHide.forEach(eyeIcon => {
// eyeIcon.addEventListener("click", () => {
//   let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
  
//   pwFields.forEach(password => {
//       if(password.type === "password"){
//           password.type = "text";
//           eyeIcon.classList.replace("bx-hide", "bx-show");
//           return;
//       }
//       password.type = "password";
//       eyeIcon.classList.replace("bx-show", "bx-hide");
//   })
  
// })
// })      

// links.forEach(link => {
// link.addEventListener("click", e => {
//  e.preventDefault(); //preventing form submit
//  forms.classList.toggle("show-signup");
// })
// })

/*--- LOGIN SHOW AND HIDDEN ---*/
const singUp = document.getElementById('sign-up');
    singIn = document.getElementById('sign-in');
    loginIn = document.getElementById('login-in');
    loginUp = document.getElementById('login-up');


singUp.addEventListener('click', function() {
    //Remove classes first if they exist
    loginIn.classList.remove('block');
    loginUp.classList.remove('none');

    //Add classes
    loginIn.classList.add('none');
    loginUp.classList.add('block');
});

singIn.addEventListener('click', function() {
    //Remove classes first if they exist
    loginIn.classList.remove('none');
    loginUp.classList.remove('block');

    //Add classes
    loginIn.classList.add('block');
    loginUp.classList.add('none');
});