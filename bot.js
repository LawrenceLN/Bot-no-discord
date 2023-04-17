const Discord = require('discord.js');
const client = new Discord.Client();
const TOKEN = 'YOUR_BOT_TOKEN';

client.on('ready', () => {
  console.log(`Bot conectado como ${client.user.tag}`);
});

client.on('guildMemberAdd', member => {
  const message = 'Bem-vindo ao Clube da Luta, se esse é seu priemrio dia, você tem que lutar!';
  member.send(message);
});

client.login(TOKEN);
