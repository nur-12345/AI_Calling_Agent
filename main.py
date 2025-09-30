import csv
import requests
import time
import os
from dotenv import load_dotenv

# 🔹 Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

def make_call(phone_number, name=None):
    url = "https://api.vapi.ai/call"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "assistantId": ASSISTANT_ID,
        "type": "outboundPhoneCall",
        "customer": {
            "number": phone_number,
            "name": name if name else "Customer"
        },
       "phoneNumberId": PHONE_NUMBER_ID
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        data = response.json()
    except:
        data = response.text
    print(f"📞 Calling {phone_number} -> {data}")

# CSV se numbers read karna
with open("demo.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        phone = row['Phone Number']
        name = row.get('Name', None)

        # ✅ Clean and format number
        phone = phone.strip().replace(" ", "")
        if not phone.startswith("+"):
            phone = "+91" + phone

        print(f"📞 Final dialing number: {phone}")  # Debugging

        make_call(phone, name)
        time.sleep(2)  # 2 sec gap between calls