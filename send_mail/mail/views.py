from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email(mail):
    context = {'mail': mail}
    template = get_template('mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'CodigoFacilito',
        settings.EMAIL_HOST_USER,
        [mail],  
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def index(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)

    return render(request, 'index.html', {})
