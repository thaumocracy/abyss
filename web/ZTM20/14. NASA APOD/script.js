const count = 5;
const apiKey = "DEMO_KEY";
const nasaAPI = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}&count=${count}`;

const resultsNav = document.getElementById("resultsNav");
const favoritesNav = document.getElementById("favoritesNav");
const imagesContainer = document.querySelector(".images-container");
const saveConfirmed = document.querySelector(".save-confirmed");
const loader = document.querySelector(".loader");

let resultsArray = [];
let favorites = {};

function showContent() {
  loader.classList.add("hidden");
}

function createDOMNodes(page) {
  console.log(page);
  loader.classList.remove("hidden");
  const currentArray =
    page === "results" ? resultsArray : Object.values(favorites);
  currentArray.forEach((item) => {
    const card = document.createElement("div");
    card.classList.add("card");
    const link = document.createElement("a");
    link.href = item.hdurl;
    link.title = "View Full Image";
    link.target = "_blank";
    const image = document.createElement("img");
    image.src = item.url;
    image.alt = "NASA picture of the day";
    image.loading = "lazy";
    image.classList.add("card-img-top");
    const cardBody = document.createElement("div");
    cardBody.classList.add("card-body");
    const cardTitle = document.createElement("h5");
    cardTitle.classList.add("card-title");
    cardTitle.textContent = item.title;
    const saveText = document.createElement("p");
    saveText.classList.add("clickable");
    if (page === "results") {
      saveText.textContent = "Add to Favorites";
      saveText.setAttribute("onclick", `saveFavorite('${item.url}')`);
    } else {
      saveText.textContent = "Remove favorite";
      saveText.setAttribute("onclick", `removeFavorite('${item.url}')`);
    }
    const cardText = document.createElement("p");
    cardText.textContent = item.explanation;
    const footer = document.createElement("small");
    footer.classList.add("text-muted");
    const date = document.createElement("strong");
    date.textContent = item.date;
    const copyrightResult = item.copyright === undefined ? "" : item.copyright;
    const copyright = document.createElement("span");
    copyright.textContent = ` ${copyrightResult}`;
    // Append items
    footer.append(date, copyright);
    cardBody.append(cardTitle, saveText, cardText, footer);
    link.appendChild(image);
    card.append(link, cardBody);

    imagesContainer.appendChild(card);
  });
}

function updateDOM(page) {
  if (localStorage.getItem("nasaFavorites")) {
    favorites = JSON.parse(localStorage.getItem("nasaFavorites"));
  }
  imagesContainer.textContent = "";
  createDOMNodes(page);
  showContent();
}

async function getPictures() {
  try {
    const response = await fetch(nasaAPI);
    resultsArray = await response.json();
    updateDOM("results");
  } catch (error) {}
}

function saveFavorite(itemURL) {
  resultsArray.forEach((item) => {
    if (item.url.includes(itemURL) && !favorites[itemURL]) {
      favorites[itemURL] = item;
      saveConfirmed.hidden = false;
      setTimeout(() => {
        saveConfirmed.hidden = true;
      }, 2000);
    }
    localStorage.setItem("nasaFavorites", JSON.stringify(favorites));
  });
}

function removeFavorite(itemURL) {
  if (favorites[itemURL]) {
    delete favorites[itemURL];
  }
  localStorage.setItem("nasaFavorites", JSON.stringify(favorites));
  updateDOM("favorites");
}

getPictures();
