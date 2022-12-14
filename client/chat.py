from utils import set_timeout, fetch

last_seen_id = 0
# Находим элементы интерфейса по их ID
send_message = document.getElementById("send_message")
sender = document.getElementById("sender")
message_text = document.getElementById("message_text")
chat_window = document.getElementById("chat_window")

# Добавляет новое сообщение в список сообщений
def append_message(message):
    # Создаем HTML-элемент представляющий сообщение
    item = document.createElement("li")  # li - это HTML-тег для элемента списка
    item.className = "list-group-item"   # className - определяет как элемент выглядит
    # Добавляем его в список сообщений (chat_window)
    item.innerHTML = f'[<b>{message["sender"]}</b>]: <span>{message["text"]}</span><span class="badge text-bg-light text-secondary">{message["time"]}</span>'
    chat_window.prepend(item)

# Вызывается при клике на send_message
async def send_message_click(e):
    # Отправляем запрос
    await fetch(f"/send_message?sender={sender.value}&text={message_text.value}", method="GET")
    # Очищаем поле
    message_text.value = ""


# Загружает новые сообщения с сервера и отображает их
async def load_fresh_messages():
    # 1. Загружать все сообщения каждую секунду (большой трафик)
    result = await fetch("/get_messages", method="GET")  # Делаем запрос
    chat_window.innerHTML = ""  # Очищаем окно с сообщениями
    data = await result.json()
    all_messages = data["messages"]  # Берем список сообщений из ответа сервера
    for msg in all_messages:
        append_message(msg)
    set_timeout(1, load_fresh_messages) # Запускаем загрузку заново через секунду
    # 2. Загружать только новые сообщения


# Устнаваливаем действие при клике
send_message.onclick = send_message_click
append_message({"sender":"MIKE", "text":"Add Message Works!!!", "time": "25:88"})
load_fresh_messages()


# from utils import set_timeout, fetch
#
# last_seen_id = 0
# send_message = document.getElementById("send_message")
# sender - document.getElementById("sender")
# message_text = document.getElementById("message_text")
#
# # append_message добавлять новые соьбщение в сообщения
# def append_message(message):
#     # создает HTML element  представляющий код # document - то с чем мы работаем
#     item - document.createElement("li") # li - html тэк для элемента списка
#     item.className = "list-group-item" # className 0- определяет как элемент выглядит
#     # добюавляем его в спимок сообщений (chat_window)
#     #item.innerHTML = f"[<b>Mike</b>]: <span>Text</span> <span class= \"bage text-bg-dark\">Time</span>"
#
# # вызввается при клике на  send_message
# async def send_message_click(e):
#     # функция должна отправить запрос к странице /send_message
#     await fetch(f"/send_message?sender=Mike&text=Hello", method="GET")
#     send_message.value = ""
#
# # Загружает и отображает новые сообщение с сервера
# async def load_fresh_messages():
#     pass
#     # global last_seen_id
#     # result = await fetch(f"/get_messages?after={last_seen_id}", method="GET")
#     # payload = await result.json()
#     # messages = payload["messages"]
#     # for message in messages:
#     #     msg_id = message["msg_id"]
#     #     if msg_id >= last_seen_id:
#     #         last_seen_id = msg_id + 1
#     #     append_message(message)
#     # set_timeout(2, load_fresh_messages)
#
#
# # Установили действие при клике
# send_message.onclick = send_message_click
#
# # Позволяет запгружать сообщения за 1 сек
# set_timeout(2, load_fresh_messages)
