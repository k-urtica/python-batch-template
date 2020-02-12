import env
import json
import requests


def slack_notice(text, icon=None):
    """slackへ通知を発信する
    Arguments:
        text {string} -- 通知するメッセージテキスト
    Keyword Arguments:
        icon {string} -- 通知アイコン (default: {None})
    """
    url = env.SLACK_WEBHOOK
    requests.post(url, data=json.dumps({"icon_emoji": icon, "text": text}))
