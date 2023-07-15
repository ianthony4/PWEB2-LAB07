from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hola de Anthony Chaisa para el Laboratorio 7', 
                'Hola, esto es un mensaje automatico de PWEB2',
                'anthonyleo2001@gmail.com',
                ['wosoke8405@kameili.com'],
                fail_silently=False)
    
    return render('send/index.html')