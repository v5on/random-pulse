import json
import os
from datetime import datetime
import random
import pytz

# ✅ ডেটা ফোল্ডার তৈরি করা
os.makedirs("data", exist_ok=True)

# ✅ এলোমেলো সংখ্যা তৈরি
number = random.randint(1000, 9999)

# ✅ বাংলাদেশ টাইমজোনে সময় নেওয়া
tz = pytz.timezone("Asia/Dhaka")
timestamp = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

# ✅ JSON ডেটা লেখা
data = {
    "number": number,
    "timestamp": timestamp
}

with open("data/latest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"সংখ্যা {number} তৈরি হয়েছে সময়: {timestamp}")
