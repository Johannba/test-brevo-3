from django.shortcuts import render
from django.http import JsonResponse
from .service import send_email_with_brevo

def send_test_email(request):
    status, data = send_email_with_brevo(
        to_email="assancode@gmail.com",
        subject="Hello depuis l'API Brevo 🚀",
        html_content="<h1>Bienvenue sur notre plateforme</h1><p>Ceci est un test !</p>"
    )
    return JsonResponse({"status": status, "response": data})

