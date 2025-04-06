import requests
from django.conf import settings

def send_email_with_brevo(to_email, subject, html_content):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json",
    }
    data = {
        "sender": {
            "name": "Mon App",
            "email": settings.DEFAULT_FROM_EMAIL  # doit être validé sur Brevo
        },
        "to": [{"email": to_email}],
        "subject": subject,
        "htmlContent": html_content
    }

    response = requests.post(url, json=data, headers=headers)

    # 💡 Log si échec
    if response.status_code != 201:
        print("Erreur Brevo:", response.status_code, response.text)

    return response.status_code, response.json()
