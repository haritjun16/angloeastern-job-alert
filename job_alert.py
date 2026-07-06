import requests
from bs4 import BeautifulSoup
import os

url = "https://apply.workable.com/angloeastern/"

html = requests.get(url).text

if "job" in html.lower():
    requests.post(
        f"https://api.telegram.org/bot{os.environ['TELEGRAM_BOT_TOKEN']}/sendMessage",
        data={
            "chat_id": os.environ["TELEGRAM_CHAT_ID"],
            "text": "✅ Anglo-Eastern careers page checked successfully."
        },
    )
