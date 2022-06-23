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

client.on("message", (msg) => {
  const channel = client.channels.cache.get(`514836808312553472`);
  // console.log(channel);
  switch (msg.content) {
    case "ping":
      channel.send(`PREVED BUHANKA`);
      break;
    case "::q":
      channel.send(`*${testQuote.text}*\n**${testQuote.author}**`);
      break;
    case "sendpic":
      channel.send({
        files: ["https://i.ytimg.com/vi/1Ne1hqOXKKI/maxresdefault.jpg"],
      });
      break;
    default:
      break;
  }
});

client.login(key);
