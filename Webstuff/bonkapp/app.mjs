// Import the functions you need from the SDKs you need
import { initializeApp, applicationDefault, cert } from "firebase-admin/app";
import { getFirestore, Timestamp, FieldValue } from "firebase-admin/firestore";
import Express from "express";
const serviceAccount = ?;
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAOhcPOY9h9MhSeFzdBlDRh-Fu8kgNaQ0Y",
  authDomain: "bonk-b0fc2.firebaseapp.com",
  projectId: "bonk-b0fc2",
  storageBucket: "bonk-b0fc2.appspot.com",
  messagingSenderId: "764532280446",
  appId: "1:764532280446:web:07943fb942cba3340b1c2f",
};

// Initialize Firebase

initializeApp({
  credential: cert(serviceAccount),
});
const db = getFirestore();
const app = Express();

// Get a list of cities from your database
async function getMemes(db) {
  const memesCol = collection(db, "memes");
  const memeSnapshot = await getDocs(memesCol);
  const memeList = memeSnapshot.docs.map((doc) => doc.data());
  return memeList;
}

app.get("/", (request, response) => {
  getMemes(db).then((data) => response.send(data));
});

app.get("/bobonk", (request, response) => {
  db.collection("memes").add({
    link: "https://i.ytimg.com/vi/Zr-qM5Vrd0g/maxresdefault.jpg",
  });
  response.send("Meme is added!");
});

app.listen(3005, () => {
  console.log("Meme app is on port 3005");
});
