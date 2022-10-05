from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__, static_folder="./client", template_folder="./client")  # Настройки приложения

msg_ID = 1
all_messages = []


@app.route("/chat")
def chat_page():
    return render_template("chat.html")


def add_message(sender, text):
    global msg_ID
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M"),
        "msg_ID": msg_ID
    }
    msg_ID += 1
    all_messages.append(new_message)


# API для получения списка сообщений
# будем просить сервер дать только новые сообщения /get_messages?after=0 /get_messages?after=5
@app.route("/get_messages")
def get_messages():
    after = int(request.args['after'])
    return {"messages": all_messages[after:]}  # Делаем СЛАЙС - отрезать кусочек. Взять всё после сообщения after


# API для получения отправки сообщения  /send_message?sender=Mike&text=Hello
@app.route("/send_message")
def send_message():
    sender = request.args["sender"]
    text = request.args["text"]

    if len(sender) < 3 or len(sender) > 100:
        add_message('<font color="red">SYSTEM</font>', 'Invalid Name')
        return {"result": False, "Error": "Invalid Name"}
    elif len(text) < 1 or len(text) > 3000:
        add_message('<font color="red">SYSTEM</font>', 'Invalid Message')
        return {"result": False, "Error": "Invalid Message"}
    else:
        add_message(sender, text)
        return {"result": True}


# Главная страница
@app.route("/")
def hello_page():
    return "<br><br><center><h1><a href=\"/chat\">Chat</a><br><a href=\"/info\">INFO</a> </h1></center>"


@app.route("/info")
def info_page():
    info = len(all_messages)
    return f"<br><br><center><h1> Количество сообщений: {info} <br> <a href=\"/chat\">Chat</a> </h1></center>"

# app.run() по умолчанию - запускается локально на порту 5000 (127,0,0,1)
app.run() # 80 стандартный порт для ХТТП, что бы не вводить порт
