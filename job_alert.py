import json
import os
import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

API = "https://apply.workable.com/api/v3/accounts/angloeastern/jobs"

r = requests.get(API)
r.raise_for_status()
jobs = r.json()["results"]

titles = [f'{j["title"]} - {j["location"]["city"]}' for j in jobs]

try:
    with open("jobs.json", "r") as f:
        old = json.load(f)
except:
    old = []

new_jobs = [j for j in titles if j not in old]

if new_jobs:
    text = "🚢 New Anglo-Eastern vacancy!\n\n" + "\n".join(new_jobs)
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

with open("jobs.json", "w") as f:
    json.dump(titles, f)
