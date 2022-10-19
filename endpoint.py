from flask import Flask, request
import requests
from threading import Thread
import sys
from main import handler
import os
import logging
app = Flask(__name__)

def send_message(chat_id, text):
    method = "sendMessage"
    token = "840446984:AAFuVTW-FYP5tJVu8mqhc9y4E0j1fr2lCD0"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        logging.info('sdfsdf')
        # logging.info(request.get_json())
        print(request.get_json(), flush=True)
        msg = {
            'id': request.get_json()['message']['chat']['id'],
            'from': request.get_json()['message']['chat']['first_name'],
            'text': request.get_json()['message']['text'],
        }
        print(msg,flush=True)
        # try:
        thread = Thread(target=handler, args = (msg, ))
        thread.start()
        # except:
        #     pass

    return {"ok": True}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)