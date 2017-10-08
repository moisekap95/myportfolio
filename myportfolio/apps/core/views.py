from django.views.generic import ListView
from apps.services.models import Service
from apps.texts.models import Text
from apps.works.models import Work
from apps.skills.models import Skill
from apps.categories.models import Category

#Email packages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

#Form
from . import forms

class IndexView(ListView):
    context_object_name = 'works'
    #model = Work
    template_name = 'core/index.html'
    queryset = Work.objects.all()

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['texts'] = Text.objects.all()
        context['services'] = Service.objects.all()
        context['works'] = Work.objects.all()
        context['skills'] = Skill.objects.all()
        context['categories'] = Category.objects.all()
        context['contact_form'] = forms.ContactForm
        return context


def send_email_view(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    if request.method == 'POST':   
        try:
            send_mail(subject, message  + '\n ' + name, email, ['moisekapanda@gmail.com'])
            return render(request, 'core/email_sent.html', {'name':name})
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
