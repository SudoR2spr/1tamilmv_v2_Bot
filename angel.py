# @SudoR2spr WOODcraft 
from asyncio import events
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from flask import Flask, request

TOKEN = '6700432608:AAGLewsKHozPU8WoAIzvdEtYLGUhqZAZw'  # replace your bot token

bot = telebot.TeleBot(TOKEN)

# Flask app
app = Flask(__name__)

# Global variables
movie_list = []
real_dict = {}

# Commands and Handlers
@bot.message_handler(commands=['start'])
def random_answer(message):
    text_message = (
        "Hello👋 \n\n"
        "🗳 Get latest Movies from 1Tamilmv\n\n"
        "⚙️ *How to use me??*🤔\n\n"
        "✯ Please Enter */view* command and you'll get magnet link as well as link to torrent file 😌\n\n"
        "🔗 Share and Support💝"
    )
    
    keyboard = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('🔗 GitHub 🔗', url='https://github.com/SudoR2spr'),
        types.InlineKeyboardButton(text="⚡ Powered By", url='https://t.me/Opleech_WD')
    )
    
    bot.send_photo(
        chat_id=message.chat.id,
        photo='https://graph.org/file/4e8a1172e8ba4b7a0bdfa.jpg',
        caption=text_message,
        parse_mode='Markdown',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['view'])
def start(message):
    bot.send_message(message.chat.id, "*🧲 Please wait for 10 ⏰ seconds*", parse_mode='Markdown')
    global movie_list, real_dict
    movie_list, real_dict = tamilmv()  # Collect both movie_list and real_dict

    combined_caption = "🔗 Select a Movie from the list 🎬 :\n\n🔘 Please select a movie:"
    keyboard = makeKeyboard(movie_list)

    bot.send_photo(
        chat_id=message.chat.id,
        photo='https://graph.org/file/4e8a1172e8ba4b7a0bdfa.jpg',
        caption=combined_caption,
        parse_mode='Markdown',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global real_dict
    for key, value in enumerate(movie_list):
        if call.data == f"{key}":
            if value in real_dict.keys():
                for i in real_dict[value]:
                    bot.send_message(call.message.chat.id, text=i, parse_mode='HTML')  # Changed to HTML


def makeKeyboard(movie_list):
    markup = types.InlineKeyboardMarkup()
    for key, value in enumerate(movie_list):
        markup.add(types.InlineKeyboardButton(text=value, callback_data=f"{key}"))
    return markup

def tamilmv():
    mainUrl = 'https://www.1tamilmv.moi'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }
    
    movie_list = []
    real_dict = {}
    
    web = requests.get(mainUrl, headers=headers)
    soup = BeautifulSoup(web.text, 'lxml')

    temps = soup.find_all('div', {'class': 'ipsType_break ipsContained'})
    
    if len(temps) < 21:
        return [], {}
    
    for i in range(21):
        title = temps[i].findAll('a')[0].text.strip()
        link = temps[i].find('a')['href']
        movie_list.append(title)
        
        movie_details = get_movie_details(link)
        real_dict[title] = movie_details

    return movie_list, real_dict

def get_movie_details(url):
    try:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        
        mag = [a['href'] for a in soup.find_all('a', href=True) if 'magnet:' in a['href']]
        filelink = [a['href'] for a in soup.find_all('a', {"data-fileext": "torrent", 'href': True})]

        movie_details = []
        movie_title = soup.find('h1').text.strip()  # Assuming the title is in <h1> tag

        for p in range(len(mag)):
            if p < len(filelink):
                movie_details.append(f"<b>📂 Movie Title:</b> {movie_title}\n🧲 <code>{mag[p]}</code>\n\n🗒️-> <a href='{filelink[p]}'>Torrent File Download 🖇</a>")
            else:
                movie_details.append(f"<b>📂 Movie Title:</b> {movie_title}\n🧲 <code>{mag[p]}</code>\n\n🗒️-> <a href='#'>Torrent File Download 🖇</a>")  # Placeholder if filelink not available

        return movie_details
    except Exception as e:
        print(f"Error retrieving movie details: {e}")
        return []

@app.route('/')
def health_check():
    return "Angep LOL Healthy", 200

if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.polling, kwargs={'none_stop': True}).start()
    app.run(host='0.0.0.0', port=3000)
