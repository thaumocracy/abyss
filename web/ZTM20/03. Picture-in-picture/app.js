const videoElement = document.getElementById("video");
const button = document.getElementById("button");

async function selectMediaStream() {
  try {
    const mediaStream = await navigator.mediaDevices.getDisplayMedia();
    videoElement.srcObject = mediaStream;
    videoElement.onloadedmetadata = () => {
      videoElement.play();
    };
  } catch (error) {
    console.log(error);
  }
}

button.addEventListener("click", async () => {
  button.disabled = true;
  await videoElement.requestPictureInPicture();
  button.disabled = false;
});

async function getUsers() {
  try {
    const data = await fetch("https://jsonplaceholder.typicode.com/users");
    const users = await data.json();
    console.log(users);
  } catch (error) {
    console.log(error);
  }
}

selectMediaStream();
