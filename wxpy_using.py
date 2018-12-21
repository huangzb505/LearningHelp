import json
import requests
from wxpy import *


def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "f8f5bdf83b0b416a8534c6ddf9996e1c"
    payload = {
        "info": text,
        "key": api_key,
        "userId": "1038103831"

    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result["text"]


bot = Bot(cache_path=True)


@bot.register(except_self=True)
def forward_message(msg):
    return auto_reply(msg.text)


embed()
