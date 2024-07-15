from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import func

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))
#line_bot_api = LineBotApi("mES+lJ+ZFTtjZmMic7pAa6L47SaJX//4ywwQzg23QCRHO3x7VVpcJcwo6q8Y43AUzw3AnKRGWzuHhMg5QXqS4Okk5rAjwrd6/hhojTewa36El/bq7w/a3D8zjYC1Wk7o7LBP7+ua8eFpFS2lYr+ViAdB04t89/1O/w1cDnyilFU=")
# Channel Secret
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))
#handler = WebhookHandler("b070eac52fefe35f9c855757c8c8f4c3")

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    #加了下面這一行
    print("THE BODY: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
# event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    message = message.encode('utf-8')
    if event.message.text == "查股價":
        func.sendQuicklyReply(event)
    elif(event.message.text[7:10] == "的股價"):
        func.Stock_price(event)
    elif event.message.text == "幫我來個今日趨勢吧":
        func.sendQuicklyReply2(event)
    elif(event.message.text[7:10] == "的趨勢"):
        func.Stock_line(event)
    elif(event.message.text == "我是捷運常客"):
        message=[]
        message.append(TextSendMessage(text='請修改下行格式操作：\n（總花費是目前折扣前金額）'))
        message.append(TextSendMessage(text='趟數：28；總花費：1050'))
        line_bot_api.reply_message(event.reply_token, message)
    elif(event.message.text[0:3] == "趟數："):
        func.MRT(event)
    else:
        message =[]
        message.append(TextSendMessage(text='例外測試 !!'))
        line_bot_api.reply_message(event.reply_token, message)
    #elif(event.message.text == "趨勢圖"): 
    #回傳訊息的api
    #else: 
        #這樣可以一次回覆兩個訊息
        #message=[]
        #message.append(TextSendMessage(text='收到的工作內容為：'))
        #message.append(TextSendMessage(text='水煎包'))
        #line_bot_api.reply_message(event.reply_token, message)
        


import os
if __name__ == "__main__":
    print('work')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
