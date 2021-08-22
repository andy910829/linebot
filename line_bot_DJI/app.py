from re import search
import time
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import function
from function import search, searchIXIC, searchSOX





app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('R1fJxcjD6E1aupAy7C8yEW5qdalKwA3eTSzbj5VvbS9fmHAwSRTiEQAk2hBAy0tuyDwerf/47Gt433BQa9BAJBN9u8SkQyLKo8QZv9VmOAaENWmsDxwYtQoJUOhTjfkxu+JIfl3g9GvglCr+ZNSaHwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('4a8ad6823d5408ec815c10d361e6ee3b')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "Hi" or event.message.text == "hi":
        user_id = event.source.user_id
        kw = function.getdata(search()) +'\n' + '今日道瓊指數漲跌:' + function.gethtml(search()) + '\n' + '今日費城半導體漲跌:' + function.gethtml(searchSOX()) + '\n' + '今日那斯達克漲跌:' + function.gethtml(searchIXIC())
        line_bot_api.push_message(user_id , TextSendMessage(text=kw))
            

            

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)