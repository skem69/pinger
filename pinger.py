import requests
import threading
import time

bot_tokens = ["token1", "token2", "token3"]

guild_id="ur guild id"

def send_messages(token):
    while True:
        channels = requests.get(f"https://discord.com/api/v9/guilds/{int(guild_id)}/channels", headers={'authorization':f'Bot {token}'}).json()
        print(channels)
        
        for channel in channels:
            if "ping" in channel["name"]:
                r = requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers={'authorization':f'Bot {token}'}, json={'content':'message you want bot to send'})
                print(r.status_code)
                time.sleep(0.5)

for token in bot_tokens:
    th = threading.Thread(target=send_messages, args=[token])
    th.start()
