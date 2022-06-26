const audio = document.querySelector("audio");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");
const playBtn = document.getElementById("play");

const image = document.querySelector("img");
const title = document.getElementById("title");
const artist = document.getElementById("artist");

const progressContainer = document.getElementById("progress-container");
const progress = document.getElementById("progress");
const currentTimeElement = document.getElementById("current-time");
const durationElement = document.getElementById("duration");

const songs = [
  {
    name: "jacinto-1",
    displayName: "Electric Chill Machine",
    artist: "Jacinto Design",
  },
  {
    name: "jacinto-2",
    displayName: "Second",
    artist: "Jacinto Design",
  },
  {
    name: "jacinto-3",
    displayName: "Third",
    artist: "Jacinto Design",
  },
  {
    name: "metric-1",
    displayName: "Whatever",
    artist: "Metric1",
  },
];

function toggleMusic() {
  if (audio.paused) {
    audio.play();
    playBtn.classList.replace("fa-play", "fa-pause");
    playBtn.setAttribute("title", "Pause");
  } else {
    audio.pause();
    playBtn.classList.replace("fa-pause", "fa-play");
    playBtn.setAttribute("title", "Play");
  }
}

playBtn.addEventListener("click", toggleMusic);

function loadSong(song) {
  title.textContent = song.displayName;
  artist.textContent = song.artist;
  audio.src = `./music/${song.name}.mp3`;
  image.src = `./img/${song.name}.jpg`;
}

let songIndex = 0;

function prevSong() {
  songIndex--;
  if (songIndex < 0) {
    songIndex = songs.length - 1;
  }
  loadSong(songs[songIndex]);
  toggleMusic();
}

function nextSong() {
  songIndex++;
  if (songIndex > songs.length - 1) {
    songIndex = 0;
  }
  loadSong(songs[songIndex]);
  toggleMusic();
}

function updateProgressBar(event) {
  if (!audio.paused) {
    const { duration, currentTime } = event.srcElement;
    const progressPercent = (currentTime / duration) * 100;
    progress.style.width = `${progressPercent}%`;
    let durationMinutes = Math.floor(duration / 60);
    let durationSeconds = Math.floor(duration % 60);
    let currentMinutes = Math.floor(currentTime / 60);
    let currentSeconds = Math.floor(currentTime % 60);

    if (durationSeconds < 10) {
      durationSeconds = `0${durationSeconds}`;
    }

    if (durationSeconds) {
      durationElement.textContent = `${durationMinutes}:${durationSeconds}`;
    }

    if (currentSeconds < 10) {
      currentSeconds = `0${currentSeconds}`;
    }

    if (currentSeconds) {
      currentTimeElement.textContent = `${currentMinutes}:${currentSeconds}`;
    }
  }
}

loadSong(songs[songIndex]);

function setProgressBar(event) {
  const width = this.clientWidth;
  const clickX = event.offsetX;
  const { duration } = audio;
  audio.currentTime = (clickX / width) * duration;
}

prevBtn.addEventListener("click", prevSong);
nextBtn.addEventListener("click", nextSong);
audio.addEventListener("timeupdate", updateProgressBar);
audio.addEventListener("ended", nextSong);
progressContainer.addEventListener("click", setProgressBar);
