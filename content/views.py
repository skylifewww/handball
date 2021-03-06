# -*- coding: utf-8 -*-

from django.http.response import Http404
from django.shortcuts import render_to_response, redirect
from content.models import *
from content.templatetags.content_tags import load_related_m2m
from django.core.exceptions import ObjectDoesNotExist
# from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
# from django.contrib.auth.models import User
# from iosDevCourse.users.models import User
from django.template import loader, Context, RequestContext

# from django.db import models
# from django.http import HttpResponse
# from django.template import Context, loader
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
# from django.shortcuts import redirect, render, get_object_or_404
# from content.models import *

# from slideshow.models import *
# from django.core.mail import send_mail, EmailMessage
# from turn.models import EmailTurn, SmsTurn
# from suds.client import Client


def raspisanie(request):
    
    all_plays = Play.objects.all()    

    load_related_m2m(all_plays, 'team')
    load_related_m2m(all_plays, 'enemy_team')
    load_related_m2m(all_plays, 'place_game')

    return render_to_response("plays.html", {"all_plays": all_plays, "page": 6})   


def plays(request, cat_play_id):
    
    current_cat_play = Cat_play.objects.get(id=cat_play_id)
    all_plays = Play.objects.filter(cat_play_id=current_cat_play.id)    

    load_related_m2m(all_plays, 'team')
    load_related_m2m(all_plays, 'enemy_team')
    load_related_m2m(all_plays, 'place_game')

    return render_to_response("plays.html", {"all_plays": all_plays, "cat_play": current_cat_play})   



def force(request):

    # args = {}
    # args['works'] = Works.objects.all()
    # args['username'] = auth.get_user(request).username     
 

    return render_to_response("force.html")







# def clear_cache(request):
#     cache.clear()
#     return redirect('/')



# def home(request):
    
    

#     return render(request, 'index.html', )
    



# def callback(request):
#     if 'name' in request.POST:
#         name = unicode(request.POST['name'])
#     else:
#         name = '__'
#     tel = str(request.POST['tel'])
    
#     e = EmailTurn(name=u'Заказ ювелирки', to='yrki@inbox.ru', title=u"Заказ ювелирки %s" % tel, text=u'Контактное лицо: %s \nТелефон: %s' %(name, tel))
#     e.save()
#     e = EmailTurn(name=u'Заказ ювелирки', to='zolotiryki@gmail.com', title=u"Заказ ювелирки %s" % tel, text=u'Контактное лицо: %s \nТелефон: %s' %(name, tel))
#     e.save()

#     s = SmsTurn(name=name,to='+380934996314', text=u'Контактное лицо: %s \nТелефон: %s' %(name, tel))
#     s.save()

    
#     import threading
#     t = threading.Thread(target=send_messages)
#     t.start()
#     return HttpResponse("ok")



# def send_messages():
#     e = EmailTurn.objects.filter(published=0)
#     s = SmsTurn.objects.filter(published=0)
    
#     for i in e:
#         try:
#             msg = EmailMessage(i.title, i.text, u"jcdeesign@gmail.com", [u"webmagic@mail.ua", i.to])
#             msg.content_subtype = "html"
#             msg.send()
#             i.published = 1
#             i.save()
#         except:
#             pass
    
#     for i in s:
#         try:
#             client = Client('http://turbosms.in.ua/api/wsdl.html')
#             r = client.service.Auth(login='osvita',password='1qaz2wsx')
#             r = client.service.SendSMS(sender='SheekComUa',destination='+'+i.to, text=i.text)
#             i.published = 1
#             i.save()
#         except:
#             pass
    
