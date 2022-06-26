const inputContainer = document.getElementById("input-container");
const countdownForm = document.getElementById("countdown-form");
const dateElement = document.getElementById("date-picker");

let countdownTitle = "";
let countdownDate = "";
let countdownValue = new Date();
let countdownActive = null;
let savedCountdown = null;
const second = 1000;
const minute = second * 60;
const hour = minute * 60;
const day = hour * 24;

const countdownElement = document.getElementById("countdown");
const countdownElementTitle = document.getElementById("countdown-title");
const countdownButton = document.getElementById("countdown-button");
const timeElements = document.querySelectorAll("span");
const today = new Date().toISOString().split("T")[0];
dateElement.setAttribute("min", today);

const completeElement = document.getElementById("complete");
const completeElementInfo = document.getElementById("complete-info");
const completeButon = document.getElementById("complete-button");

function updateDOM() {
  countdownActive = setInterval(() => {
    const now = new Date().getTime();
    const distance = countdownValue - now;

    const days = Math.floor(distance / day);
    const hours = Math.floor((distance % day) / hour);
    const minutes = Math.floor((distance % hour) / minute);
    const seconds = Math.floor((distance % minute) / second);

    inputContainer.hidden = true;
    if (distance < 0) {
      countdownElement.hidden = true;
      clearInterval(countdownActive);
      completeElementInfo.textContent = `${countdownTitle} finished on ${countdownDate}`;
      completeElement.hidden = false;
    } else {
      countdownElementTitle.textContent = `${countdownTitle}`;
      timeElements[0].textContent = `${days}`;
      timeElements[1].textContent = `${hours}`;
      timeElements[2].textContent = `${minutes}`;
      timeElements[3].textContent = `${seconds}`;
      countdownElement.hidden = false;
      completeElement.hidden = true;
    }
  }, second);
}

function updateCountdown(event) {
  event.preventDefault();
  countdownTitle = event.srcElement[0].value;
  countdownDate = event.srcElement[1].value;
  savedCountdown = {
    title: countdownTitle,
    date: countdownDate,
  };
  localStorage.setItem("countdown", JSON.stringify(savedCountdown));
  if (countdownDate === "") {
    alert("Enter a date");
  } else {
    countdownValue = new Date(countdownDate).getTime();
    updateDOM();
  }
}

function resetAll() {
  countdownElement.hidden = true;
  inputContainer.hidden = false;
  clearInterval(countdownActive);
  countdownElementTitle.textContent = "";
  countdownDate = "";
  completeElement.hidden = true;
  localStorage.removeItem("countdown");
}

function restorePreviousCountdown() {
  if (localStorage.getItem("countdown")) {
    inputContainer.hidden = true;
    savedCountdown = JSON.parse(localStorage.getItem("countdown"));
    countdownTitle = savedCountdown.title;
    countdownDate = savedCountdown.date;
    countdownValue = new Date(countdownDate).getTime();
    updateDOM();
  }
}

countdownForm.addEventListener("submit", updateCountdown);
countdownButton.addEventListener("click", resetAll);
completeButon.addEventListener("click", resetAll);

restorePreviousCountdown();
