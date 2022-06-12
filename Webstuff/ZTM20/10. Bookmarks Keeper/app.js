const modal = document.getElementById("modal");
const modalShow = document.getElementById("show-modal");
const modalClose = document.getElementById("close-modal");
const bookmarkForm = document.getElementById("bookmark-form");
const websiteNameElement = document.getElementById("website-name");
const websiteURLElement = document.getElementById("website-url");
const bookmarksContainer = document.getElementById("bookmarks-container");
const googleServ = `http://s2.googleusercontent.com/s2/favicons?domain=`;
let bookmarks = [];

// Show Modal
function showModal() {
  modal.classList.add("show-modal");
  websiteNameElement.focus();
}

function validate(nameValue, urlValue) {
  const regURL = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/g;
  const regex = new RegExp(regURL);
  if (!nameValue || !urlValue) {
    return false;
  }
  if (urlValue.match(regex)) {
  }
  if (!urlValue.match(regex)) {
    alert("Not match");
    return false;
  }
  return true;
}

function storeBookmark(event) {
  event.preventDefault();
  const nameValue = websiteNameElement.value;
  let urlValue = websiteURLElement.value;
  if (!urlValue.includes("http://", "http://")) {
    urlValue = `https://${urlValue}`;
  }
  if (!validate(nameValue, urlValue)) {
    return false;
  }

  const bookmark = {
    name: nameValue,
    url: urlValue,
  };
  bookmarks.push(bookmark);
  localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  fetchBookmarks();
  bookmarkForm.reset();
  websiteNameElement.focus();
}

function buildBookmarks() {
  bookmarksContainer.textContent = "";
  bookmarks.forEach((bookmark) => {
    const { name, url } = bookmark;
    const item = document.createElement("div");
    const closeIcon = document.createElement("i");
    const linkInfo = document.createElement("div");
    const favicon = document.createElement("img");
    const link = document.createElement("a");
    item.classList.add("item");
    closeIcon.classList.add("fas", "fa-times");
    closeIcon.setAttribute("title", "Delete Bookmark");
    closeIcon.setAttribute("onclick", `deleteBookmark('${url}')`);
    linkInfo.classList.add("name");
    favicon.setAttribute("src", `${googleServ}${url}`);
    favicon.setAttribute("alt", "Favicon");
    link.setAttribute("href", `${url}`);
    link.setAttribute("target", "_blank");
    link.textContent = name;
    linkInfo.append(favicon, link);
    item.append(closeIcon, linkInfo);
    bookmarksContainer.appendChild(item);
  });
}

function fetchBookmarks() {
  if (localStorage.getItem("bookmarks")) {
    bookmarks = JSON.parse(localStorage.getItem("bookmarks"));
  } else {
    bookmarks = [
      {
        name: "Enter a name",
        url: "Enter a URL",
      },
    ];
  }
  localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  buildBookmarks();
}

function deleteBookmark(url) {
  bookmarks.forEach((bookmark, i) => {
    if (bookmark.url === url) {
      bookmarks.splice(i, 1);
    }
  });
  localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  fetchBookmarks();
}

bookmarkForm.addEventListener("submit", storeBookmark);
modalShow.addEventListener("click", showModal);

modalClose.addEventListener("click", () => {
  modal.classList.remove("show-modal");
});

window.addEventListener("click", (event) => {
  event.target === modal ? modal.classList.remove("show-modal") : false;
});

fetchBookmarks();
