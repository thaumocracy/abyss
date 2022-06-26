const form = document.getElementById("form");
const password1Element = document.getElementById("password1");
const password2Element = document.getElementById("password2");
const messageContainer = document.querySelector(".message-container");
const message = document.getElementById("message");

let isValid = false;
let passwordsMatch = false;

function validateForm() {
  isValid = form.checkValidity();
  console.log(isValid);
  if (!isValid) {
    messageContainer.textContent = "Please Fill out all fields";
    messageContainer.style.color = "red";
    messageContainer.style.borderColor = "red";
    return;
  }
  if (password1Element.value === password2Element.value) {
    passwordsMatch = true;
    password1Element.style.borderColor = "green";
    password2Element.style.borderColor = "green";
  } else {
    passwordsMatch = false;
    message.textContent = "Make sure passwords match.";
    message.style.color = "red";
    messageContainer.style.borderColor = "red";
    password1Element.style.borderColor = "red";
    password2Element.style.borderColor = "red";
    return;
  }

  if (isValid && passwordsMatch) {
    message.textContent = "You just joined in!";
    message.style.color = "green";
    messageContainer.style.borderColor = "green";
  }
}

function storeFormData() {
  const user = {
    name: form.name.value,
    phone: form.phone.value,
    email: form.email.value,
    website: form.website.value,
    password: form.password1.value,
  };
  console.log(user);
}

function processFormData(event) {
  event.preventDefault();
  console.log("SUBMITTED");
  validateForm();
  if (isValid && passwordsMatch) {
    storeFormData();
  }
}

form.addEventListener("submit", processFormData);
