from flask import Flask, request
import requests
from threading import Thread
import sys
from main import handler
import os
import logging

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_update():
    if request.method == "POST":
        logging.info('API call')
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
