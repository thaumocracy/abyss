const quoteContainer = document.getElementById("quote-container");
const quoteText = document.getElementById("quote");
const authorText = document.getElementById("author");
const twitterBtn = document.getElementById("twitter");
const newQuoteBtn = document.getElementById("new-quote");
const loader = document.getElementById("loader");

function showSpinner() {
  loader.hidden = false;
  quoteContainer.hidden = true;
}

function removeSpinner() {
  if (!loader.hidden) {
    quoteContainer.hidden = false;
    loader.hidden = true;
  }
}

async function getQuote() {
  showSpinner();
  const proxyURL = "https://cors-anywhere.herokuapp.com/";
  const apiURL =
    "http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json";
  try {
    const response = await fetch(proxyURL + apiURL, {
      headers: { Origin: "X-Requested-With" },
    });
    const data = await response.json();
    if (data.quoteAuthor === "") {
      authorText.innerText = "unknown";
    } else {
      authorText.innerText = data.quoteAuthor;
    }
    if (data.quoteText.length > 120) {
      quoteText.classList.add("long-quote");
    } else {
      quoteText.classList.remove("long-quote");
    }
    quoteText.innerText = data.quoteText;
    removeSpinner();
  } catch (error) {
    getQuote();
  }
}

getQuote();
showSpinner();

newQuoteBtn.addEventListener("click", () => {
  getQuote();
});

twitterBtn.addEventListener("click", () => {
  alert("Sorry,twitter did not approve my request");
});
