const photos = 3;
const unsplash =
  "7ff62dfa0f6bdc0babd7451cdea2a7c9a58e11b21807c2b172ec038d285b11b6";
const apiURL = `https://api.unsplash.com/photos/random?client_id=${unsplash}&count=${photos}`;

const loader = document.getElementById("loader");

let ready = false;
let imagesLoaded = 0;
let totalImages = 0;
let imageList = [];
const imageContainer = document.getElementById("image-container");

function imageLoaded() {
  imagesLoaded++;
  if (imagesLoaded === totalImages) {
    ready = true;
    loader.hidden = true;
  }
}

async function getPhotos() {
  try {
    const response = await fetch(apiURL);
    imageList = await response.json();
    displayPhotos();
  } catch (error) {
    console.log(error);
  }
}

function displayPhotos() {
  imagesLoaded = 0;
  totalImages = imageList.length;
  imageList.forEach((photo) => {
    const item = document.createElement("a");
    item.setAttribute("href", photo.links.html);
    item.setAttribute("target", "_blank");
    const img = document.createElement("img");
    img.setAttribute("src", photo.urls.regular);
    img.setAttribute("alt", photo.alt_description);
    img.setAttribute("title", photo.alt_description);
    img.addEventListener("load", imageLoaded);
    item.appendChild(img);
    imageContainer.appendChild(item);
  });
}

window.addEventListener("scroll", () => {
  if (
    window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000 &&
    ready
  ) {
    ready = false;
    getPhotos();
  }
});
getPhotos();
