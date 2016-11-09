# -*- coding: utf-8 -*- 

from django.views.generic import TemplateView
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from handball.forms import *
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from content.models import Players



def index(request):

    players = Players.objects.all()
    players_all = []
    length = int(len(players)/4)
    for i in range(length):
        arr = []
        for j in range(4):
            arr.append(players[i * 4 + j])
        players_all.append(arr)    



    return render_to_response("index.html", {'page': 1, 'players_all': players_all, 'length': length})


def about(request):

    

    return render_to_response("about.html", {'page': 2})    


def events(request):


    return render_to_response("events.html", {'page': 3})        
 
 
def gallery(request):

  

    return render_to_response("gallery.html", {'page': 4})  


def contact(request):

    form_class = ContactForm


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
        'form': form_class, 'page': 5
    })
