from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/get/*": {"origins": "*"}})

english_bot = ChatBot("English Bot")
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/")
def index():
    query = request.args.get('message')
    return str(english_bot.get_response(query))


if __name__ == "__main__":
    app.run()