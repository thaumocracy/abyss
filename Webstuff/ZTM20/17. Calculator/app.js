const calculatorDisplay = document.querySelector("h1");
const inputButtons = document.querySelectorAll("button");
const clearButton = document.getElementById("clear-btn");

let firstValue = 0;
let operatorValue = "";
let awaitingNextValue = false;

const calculate = {
  "/": (num1, num2) => num1 / num2,
  "*": (num1, num2) => num1 * num2,
  "-": (num1, num2) => num1 - num2,
  "+": (num1, num2) => num1 + num2,
  "=": (num1, num2) => num2,
};

function sendNumberValue(number) {
  if (awaitingNextValue) {
    calculatorDisplay.textContent = number;
    awaitingNextValue = false;
  } else {
    const displayValue = calculatorDisplay.textContent;
    calculatorDisplay.textContent =
      calculatorDisplay === displayValue ? number : displayValue + number;
  }
}

function addDecimal() {
  if (awaitingNextValue) {
    return;
  }
  if (!calculatorDisplay.textContent.includes(".")) {
    calculatorDisplay.textContent = `${calculatorDisplay.textContent}.`;
  }
}

function resetAll() {
  calculatorDisplay.textContent = "0";
  firstValue = 0;
  operatorValue = "";
  awaitingNextValue = false;
}

function useOperator(operator) {
  const currentValue = Number(calculatorDisplay.textContent);
  if (operatorValue && awaitingNextValue) {
    operatorValue = operator;
    return;
  }
  if (!firstValue) {
    firstValue = currentValue;
  } else {
    const calculation = calculate[operatorValue](firstValue, currentValue);
    firstValue = calculation;
    calculatorDisplay.textContent = calculation;
  }
  awaitingNextValue = true;
  operatorValue = operator;
}

inputButtons.forEach((inputButton) => {
  if (inputButton.classList.length === 0) {
    inputButton.addEventListener("click", () =>
      sendNumberValue(inputButton.value)
    );
  } else if (inputButton.classList.contains("operator")) {
    inputButton.addEventListener("click", () => useOperator(inputButton.value));
  } else if (inputButton.classList.contains("decimal")) {
    inputButton.addEventListener("click", () => addDecimal());
  }
});

clearButton.addEventListener("click", resetAll);
