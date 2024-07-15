from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
import os
import json

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))

def age(event):
      # Flex Message Simulator網頁：https://developers.line.biz/console/fx/
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/3788/3788610.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "1. 您的年齡",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 20 ~ 29",
            "text": "我的年齡落在20~29歲 - 1"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 30 ~ 39",
            "text": "我的年齡落在30~39歲 - 1"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "C. 40 ~ 49",
            "text": "我的年齡落在40~49歲 - 2"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "D. 50 ~ 59",
            "text": "我的年齡落在50~59歲 - 3"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "E. 60 ~ 69",
            "text": "我的年齡落在60~69歲 - 2"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "F. 70歲以上",
            "text": "我的年齡落在70歲以上 - 1"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第1題輸入錯誤，請重新輸入'))

def salary(event):
      # Flex Message Simulator網頁：https://developers.line.biz/console/fx/
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/3135/3135706.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "2. 您的收入來源",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 固定收入(年、月薪)",
            "text": "我是屬於固定收入 - 3"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 非固定收入(接案)",
            "text": "我是屬於非固定收入 - 2"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第2題輸入錯誤，請重新輸入'))

def education(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/2987/2987903.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "3. 您的教育程度",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 國小(含)以下",
            "text": "我的教育程度約在國小(含)以下"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 國中",
            "text": "我的教育程度約在國中"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 高中職/專科",
            "text": "我的教育程度約在高中職/專科"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 大學",
            "text": "我的教育程度約在大學"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "E. 碩士/博士",
            "text": "我的教育程度約在碩士/博士"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第3題輸入錯誤，請重新輸入'))

def income(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/893/893104.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "4. 您的年收入約為?",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 50萬以下",
            "text": "我的年收入約在50 萬以下"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 50 萬(含)〜100 萬",
            "text": "我的年收入約在50 萬(含)〜100 萬"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 100 萬(含)〜150 萬",
            "text": "我的年收入約在100 萬(含)〜150 萬"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 150 萬(含)〜200 萬",
            "text": "我的年收入約在150 萬(含)〜200 萬"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "E. 200 萬(含)以上",
            "text": "我的年收入約在200 萬(含)以上"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第4題輸入錯誤，請重新輸入'))

def disease(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/4599/4599010.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "5. 是否有重大傷病證明？",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 是",
            "text": "是"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 否",
            "text": "否"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第5題輸入錯誤，請重新輸入'))

def invest_year(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/2910/2910282.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "6.	請問您的投資經驗為？",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 未滿 1 年",
            "text": "我的投資經驗未滿 1 年"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 1 年(含)以上〜未滿 3 年",
            "text": "我的投資經驗約在1 年(含)以上〜未滿 3 年"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 3 年(含)以上〜未滿 5 年",
            "text": "我的投資經驗約在3 年(含)以上〜未滿 5 年"
            },
            "gravity": "center"
        },
                {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 5 年(含)以上〜未滿 10 年",
            "text": "5 年(含)以上〜未滿 10 年"
            },
            "gravity": "center"
        },
                {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "E. 10 年(含)以上",
            "text": "我的投資經驗約在10 年(含)以上"
            },
            "gravity": "center"
        },
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第6題輸入錯誤，請重新輸入'))

def money_from(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/2145/2145230.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "7. 您的投資金額來源為何？",
            "weight": "bold",
            "size": "lg",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 薪資收入",
            "text": "我的資金來自薪資收入"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 投資所得",
            "text": "我的資金來自投資所得"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 閒置資金",
            "text": "我的資金來自閒置資金"
            },
            "gravity": "center"
        },
                {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 租金/利息收入/退休金",
            "text": "我的資金來自租金/利息收入/退休金"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第7題輸入錯誤，請重新輸入'))

def invest_period(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/1497/1497835.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "8. 您預計的投資期間為何?",
            "weight": "bold",
            "size": "lg",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 1年以內",
            "text": "我的投資期間約為1年以內"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 1年(含)~3年",
            "text": "我的投資期間約為1年(含)~3年"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 3年(含)~5年",
            "text": "我的投資期間約為3年(含)~5年"
            },
            "gravity": "center"
        },
                {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 5年(含)以上",
            "text": "我的投資期間約為5年(含)以上"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第8題輸入錯誤，請重新輸入'))

def invest_method(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/2857/2857511.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "9. 您偏好哪種投資方式?",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 短線投機",
            "text": "我偏好短線投機"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 波段操作",
            "text": "我偏好波段操作"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 長期持有",
            "text": "我偏好長期持有"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第9題輸入錯誤，請重新輸入'))

def invest_goal(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/3233/3233497.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "10. 您的投資目的為何？",
            "weight": "bold",
            "size": "xl",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 提早享受退休生活",
            "text": "我想要提早享受退休生活"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 獲得人生的第一桶金",
            "text": "我想要獲得人生的第一桶金"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 財產保值",
            "text": "我想要讓財產保值"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 小孩教育資金",
            "text": "我想要存小孩教育資金"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "E. 買下屬於自己的房子",
            "text": "我想要買下屬於自己的房子"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "F. 累積長期財富",
            "text": "我想要累積長期財富"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第10題輸入錯誤，請重新輸入'))

def loss(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/3309/3309996.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "11. 您最多能承擔下跌多少金額？",
            "weight": "bold",
            "size": "md",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 5%",
            "text": "我能忍受損失5%"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 10%",
            "text": "我能忍受損失10%"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 15%",
            "text": "我能忍受損失15%"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 20%以上",
            "text": "我能忍受損失20%以上"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第11題輸入錯誤，請重新輸入'))

def unexpected(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/1768/1768400.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "12. 當超過預設停損停利點，",
            "weight": "bold",
            "size": "lg",
            "style": "normal",
            "decoration": "none"
        },
        {
        "type": "text",
        "text": "你會採取何種方式？",
        "size": "lg",
        "weight": "bold",
        "align": "center"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 立即賣出所有部位",
            "text": "我會立即賣出所有部位"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 先賣出一半或一半以上部位 ",
            "text": "我會先賣出一半或一半以上部位 "
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 先賣出一半以內部位",
            "text": "我會先賣出一半以內部位"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 暫時觀望，視情況再因應",
            "text": "我會暫時觀望，視情況再因應"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "E. 繼續買進部位",
            "text": "我會繼續買進部位"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第12題輸入錯誤，請重新輸入'))

def portfolio(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://i.imgur.com/BLIUjsK.jpg",
        "backgroundColor": "#ffffff"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
        "type": "text",
        "text": "13. 假設有四種投資組合，",
        "weight": "bold",
        "size": "lg"
        },
        {
        "type": "text",
        "text": "您會選擇哪一個投資？",
        "size": "lg",
        "weight": "bold",
        "align": "center"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 投資組合A",
            "text": "投資組合A"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 投資組合B ",
            "text": "投資組合B"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 投資組合C",
            "text": "投資組合C"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 投資組合D",
            "text": "投資組合D"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "E. 投資組合E",
            "text": "投資組合E"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第13題輸入錯誤，請重新輸入'))

def frequency(event):
    try:
        flex_message = FlexSendMessage(
                alt_text='KYC測驗',
                contents={
    "type": "bubble",
    "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        },
        "url": "https://cdn-icons-png.flaticon.com/512/690/690466.png",
        "backgroundColor": "#3D59AB"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "14. 您多久看一次投資的狀況？",
            "weight": "bold",
            "size": "lg",
            "style": "normal",
            "decoration": "none"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "A. 每天",
            "text": "我平均每天看一次"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "B. 三天 ",
            "text": "我平均三天看一次"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "C. 每週",
            "text": "我平均每週看一次"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "D. 半個月",
            "text": "我平均半個月看一次"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "E. 一個月",
            "text": "我平均一個月看一次"
            },
            "gravity": "center"
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "message",
            "label": "F. 一個月以上",
            "text": "我平均一個月以上才會看一次"
            },
            "gravity": "center"
        }
        ],
        "flex": 0
    }
    }
                )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage('第14題輸入錯誤，請重新輸入'))

def amount(event):
    try:
        line_bot_api.reply_message(event.reply_token,
                                    TextSendMessage(
                                    text='15. 您初次預計投入多少資金投資?(輸入規則：我要投入+金額(單位：台幣)，e.g. 我要投入10000)')
                                    )
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='第15題輸入錯誤，請重新輸入'))

def end(event):
    line_bot_api.reply_message(event.reply_token,
                                TextSendMessage(
                                text='您已完成測驗!')
                                )
