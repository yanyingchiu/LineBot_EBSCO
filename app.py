from typing import Text
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
userAnswer = {}

# Channel Access Token
line_bot_api = LineBotApi('My Channel Access Token')
# Channel Secret
handler = WebhookHandler('My Channel Secret')

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
    reply = TextSendMessage(text='EBSCO 小精靈看不懂你在說什麼，或是你已經作答過了！可以再告訴我一次嗎？')

    if event.source.user_id not in userAnswer:
        userAnswer[event.source.user_id] = 0

    if userAnswer[event.source.user_id] == 0:
        if event.message.text == "開始作答":
            userAnswer[event.source.user_id] = 1
            reply = [
                TextSendMessage(text='題組一：請於 EBSCO Academic Search 系列資料庫，使用關鍵字 sports injuries，找到 "Influence of Stress and Anxiety on Sports Injuries in Athletes" 這篇文章，閱讀後回答下列 2 個問題。'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/bOM44Fm.png',
                    preview_image_url='https://i.imgur.com/bOM44Fm.png'
                ),
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='問題一',
                        actions=[
                            MessageTemplateAction(
                                label='A',
                                text='我選 A',
                            ),
                            MessageTemplateAction(
                                label='B',
                                text='我選 B',
                            ),
                            MessageTemplateAction(
                                label='C',
                                text='我選 C',
                            ),
                            MessageTemplateAction(
                                label='D',
                                text='我選 D',
                            ),
                        ]
                    )
                )
            ]
    
    # 問題二
    elif userAnswer[event.source.user_id] == 1:
        if event.message.text == '我選 B':
            userAnswer[event.source.user_id] = 2
            reply = [
                TextSendMessage(text='嗚呼恭喜你答對了！\n那麼趕快來挑戰下一題吧～'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/Z3U7hGM.png',
                    preview_image_url='https://i.imgur.com/Z3U7hGM.png'
                ),
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='問題二',
                        actions=[
                            MessageTemplateAction(
                                label='A',
                                text='我選 A',
                            ),
                            MessageTemplateAction(
                                label='B',
                                text='我選 B',
                            ),
                            MessageTemplateAction(
                                label='C',
                                text='我選 C',
                            ),
                            MessageTemplateAction(
                                label='D',
                                text='我選 D',
                            ),
                        ]
                    )
                )
            ]
        elif event.message.text == '我選 A' or event.message.text == '我選 C' or event.message.text == '我選 D':
            userAnswer[event.source.user_id] = 2
            reply = [
                TextSendMessage(text='看來你不小心失誤了，但沒關係，就讓 EBSCO 小精靈來幫你解答\n\n正確答案為 B，作者所參考的 18 篇研究中，只有 2 篇採用前瞻性研究法。\n\n那麼趕快來挑戰下一題吧！'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/Z3U7hGM.png',
                    preview_image_url='https://i.imgur.com/Z3U7hGM.png'
                ),
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='問題二',
                        actions=[
                            MessageTemplateAction(
                                label='A',
                                text='我選 A',
                            ),
                            MessageTemplateAction(
                                label='B',
                                text='我選 B',
                            ),
                            MessageTemplateAction(
                                label='C',
                                text='我選 C',
                            ),
                            MessageTemplateAction(
                                label='D',
                                text='我選 D',
                            ),
                        ]
                    )
                )
            ]
    
    # 問題三
    elif userAnswer[event.source.user_id] == 2:
        if event.message.text == '我選 C':
            userAnswer[event.source.user_id] = 3
            reply = [
                TextSendMessage(text='嗚呼答對了！\n恭喜你進入下一個題組！'),
                TextSendMessage(text='題組二：請於 EBSCO Academic Search 系列資料庫，組合關鍵字 sport science AND cognitive training，找到《四肢發達頭腦卻不簡單－ 運動員與認知神經功能之研究回顧與展望》，閱讀並回答下列 2 個問題。'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/C3hjaCa.png',
                    preview_image_url='https://i.imgur.com/C3hjaCa.png'
                ),
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='問題三',
                        actions=[
                            MessageTemplateAction(
                                label='A',
                                text='我選 A',
                            ),
                            MessageTemplateAction(
                                label='B',
                                text='我選 B',
                            ),
                            MessageTemplateAction(
                                label='C',
                                text='我選 C',
                            ),
                            MessageTemplateAction(
                                label='D',
                                text='我選 D',
                            ),
                        ]
                    )
                )
            ]
        elif event.message.text == '我選 A' or event.message.text == '我選 B' or event.message.text == '我選 D':
            userAnswer[event.source.user_id] = 3
            reply = [
                TextSendMessage(text='看來你不小心失誤了，但沒關係，就讓 EBSCO 小精靈來幫你解答\n\n正確答案為 C，在摘要中有提到壓力和焦慮會影響到運動傷害發生的風險、頻率與嚴重程度。\n\n那麼趕快來挑戰下一個題組吧！'),
                TextSendMessage(text='題組二：請於 EBSCO Academic Search 系列資料庫，組合關鍵字 sport science AND cognitive training，找到《四肢發達頭腦卻不簡單－ 運動員與認知神經功能之研究回顧與展望》，閱讀並回答下列 2 個問題。'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/C3hjaCa.png',
                    preview_image_url='https://i.imgur.com/C3hjaCa.png'
                ),
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='問題三',
                        actions=[
                            MessageTemplateAction(
                                label='A',
                                text='我選 A',
                            ),
                            MessageTemplateAction(
                                label='B',
                                text='我選 B',
                            ),
                            MessageTemplateAction(
                                label='C',
                                text='我選 C',
                            ),
                            MessageTemplateAction(
                                label='D',
                                text='我選 D',
                            ),
                        ]
                    )
                )
            ]
    
    # 問題四
    elif userAnswer[event.source.user_id] == 3:
        if event.message.text == '我選 B':
            userAnswer[event.source.user_id] = 4
            reply = [
                TextSendMessage(text='嗚呼恭喜你答對了！\n那麼繼續來挑戰下一題吧～'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/v0KU5hf.png',
                    preview_image_url='https://i.imgur.com/v0KU5hf.png'
                ),
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='問題四',
                        actions=[
                            MessageTemplateAction(
                                label='A',
                                text='我選 A',
                            ),
                            MessageTemplateAction(
                                label='B',
                                text='我選 B',
                            ),
                            MessageTemplateAction(
                                label='C',
                                text='我選 C',
                            ),
                            MessageTemplateAction(
                                label='D',
                                text='我選 D',
                            ),
                        ]
                    )
                )
            ]
        elif event.message.text == '我選 A' or event.message.text == '我選 C' or event.message.text == '我選 D':
            userAnswer[event.source.user_id] = 4
            reply = [
                TextSendMessage(text='正確答案為 B，不是無氧適能，而是有氧適能喔！！\n\n論文中建議若運動訓練要運動員達到較高水準的表現，須要保持高有氧適能水準，以幫助運動員展現出較佳的認知與運動技能表現。\n高有氧適能除了可以為運動員提供好的認知功能訓練，對於非運動員的一般人也是有一定效果的助益喔，大家也可以試著在日常中增加有氧適能的訓練，看看是不是有效果～\n\n那麼趕快來挑戰下一題吧！'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/v0KU5hf.png',
                    preview_image_url='https://i.imgur.com/v0KU5hf.png'
                ),
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        text='問題四',
                        actions=[
                            MessageTemplateAction(
                                label='A',
                                text='我選 A',
                            ),
                            MessageTemplateAction(
                                label='B',
                                text='我選 B',
                            ),
                            MessageTemplateAction(
                                label='C',
                                text='我選 C',
                            ),
                            MessageTemplateAction(
                                label='D',
                                text='我選 D',
                            ),
                        ]
                    )
                )
            ]

    # 問題五    
    elif userAnswer[event.source.user_id] == 4:
        if event.message.text == '我選 B':
            userAnswer[event.source.user_id] = 5
            reply = [
                TextSendMessage(text='嗚呼恭喜你答對了！\n那麼來挑戰最後一題吧～'),
                TextSendMessage(text='在開始作答前，小精靈想請你先下載一本魔法書：EBSCO Mobile 來幫助你完成最後一題\n\n➡️ Google Play:https://play.google.com/store/apps/details?id=com.ebsco.ebscomobile\n➡️ Apple Store: https://apps.apple.com/tw/app/ebsco-mobile/id1473281170'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/dLRcULb.png',
                    preview_image_url='https://i.imgur.com/dLRcULb.png'
                ),
                TextSendMessage(text='小提示：可以使用像是 "sports injuries"（運動傷害）或是 "sport science", "cognitive training"（運動科學）等主題詞下去檢索呦！')
            ]
        elif event.message.text == '我選 A' or event.message.text == '我選 C' or event.message.text == '我選 D':
            userAnswer[event.source.user_id] = 5
            reply = [
                TextSendMessage(text='看來你不小心失誤了，但沒關係，就讓 EBSCO 小精靈來幫你解答\n\n正確答案為 B，在測量兩種不同的轉移效果時，長程轉移效果使用幾何圖型為材料刺激，而短程轉移效果則是使用運動情境作為材料刺激。\n\n那麼來挑戰最後一題吧～'),
                TextSendMessage(text='在開始作答前，小精靈想請你先下載一本魔法書：EBSCO Mobile 來幫助你完成最後一題\n\n➡️ Google Play:https://play.google.com/store/apps/details?id=com.ebsco.ebscomobile\n➡️ Apple Store: https://apps.apple.com/tw/app/ebsco-mobile/id1473281170'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/dLRcULb.png',
                    preview_image_url='https://i.imgur.com/dLRcULb.png'
                ),
                TextSendMessage(text='小提示：可以使用像是 "sports injuries"（運動傷害）或是 "sport science", "cognitive training"（運動科學）等主題詞下去檢索呦！')
            ]
    
    elif userAnswer[event.source.user_id] == 5:
        if "View in EBSCO mobile app:" in event.message.text:
            userAnswer[event.source.user_id] = 6
            reply = [
                TemplateSendMessage(
                    alt_text='Buttons template',
                    template=ButtonsTemplate(
                        thumbnail_image_url='https://i.imgur.com/B4uVWi1.png',
                        title='恭喜你全部答完了！',
                        text='接下來只要填完基本資料就能參加抽獎拉',
                        actions=[
                            URITemplateAction(
                                label='問卷連結',
                                uri='https://forms.gle/inFvRfJRhbCySJkd6'
                            )
                        ]
                    )
                )
            ]
        else:
            reply = [
                TextSendMessage(text='似乎有哪邊不對，可以參考 https://sites.google.com/view/2021ebscoacademicsearch/ebsco-mobile-%E4%BB%8B%E7%B4%B9?authuser=0\n或是跟著下圖操作呦！'),
                ImageSendMessage(
                    original_content_url='https://i.imgur.com/NftVkNz.png',
                    preview_image_url='https://i.imgur.com/NftVkNz.png'
                )
            ]

    line_bot_api.reply_message(event.reply_token,reply)
    print(userAnswer)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
