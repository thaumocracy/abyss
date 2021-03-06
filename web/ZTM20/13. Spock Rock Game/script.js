const playerScoreElement = document.getElementById("playerScore");
const playerChoiceElement = document.getElementById("playerChoice");
const computerScoreElement = document.getElementById("computerScore");
const computerChoiceElement = document.getElementById("computerChoice");
const resultText = document.getElementById("result-text");
const playerRock = document.getElementById("playerRock");
const playerPaper = document.getElementById("playerPaper");
const playerScissors = document.getElementById("playerScissors");
const playerLizard = document.getElementById("playerLizard");
const playerSpock = document.getElementById("playerSpock");
const computerRock = document.getElementById("computerRock");
const computerPaper = document.getElementById("computerPaper");
const computerScissors = document.getElementById("computerScissors");
const computerLizard = document.getElementById("computerLizard");
const computerSpock = document.getElementById("computerSpock");

const allGameIcons = document.querySelectorAll(".far");

const choices = {
  rock: { name: "Rock", defeats: ["scissors", "lizard"] },
  paper: { name: "Paper", defeats: ["rock", "spock"] },
  scissors: { name: "Scissors", defeats: ["paper", "lizard"] },
  lizard: { name: "Lizard", defeats: ["paper", "spock"] },
  spock: { name: "Spock", defeats: ["scissors", "rock"] },
};

let computerChoice = "";
let playerScoreNumber = 0;
let computerScoreNumber = 0;

function updateScore(playerChoice) {
  console.log(playerChoice, computerChoice);
  if (playerChoice === computerChoice) {
    resultText.textContent = "A TIE";
  } else {
    const choice = choices[playerChoice];
    console.log(choice.defeats.indexOf(computerChoice));
    if (choice.defeats.indexOf(computerChoice) > -1) {
      resultText.textContent = "YOU JUST WON A ROUND!";
      playerScoreNumber++;
      playerScoreElement.textContent = playerScoreNumber;
    } else {
      resultText.textContent = "A TRAGEDY HAPPENED!";
      computerScoreNumber++;
      computerScoreElement.textContent = computerScoreNumber;
    }
  }
}
function resetSelected() {
  allGameIcons.forEach((icon) => {
    icon.classList.remove("selected");
  });
}

function resetAll() {
  resetSelected();
  playerScoreNumber = 0;
  computerScoreNumber = 0;
  playerScoreElement.textContent = playerScoreNumber;
  computerScoreElement.textContent = computerScoreNumber;
  playerChoiceElement.textContent = "";
  computerChoiceElement.textContent = "";
  resultText.textContent = "";
}

function computerChoiceRandom() {
  const computerChoiceNumber = Math.floor(Math.random() * 10);
  switch (computerChoiceNumber) {
    case 0:
    case 1:
      computerChoice = "rock";
      break;
    case 2:
    case 4:
      computerChoice = "paper";
      break;
    case 4:
    case 5:
      computerChoice = "scissors";
      break;
    case 6:
    case 7:
      computerChoice = "lizard";
      break;
    case 8:
    case 9:
      computerChoice = "spock";
      break;
    default:
      computerChoice = "rock";
  }
}

function checkResult(playerChoice) {
  resetSelected();
  computerChoiceRandom();
  updateScore(playerChoice);
}

function select(playerChoice) {
  checkResult(playerChoice);
  switch (playerChoice) {
    case "rock":
      playerRock.classList.add("selected");
      playerChoiceElement.textContent = "--- Rock!";
      break;
    case "paper":
      playerPaper.classList.add("selected");
      playerChoiceElement.textContent = "--- Paper!";
      break;
    case "scissors":
      playerScissors.classList.add("selected");
      playerChoiceElement.textContent = "--- Scissors!";
      break;
    case "lizard":
      playerLizard.classList.add("selected");
      playerChoiceElement.textContent = "--- Lizard!";
      break;
    case "spock":
      playerSpock.classList.add("selected");
      playerChoiceElement.textContent = "--- Spock!";
      break;
    default:
      break;
  }
  computerSelect();
}

function computerSelect() {
  switch (computerChoice) {
    case "rock":
      computerRock.classList.add("selected");
      computerChoiceElement.textContent = "--- Rock!";
      break;
    case "paper":
      computerPaper.classList.add("selected");
      computerChoiceElement.textContent = "--- Paper!";
      break;
    case "scissors":
      computerScissors.classList.add("selected");
      computerChoiceElement.textContent = "--- Scissors!";
      break;
    case "lizard":
      computerLizard.classList.add("selected");
      computerChoiceElement.textContent = "--- Lizard!";
      break;
    case "spock":
      computerSpock.classList.add("selected");
      computerChoiceElement.textContent = "--- Spock!";
      break;
    default:
      break;
  }
}

resetAll();
