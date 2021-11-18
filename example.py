import admier
import json

# Edit or delete this line
config = json.load(open("config/auth.json"))

# Your group_id is here
group_id = config["group_id"]

# Your access_token is here
access_token = config["access_token"] 

def handle(event):
    if not(event["updates"]) or not(event["updates"][0]["type"] == "message_new"): return

    params = {
        "peer_id": event["updates"][0]["object"]["message"]["peer_id"],
        "random_id": 0,
        "message": "Hello World!"
    }
    bot.request("messages.send", params)

bot = admier.Client(group_id, access_token)
bot.connect(handle)