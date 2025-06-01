import requests

WEBHOOK_URL = 'https://webhook.site/your-webhook-url'  # замените

def send_signal(signal):
    payload = {"signal": signal}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"Signal sent: {signal}, Status: {response.status_code}")
    except Exception as e:
        print(f"Webhook error: {e}")