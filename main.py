from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__, static_folder="./client", template_folder="./client")  # Настройки приложения

all_messages = []


@app.route("/chat")
def chat_page():
    return render_template("chat.html")


def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M")
    }
    all_messages.append(new_message)


# API для получения списка сообщений
@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


# API для получения отправки сообщения  /send_message?sender=Mike&text=Hello
@app.route("/send_message")
def send_message():
    sender = request.args["sender"]
    text = request.args["text"]
    add_message(sender, text)
    return {"result": True}


# Главная страница
@app.route("/")
def hello_page():
    return "New text goes here"


app.run()