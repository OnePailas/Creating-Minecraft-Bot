from javascript import require, On, Once, AsyncTask, off, on

mineflayer = require('mineflayer')

bot = mineflayer.createBot({
    'host': 'adress',
    'username': 'Nqowdown',
    'version': '1.8.9'
})

@On(bot, 'chat')
def msgHandler(this, user, message, *args):
    if user != 'Bot':
        bot.chat(f'Привет, {user}, как твои дела?')

