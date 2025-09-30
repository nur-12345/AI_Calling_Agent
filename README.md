# AI Voice Calling Agent 📞

This project demonstrates how to build an **AI-powered voice calling system** using [Vapi](https://vapi.ai/), Python, and Twilio integration.  
It automatically reads phone numbers from a CSV file and makes outbound calls using an AI assistant.

---

## 🚀 Features
- Reads customer name and phone number from `demo.csv`
- Formats phone numbers automatically (+91 prefix for India if missing)
- Calls customers using **Vapi AI assistant**
- Secure API keys using `.env`
- Simple and extendable Python code

---

## 📂 Project Structure

    ├── main.py # Main Python script
    ├── demo.csv # Sample CSV file with names and phone numbers
    ├── .env # API keys and secrets (not pushed to GitHub)
    ├── .gitignore # Ignore sensitive files and venv
    └── venv/ # Virtual environment (ignored)

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   
Create virtual environment


    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

    
Install dependencies

    pip install -r requirements.txt
    
Setup .env file

    API_KEY=your_api_key_here
    ASSISTANT_ID=your_assistant_id_here
    PHONE_NUMBER_ID=your_phone_number_id_here

    
Prepare CSV (demo.csv)

Name, Phone Number
John, 1234567890

Alice, 9876543210

Run script

    python main.py

    
📦 Requirements

    Python 3.8+
    Packages: requests, python-dotenv
    
Install manually:

pip install requests python-dotenv
Or via requirements.txt:
pip install -r requirements.txt


🔒 Security Notes

    Never commit .env or real phone numbers to GitHub.
    Use .gitignore to exclude sensitive files.

👩‍💻 Author

Nupur Shivani
