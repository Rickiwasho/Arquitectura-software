require('dotenv').config();

const kwBank = require('./constants/KeywordsBank');
const {GREET, CRYPTO_NOT_FOUND} = require('./constants/Responses');
const {isInMessage, isAllInMessage} = require('./utils/KeywordsUtils');
const { moneyFormatter, decimalFormatter} = require('./utils/Formatters');

const{RTMClient} = require('@slack/rtm-api');
const {WebClient} = require('@slack/web-api');
const packageJson = require('../package.json');

const botcoin = new RTMClient(process.env.BOT_TOKEN);
const webClient = new WebClient(process.env.BOT_TOKEN);

botcoin.start().catch(console.error);
botcoin.on('ready', async () => {
    
    console.log('Bot ready');
    announce(' Botcoin v ${packageJson.version} is online ');

});

const sendMessage = async (channel, text, attachments) => {
    await webClient.chat.postMessage({
        channel,
        text, 
        attachments
    });
};
const announce = async (message, types, attachments) => {
    const response = await webClient.conversations.list({

    });
}