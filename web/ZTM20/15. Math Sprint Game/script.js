// Pages
const gamePage = document.getElementById("game-page");
const scorePage = document.getElementById("score-page");
const splashPage = document.getElementById("splash-page");
const countdownPage = document.getElementById("countdown-page");
// Splash Page
const startForm = document.getElementById("start-form");
const radioContainers = document.querySelectorAll(".radio-container");
const radioInputs = document.querySelectorAll("input");
const bestScores = document.querySelectorAll(".best-score-value");
// Countdown Page
const countdown = document.querySelector(".countdown");
// Game Page
const itemContainer = document.querySelector(".item-container");
// Score Page
const finalTimeEl = document.querySelector(".final-time");
const baseTimeEl = document.querySelector(".base-time");
const penaltyTimeEl = document.querySelector(".penalty-time");
const playAgainBtn = document.querySelector(".play-again");

// Equations
let questionAmount = 0;
let equationsArray = [];
let playerGuessArray = [];
let bestScoreArray = [];

// Game Page
let firstNumber = 0;
let secondNumber = 0;
let equationObject = {};
const wrongFormat = [];

// Time
let timer = null;
let timePlayed = 0;
let baseTime = 0;
let penaltyTime = 0;
let finalTime = 0;
let finalTimeDisplay = `0.0`;

function checkTime() {
  if (playerGuessArray.length == questionAmount) {
    clearInterval(timer);
    equationsArray.forEach((equation, index) => {
      if (equation.evaluated === playerGuessArray[index]) {
        // Nothing
        // console.log('FIRE CORRECT')
      } else {
        penaltyTime += 0.5;
        // console.log('FIRE INCORRECT')
      }
    });
    finalTime = timePlayed + penaltyTime;
    console.log(
      `Time:${timePlayed} penalty: ${penaltyTime} final: ${finalTime}`
    );
    scoresToDOM();
  }
}

function addTime() {
  timePlayed += 0.1;
  checkTime();
}

function startTimer() {
  timePlayed = 0;
  penaltyTime = 0;
  finalTime = 0;
  timer = setInterval(addTime, 100);
  gamePage.removeEventListener("click", startTimer);
}

// Scroll

let valueY = 0;

function getSavedBestScores() {
  if (localStorage.getItem("bestScores")) {
    bestScoreArray = JSON.parse(localStorage.getItem("bestScores"));
  } else {
    bestScoreArray = [
      { questions: 10, bestScores: finalTimeDisplay },
      { questions: 25, bestScores: finalTimeDisplay },
      { questions: 50, bestScores: finalTimeDisplay },
      { questions: 99, bestScores: finalTimeDisplay },
    ];
    localStorage.setItem("bestScores", JSON.stringify(bestScoreArray));
  }
  bestScoresToDOM();
}

function updateBestScore() {
  bestScoreArray.forEach((score, index) => {
    // Select correct Best Score to update
    console.log(score);
    console.log(`${questionAmount} : ${score.questions}`);
    if (questionAmount == score.questions) {
      // Return Best Score as number with one decimal
      const savedBestScore = Number(bestScoreArray[index].bestScores);
      // Update if the new final score is less or replacing zero
      console.log(savedBestScore);
      if (savedBestScore === 0 || savedBestScore > finalTime) {
        console.log(`FIRED AT SCORE ${savedBestScore} and ${finalTimeDisplay}`);
        bestScoreArray[index].bestScores = finalTimeDisplay;
      }
    }
  });
  // Update Splash Page
  bestScoresToDOM();
  // Save to Local Storage
  localStorage.setItem("bestScores", JSON.stringify(bestScoreArray));
}
function showScorePage() {
  gamePage.hidden = true;
  scorePage.hidden = false;
  setTimeout(() => {
    playAgainBtn.hidden = false;
  }, 500);
}

function scoresToDOM() {
  finalTimeDisplay = finalTime.toFixed(1);
  baseTime = timePlayed.toFixed(1);
  penaltyTime = penaltyTime.toFixed(1);
  baseTimeEl.textContent = `Base time : ${baseTime}s`;
  penaltyTimeEl.textContent = `Penalty : ${penaltyTime}s`;
  finalTimeEl.textContent = `${finalTimeDisplay}s`;
  updateBestScore();
  itemContainer.scrollTo({
    top: 0,
    behavior: "instant",
  });
  showScorePage();
}

function bestScoresToDOM() {
  bestScores.forEach((item, index) => {
    const bestScoreEl = item;
    item.textContent = `${bestScoreArray[index].bestScores}s`;
  });
}
function select(guessedTrue) {
  valueY += 80;
  itemContainer.scroll(0, valueY);
  return guessedTrue
    ? playerGuessArray.push("true")
    : playerGuessArray.push("false");
}

function showGamePage() {
  gamePage.hidden = false;
  countdownPage.hidden = true;
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// max up to X
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function createEquations() {
  const correctEquations = getRandomInt(questionAmount);
  const wrongEquations = questionAmount - correctEquations;
  console.log(`${correctEquations} : ${wrongEquations}`);
  for (let i = 0; i < correctEquations; i++) {
    firstNumber = getRandomInt(9);
    secondNumber = getRandomInt(9);
    const equationValue = firstNumber * secondNumber;
    const equation = `${firstNumber} x ${secondNumber} = ${equationValue}`;
    equationObject = { value: equation, evaluated: "true" };
    equationsArray.push(equationObject);
  }
  for (let i = 0; i < wrongEquations; i++) {
    firstNumber = getRandomInt(9);
    secondNumber = getRandomInt(9);
    const equationValue = firstNumber * secondNumber;
    wrongFormat[0] = `${firstNumber} x ${secondNumber + 1} = ${equationValue}`;
    wrongFormat[1] = `${firstNumber} x ${secondNumber} = ${equationValue - 1}`;
    wrongFormat[2] = `${firstNumber + 1} x ${secondNumber} = ${equationValue}`;
    const formatChoice = getRandomInt(3);
    const equation = wrongFormat[formatChoice];
    equationObject = { value: equation, evaluated: "false" };
    equationsArray.push(equationObject);
  }
  shuffleArray(equationsArray);
}

function equationsToDOM() {
  equationsArray.forEach((equation) => {
    const item = document.createElement("div");
    item.classList.add("item");
    const equationText = document.createElement("h1");
    equationText.textContent = equation.value;
    item.appendChild(equationText);
    itemContainer.appendChild(item);
  });
}

function populateGamePage() {
  // Reset DOM, Set Blank Space Above
  itemContainer.textContent = "";
  // Spacer
  const topSpacer = document.createElement("div");
  topSpacer.classList.add("height-240");
  // Selected Item
  const selectedItem = document.createElement("div");
  selectedItem.classList.add("selected-item");
  // Append
  itemContainer.append(topSpacer, selectedItem);

  // Create Equations, Build Elements in DOM
  createEquations();
  equationsToDOM();
  // Set Blank Space Below
  const bottomSpacer = document.createElement("div");
  bottomSpacer.classList.add("height-500");
  itemContainer.appendChild(bottomSpacer);
}

function startCountdown() {
  countdown.textContent = "3";
  setTimeout(() => {
    countdown.textContent = "2";
  }, 1000);
  setTimeout(() => {
    countdown.textContent = "1";
  }, 2000);
  setTimeout(() => {
    countdown.textContent = "GO";
  }, 3000);
}

function showCountdown() {
  countdownPage.hidden = false;
  splashPage.hidden = true;
  startCountdown();
  populateGamePage();
  setTimeout(showGamePage, 4000);
}

function getRadioValue() {
  let radioValue = null;
  radioInputs.forEach((radio) => {
    if (radio.checked) {
      radioValue = radio.value;
    }
  });
  return radioValue;
}

function selectQuestionAmount(event) {
  event.preventDefault();
  questionAmount = getRadioValue();
  console.log(`Question amount = ${questionAmount}`);
  if (questionAmount) {
    showCountdown();
  }
}

function playAgain() {
  gamePage.addEventListener("click", startTimer);
  scorePage.hidden = true;
  splashPage.hidden = false;
  equationsArray = [];
  playerGuessArray = [];
  valueY = 0;
  playAgainBtn.hidden = true;
}
startForm.addEventListener("click", () => {
  radioContainers.forEach((radio) => {
    radio.classList.remove("selected-label");
    if (radio.children[1].checked) {
      radio.classList.add("selected-label");
    }
  });
});

startForm.addEventListener("submit", selectQuestionAmount);
gamePage.addEventListener("click", startTimer);

getSavedBestScores();
