let email = document.getElementById("email");
let userName = document.getElementById("name");
let userPhone = document.getElementById("ph");
let userPassword = document.getElementById("password");
let userImage = document.getElementById("user_image");
let warnData = document.getElementById("alertUser");
let warnBlock = document.getElementById("warnBlock");

// us variable is for email checking in validateEmail function
let us;
const validateEmail = (email) => {
  us = String(email)
    .toLowerCase()
    .match(
      /\b[A-Za-z0-9._%+-]+@(gmail\.com|outlook\.com|yahoo\.com|protonmail\.com)\b/
    );
};

function validateSignUp(e) {
  console.log(userImage[0]);
  validateEmail(email.value);
  if (userName.value == "") {
    e.preventDefault();
    warnData.innerHTML = "Please Enter Your Name";
    warnBlock.classList.remove("hidden");
    return false;
  } else if (us == null) {
    e.preventDefault();
    warnData.innerHTML = "Invalid Email";
    warnBlock.classList.remove("hidden");
    return false;
  } else if (userPhone.value == "") {
    e.preventDefault();
    warnData.innerHTML = "Please Enter Valid Phone Number";
    warnBlock.classList.remove("hidden");
    return false;
  } else if (userPassword.value.length < 8 && userPassword.value == "") {
    e.preventDefault();
    warnData.innerHTML = "Please Enter Your Password";
    warnBlock.classList.remove("hidden");
    return false;
  } else if (userImage[0] == undefined) {
    e.preventDefault();
    warnData.innerHTML = "Please Upload Your Profile Image";
    warnBlock.classList.remove("hidden");
    return false;
  } else {
    warnBlock.classList.add("hidden");
    return true;
  }
}
