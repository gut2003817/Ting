from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('otnwe2Uebi5rpvwQxXCs4o1aD7GyWGHhU9eN47NxVE0Z8zSJWqYEhCk/uVRyAx3UsCXLRDlUh4U3K5V8zpX5O60cZt7jY2JjsmAmSlw2ScybGx8eNo03kqS6iN0ZIzxRD99RGDaAbBaTQnh0XXrU+gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f1361acece2de4839efd79f8d542e2ea')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()