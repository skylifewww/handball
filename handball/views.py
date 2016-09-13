# -*- coding: utf-8 -*- 

from django.views.generic import TemplateView
from django.shortcuts import render_to_response, render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from handball.forms import *
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from article.views import return_path_f


def index(request):

    return_path_f(request)

    return render_to_response("index.html")


def about(request):

    return_path_f(request)

    return render_to_response("about.html")    


def events(request):

    return_path_f(request)

    return render_to_response("events.html")        
 
 
def gallery(request):

    return_path_f(request)

    return render_to_response("gallery.html")  


def contact(request):

    form_class = ContactForm

    return_path_f(request)

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                u"Гандбол_Шостка",
                content,
                u"Гандбол_Шостка" +'',
                ['skylifewww@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return render(request, 'contact.html', {
        'form': form_class,
    })
