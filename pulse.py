# pulse.py
import random, json
from datetime import datetime

data = {
    "number": random.randint(1000, 9999),
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

with open("data/latest.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
