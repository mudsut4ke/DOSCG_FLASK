from flask import request, abort, current_app

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)


line_bot_api = LineBotApi(current_app.config["LINE_DOSCG_ACCESS_TOKEN"])
handler = WebhookHandler(current_app.config["LINE_DOSCG_CHANNEL_SECRET"])


def line_callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if "test" not in event.message.text:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )
    elif event.source.type == "user":
        profile = line_bot_api.get_profile(event.source.user_id)
        text = "Received messages that do not match the conditions of the bot from {} \n\n '{}'".format(
            profile.display_name, event.message.text
        )
        line_bot_api.push_message(
            current_app.config["LINE_DOSCG_ADMIN_KEY"],
            TextSendMessage(text=text),
        )
    else:
        pass
