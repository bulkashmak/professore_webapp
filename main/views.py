from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from .models import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import BadHeaderError
import urllib
import json
from preferences import preferences

GOOGLE_RECAPTCHA_SECRET_KEY = '6LeFjogUAAAAAFgAicrvSyBw5WbYFtkn5O-QQOR8'

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'main/main.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AboutView(generic.TemplateView):
    template_name = 'main/about.html'


def contact(request):
    form = ContactForm(request.POST)

    if request.method == 'POST':
        messages = []
        errors = []
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                subject = 'Заявка на бронирование столика'

                context = {
                    'name': form.cleaned_data['name'],
                    'phone': form.cleaned_data['phone'],
                    'guests': form.cleaned_data['guests'],
                    'message': form.cleaned_data['message'],

                }

                html = render_to_string('main/includes/admin-email.html', context)

                recipients = [preferences.PrPreferences.admin_email]

                try:
                    msg = EmailMessage(subject, html, to=recipients, from_email='manager@professore.ru')
                    msg.content_subtype = 'html'
                    msg.send()

                except BadHeaderError:
                    return render(request, 'main/contact.html', {'form': form, 'errors': ['Неверный заголовок']})

                messages.append('Спасибо. Ваше сообщение отправлено.')

                return render(request, 'main/contact.html', {'form': form, 'messages': messages})

            else:
                errors.append('<i class="fas fa-arrow-up"></i> Докажите, что вы не робот')
                return render(request, 'main/contact.html',
                              {'form': form, 'errors': errors})

        else:
            errors.append('Пожалуйста, проверьте форму на ошибки')
            return render(request, 'main/contact.html',
                          {'form': form, 'errors': errors})

    else:
        return render(request, 'main/contact.html', {'form': form})