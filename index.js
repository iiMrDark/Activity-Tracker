const TelegramBot = require('node-telegram-bot-api');
const fs = require('fs');



// حط توكين البوت بتاعك هنا
const token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX';
const bot = new TelegramBot(token, { polling: true });

// حط معرف القناة الي عايز تبعتلها من البوت هنا
const channelId = '@iMrDarkActivity';

let lastMessageId = null;

const readDataFromFile = () => {
    return new Promise((resolve, reject) => {
        fs.readFile('C:\\usage_log.txt', 'utf8', (err, data) => {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
};

const updateMessageInChannel = async () => {
    try {
        const data = await readDataFromFile();

        if (lastMessageId) {
            
            await bot.editMessageText(data, {
                chat_id: channelId,
                message_id: lastMessageId,
            });
            console.log('Message updated successfully');
        } else {

            const sentMessage = await bot.sendMessage(channelId, data);
            lastMessageId = sentMessage.message_id;
            console.log('Message sent successfully');
        }
    } catch (error) {
    }
};

setInterval(updateMessageInChannel, 2000);
console.log('Bot is running and will update the channel message every minute.');