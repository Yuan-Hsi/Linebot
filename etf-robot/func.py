from linebot import LineBotApi
from linebot.models import *
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pandas as pd
import os
import pyimgur
import json
import matplotlib.pyplot as plt


chrome_options = webdriver.ChromeOptions()
#chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")#無頭模式
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("window-size=1400,600")


line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))
#line_bot_api = LineBotApi("mES+lJ+ZFTtjZmMic7pAa6L47SaJX//4ywwQzg23QCRHO3x7VVpcJcwo6q8Y43AUzw3AnKRGWzuHhMg5QXqS4Okk5rAjwrd6/hhojTewa36El/bq7w/a3D8zjYC1Wk7o7LBP7+ua8eFpFS2lYr+ViAdB04t89/1O/w1cDnyilFU=")

def sendText(event):
    try:
        message = TextSendMessage(
            text='喔欸喔欸！'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def sendQuicklyReply(event):
    try:
        message = []
        message.append(TextSendMessage(text='輸入格式：'))
        message.append(TextSendMessage(
            text='我想要 + 請輸入公司代碼 + 的股價',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='台積電', text='我想要2330的股價')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='聯發科', text='我想要2454的股價')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='鴻海', text='我想要2317的股價')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='聯電', text='我想要2303的股價')
                    ),
                     QuickReplyButton(
                        action=MessageAction(label='台達電', text='我想要2308的股價')
                    ),
                      QuickReplyButton(
                        action=MessageAction(label='台塑', text='我想要1301的股價')
                    ),
                      QuickReplyButton(
                        action=MessageAction(label='中華電', text='我想要2412的股價')
                    ),
                        QuickReplyButton(
                        action=MessageAction(label='南亞', text='我想要1303的股價')
                    ),
                         QuickReplyButton(
                        action=MessageAction(label='中信金', text='我想要2891的股價')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='大立光', text='我想要3008的股價')
                    ),
                ]
            )
        ))
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))


def nothing(event):
    try:
        message = TextSendMessage(
            text='好喔掰掰！'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def exchangeRate(event):
    try:
        response = requests.get('https://tw.rter.info/capi.php')
        currency = response.json()
        usdToTwd = currency['USDTWD']['Exrate']
        message = TextSendMessage(
            text=f"美元 USD 對台幣 TWD: \n1 : {usdToTwd}"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def Stock_price(event):
    try:
        stock = event.message.text[3:7]
        url = 'https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.stockList;autoRefresh=1631158268949;fields=avgPrice%2Corderbook;symbols='+stock+'.TW?bkt=tw-qsp-exp-no4&device=desktop&ecma=modern&feature=ecmaModern%2CuseVersionSwitch%2CuseNewQuoteTabColor%2ChideMarketInfo&intl=tw&lang=zh-Hant-TW&partner=none&prid=1qd9j1pgjivr5&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1138&returnMeta=true'
        res = requests.get(url)
        price = float(res.json()['data'][0].get('price').get('raw'))
        high = float(res.json()['data'][0].get('regularMarketDayHigh').get('raw'))
        low = float(res.json()['data'][0].get('regularMarketDayLow').get('raw'))
        open_p = float(res.json()['data'][0].get('regularMarketOpen').get('raw'))
        close = float(res.json()['data'][0].get('regularMarketPreviousClose').get('raw'))
        volum = float(res.json()['data'][0].get('volumeK').get('raw'))
        up_down = (price - close) / price
        up_down = str(round(up_down*100,2)) + '%'

        price_name = ['成交','漲跌','數量','開盤','收盤','最高','最低']
        price_list = [str(price),up_down,volum,open_p,close,high,low]

        dict = {"名稱": price_name,  "價格": price_list}
        st = pd.DataFrame(dict).to_string()
        message = TextSendMessage(
            text="您要的" + stock + "\n" + st
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def sendQuicklyReply2(event):
    try:
        message = []
        message.append(TextSendMessage(text='輸入格式：'))
        message.append(TextSendMessage(
            text='我想要 + 請輸入公司代碼 + 的趨勢',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='台積電', text='我想要2330的趨勢')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='聯發科', text='我想要2454的趨勢')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='鴻海', text='我想要2317的趨勢')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='聯電', text='我想要2303的趨勢')
                    ),
                     QuickReplyButton(
                        action=MessageAction(label='台達電', text='我想要2308的趨勢')
                    ),
                      QuickReplyButton(
                        action=MessageAction(label='台塑', text='我想要1301的趨勢')
                    ),
                      QuickReplyButton(
                        action=MessageAction(label='中華電', text='我想要2412的趨勢')
                    ),
                        QuickReplyButton(
                        action=MessageAction(label='南亞', text='我想要1303的趨勢')
                    ),
                         QuickReplyButton(
                        action=MessageAction(label='中信金', text='我想要2891的趨勢')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='大立光', text='我想要3008的趨勢')
                    ),
                ]
            )
        ))
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def Stock_line(event):
    try:
        stock = event.message.text[3:7]
        url = 'https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22'+stock+'.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true'
        res = requests.get(url)
        jd = res.json()['data']
        close = jd[0]['chart']['indicators']['quote'][0]['close']
        volume = jd[0]['chart']['indicators']['quote'][0]['volume']
        timestamp = jd[0]['chart']['timestamp']
        df = pd.DataFrame({'timestamp': timestamp, 'price':close})
        df2 = pd.DataFrame({'timestamp': timestamp, 'volume':volume})
        df['dt'] = pd.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')
        df2['dt'] = pd.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')
        fig, axes = plt.subplots(nrows=2, ncols=1)
        df.plot('dt', 'price', figsize = [20,10],ax=axes[0],sharex=False)
        df2.plot('dt','volume',figsize = [10,10],ax=axes[1],rot=90,sharex=False)
        plt.xticks(color='w')
        time.sleep(2)
        plt.savefig('plot.png')
        
        CLIENT_ID = "8365e4897d408bf"
        PATH = 'plot.png' #A Filepath to an image on your computer"
        title = "Uploaded with PyImgur"
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title=title)
        os.remove('plot.png')
        time.sleep(2)
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url= uploaded_image.link, preview_image_url= uploaded_image.link ))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))


def MRT(event):
    try:
        Text = event.message.text
        li = Text.split("：")
        money = int(li[2]) ##在此輸入您的目前花費
        times = int(li[1].split("；")[0]) ##在此輸入您的目前趟數
        ot = times
        discount = 0
        level = 1
        message=[]
        if times > 10 and times <= 50:
            discount = 0.05
            while times > 10:
                discount +=0.05
                times -= 10
                level += 1
        elif (times>50):
            message.append(TextSendMessage(text="大於50趟數，無套利空間喔!"))
        discount_value = money * discount
        expense = money - discount_value
        discount += 0.05
        level = level * 10 + 1
        money = money+(level-ot)*20
        discount_value_l = money * discount
        expense_l = money - discount_value_l
        if ot < 51:
            if((expense-expense_l)>0):
                message.append(TextSendMessage(text="恭喜有套利機會喔！！"))
                message.append(TextSendMessage(text="原先折扣完花費：%d \n 若你再多搭 %d 趟20元車程 \n 你的折扣完花費將會成為：%d" %(expense ,(level-ot) ,expense_l)))
            else:
                message.append(TextSendMessage(text="目前還沒有套利機會，真可惜！"))
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))
