from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email(data):
    context = {'data': data}
    template = get_template('mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'testing',
        settings.EMAIL_HOST_USER,
        [ data['mail'] ],  
    )

    email.attach_alternative(content, 'text/html')
    email.send()


def index(request):
    if request.method == 'POST':
        #mail = request.POST.get('my-form')
        data = request.POST.items() 
        send_email(dict(data))

    return render(request, 'index.html', {})
