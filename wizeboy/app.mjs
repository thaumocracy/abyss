import { Client, Intents } from "discord.js";
import keys from "./keys.mjs";
import art from "./data/art.mjs";
import verses from "./data/verses.mjs";
import quotes from "./data/quotes.mjs";

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});
client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on("message", (msg) => {
  const channel = client.channels.cache.get(msg.channel.id);
  console.log(msg.channel.id);
  // console.log(channel);
  console.log(msg.content);
  switch (msg.content) {
    case "ping":
      channel.send(`PREVED BUHANKA`);
      break;
    case "::q":
    case "::quote":
    case "::цитата":
      const quote = quotes[Math.floor(Math.random() * quotes.length)];
      channel.send(`\`\`\`${quote.text}\`\`\`\n_${quote.author}_`);
      break;
    case "::v":
    case "::verse":
    case "::стих":
      const verse = verses[Math.floor(Math.random() * verses.length)];
      channel.send(`\`\`\`${verse.text}\`\`\`\n_${verse.author}_`);
      break;
    case "::p":
    case "::pic":
    case "::арт":
    case "::art":
      const picture = art[Math.floor(Math.random() * art.length)];
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

client.login(keys.discord);
