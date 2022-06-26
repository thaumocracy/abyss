import { Client, Intents } from "discord.js";
import key from "./key.mjs";

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});
client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

const testQuote = {
  author: "Маркус Туллий Цицерон",
  text: "“A room without books is like a body without a soul.”",
};

const pictures = [
  {
    title: "Звездная ночь",
    author: "Винсент Ван Гог",
    country: "🇳🇱",
    year: "1889",
    link: "https://losko.ru/wp-content/uploads/2019/11/7702b9faef4382f33090b0b87b2c0ad0-1.jpg",
  },
  {
    title: "Черный квадрат",
    author: "Казимир Малевич",
    country: "🇺🇦",
    year: "1915",
    link: "https://losko.ru/wp-content/uploads/2019/11/CHe-rnyi-_suprematicheskii-_kvadrat._1915._GTG.png",
  },
  {
    title: "Девочка с персиками",
    author: "Валентин Александрович Серов",
    country: "🇷🇺",
    year: "1887",
    link: "https://losko.ru/wp-content/uploads/2019/11/Valentin_Serov_-_Devochka_s_persikami._Portret_V.S.Mamontovoi-_-_Google_Art_Project.jpg",
  },
  {
    title: "Девушка с жемчужной сережкой",
    author: "Ян Вермеер",
    country: "🇳🇱",
    year: "1665",
    link: "https://losko.ru/wp-content/uploads/2019/11/cover-1.jpg",
  },
  {
    title: "Постоянство памяти",
    author: "Сальвадор Дали",
    country: "🇪🇸",
    style: "",
    type: "",
    year: "1889",
    link: "https://losko.ru/wp-content/uploads/2019/11/ebd7ff7f9d8ddb7b9a8502168187.jpg",
  },
];

client.on("message", (msg) => {
  const channel = client.channels.cache.get(msg.channel.id);
  console.log(msg.channel.id);
  // console.log(channel);
  switch (msg.content) {
    case "ping":
      channel.send(`PREVED BUHANKA`);
      break;
    case "::q":
      channel.send(`*${testQuote.text}*\n**${testQuote.author}**`);
      break;
    case "::pic":
      const picture = pictures[Math.floor(Math.random() * pictures.length)];
      channel.send(
        `"${picture.title}" by ${picture.author}. ${picture.country}, ${picture.year}.`
      );
      channel.send({
        files: [picture.link],
      });
      break;
    default:
      break;
  }
});

client.login(key);
