

import requests
import os

# --- STEP-BY-STEP GUIDE ---
# 1. Open Telegram and search for "@BotFather".
# 2. Send "/newbot" and follow the instructions to name your bot.
# 3. BotFather will provide an API Token (e.g., 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11).
# 4. Store this token in your project's .env file:
#    TELEGRAM_BOT_TOKEN=your_token_here
# 5. Note: To send a message, you need the user's Telegram 'chat_id'. 
#    The user must first start a conversation with your bot.

def send_otp_via_telegram(chat_id, otp_code):
    """
    Sends an OTP message to a Telegram user.
    
    Args:
        chat_id: The unique Telegram ID of the recipient.
        otp_code: The generated OTP string.
    """
    # Retrieve token from environment variables for security
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        return {"success": False, "error": "Bot token not configured."}

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"Your verification code is: <b>{otp_code}</b>\nIt will expire in 5 minutes.",
        "parse_mode": "HTML"
    }

    try:
        # Send POST request to Telegram API
        response = requests.post(url, json=payload, timeout=10)
        
        # Raise an exception for HTTP errors (4xx or 5xx)
        response.raise_for_status()
        
        return {"success": True, "response": response.json()}
    
    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, or invalid responses
        return {"success": False, "error": str(e)}

# Example usage within a Django view or service:
# result = send_otp_via_telegram(user_chat_id, "123456")
# if result["success"]:
#     print("OTP Sent!")



        

