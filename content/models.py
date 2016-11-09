# -*- coding: utf-8 -*-
from django.db import models

import random
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
import datetime
import mptt
from mptt.fields import TreeForeignKey



def make_upload_path(instance, filename, prefix = False):
    # Переопределение имени загружаемого файла.
    n1 = random.randint(0,10000)
    n2 = random.randint(0,10000)
    n3 = random.randint(0,10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3) + '.jpg'
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)


class Cat_play(models.Model):
    name = models.CharField(max_length=250, verbose_name=u"Тип игры", blank=True, default="", unique=True)
    
    class Meta:
        db_table = "cat_play"
        verbose_name = "Тип игры"
        verbose_name_plural = "Тип игр"

    def __unicode__(self):
        return self.name


class Arena(models.Model):
    name = models.CharField(max_length=250, verbose_name=u"Название стадиона", blank=True, default="")
    city = models.CharField(max_length=250, verbose_name=u"Город", blank=True, default="")
    country = models.CharField(max_length=250, verbose_name=u"Страна", blank=True, default="")
    slug = models.CharField(max_length=250, blank=True, verbose_name=u'Картинка стадиона')
    
    class Meta:
        db_table = "arena"
        verbose_name = "стадион"
        verbose_name_plural = "стадионы"

    def __unicode__(self):
        return self.name

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Картинка стадиона'
    pic_slug.allow_tags = True                


class Team(models.Model):
    name = models.CharField(max_length=250, verbose_name=u"Название команды", blank=True, default="")
    city = models.CharField(max_length=250, verbose_name=u"Город", blank=True, default="")
    country = models.CharField(max_length=250, verbose_name=u"Страна", blank=True, default="")
    gender = models.CharField(max_length=250, verbose_name=u"Пол игроков", blank=True, default="")
    slug = models.CharField(max_length=250, blank=True, verbose_name=u'Герб команды')
    
    class Meta:
        db_table = "teams"
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __unicode__(self):
        return self.name

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Герб команды'
    pic_slug.allow_tags = True        


class Play(models.Model):
    name = models.CharField(max_length=250, verbose_name=u"Название игры", blank=True, default="")
    cat_play = models.ForeignKey(Cat_play, null=True, blank=True, verbose_name=u"Тип игры")
    enemy_team = models.ManyToManyField(Team, blank=True, related_name='enemy', verbose_name=u"Команда противник")
    place_game = models.ManyToManyField(Arena, blank=True, related_name='arena', verbose_name=u"Место встречи")
    is_home = models.BooleanField(verbose_name=u"Играем дома?")
    date = models.DateTimeField(verbose_name=u"Дата игры")
    slug = models.CharField(max_length=250, blank=True, verbose_name=u'Картинка игры')
    
    class Meta:
        db_table = "plays"
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ['date']

    def __unicode__(self):
        return self.name

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Картинка игры'
    pic_slug.allow_tags = True 

    def home_or_guest(self):
        if self.is_home: 
            return u'Играем дома.'
        else:
            return u'Играем в гостях.'    


class Players(models.Model):
    name = models.CharField(max_length=250, verbose_name=u"Имя + Фамилия игрока", blank=True, default="")
    team = models.ForeignKey(Team, null=True, blank=True, verbose_name=u"Команда игрока")
    short_text = RichTextUploadingField(blank=True, verbose_name="Короткое описание игрока")
    full_text = RichTextUploadingField(blank=True, verbose_name="Полное описание игрока")
    published = models.BooleanField(verbose_name=u"Опубликован")
    ordering = models.IntegerField(verbose_name=u"Порядок сортировки", default=0, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, verbose_name=u'Фото игрока')
    
    class Meta:
        db_table = "players"
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"
        ordering = ['ordering']

    def __unicode__(self):
        return self.name

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Фото игрока'
    pic_slug.allow_tags = True             


class Menu(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Название")
    
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = u"Меню"

    
class MenuItem(MPTTModel):
    menu = models.ForeignKey(Menu, null=True, blank=True, verbose_name=u"Меню")
    name = models.CharField(max_length=200, verbose_name=u"Название")
    slug = models.CharField(max_length=250, blank=True, verbose_name=u"Урл")
    full_text = RichTextField(blank=True, verbose_name="Полное описание")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u"Родительский пункт меню")
    published = models.BooleanField(verbose_name=u"Опубликован")
    ordering = models.IntegerField(verbose_name=u"Порядок сортировки", default=0, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"Пункты меню"
        
    class MPTTMeta:
        order_insertion_by = ['name']
    

    
class Meta(models.Model):
    meta_description = RichTextField(blank=True, verbose_name="Мета описание")
    meta_keywords = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    meta_title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    meta_author = models.CharField(max_length=250, blank=True, verbose_name="Автор сайта")
    # favicon = models.ImageField(upload_to=make_upload_path, blank=True,  verbose_name="favicon.ico")
    favicon_slug = models.CharField(max_length=250, blank=True, verbose_name="Урл favicon")
    published = models.BooleanField(verbose_name="Опубликован", blank=True, default=0)

    def __unicode__(self):
        return self.meta_title

    class Meta:
        verbose_name_plural = "Мета описания"
        verbose_name = "Мета описание"

    # def pic(self):
    #     if self.favicon:
    #         return u'<img src="%s" width="70"/>' % self.favicon.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True  

    def pic_slug(self):
        if self.favicon_slug:
            return u'<img src="%s" width="70"/>' % self.favicon_slug
        else:
            return '(none)'
    pic_slug.short_description = 'favicon'
    pic_slug.allow_tags = True       
        

        
class Snipet(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    text = RichTextField(blank=True, verbose_name="Код снипета")
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Сниппеты"
        verbose_name = "Сниппет"
      


class Top(models.Model):
    # image_back = models.ImageField(upload_to=make_upload_path, blank=True,  verbose_name="Изображение_1200x118")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    text_small = models.CharField(max_length=250, blank=True, verbose_name="Обещание")
    text_big = models.CharField(max_length=250, blank=True, verbose_name="Заявка на победу")
    published = models.BooleanField(verbose_name="Опубликован")
    
     
    def __str__(self):
        return self.text_small

    class Meta:
        verbose_name_plural = "Шапки"
        verbose_name = "Шапка"   

    # def pic(self):
    #     if self.image_back:
    #         return u'<img src="%s" width="70"/>' % self.image_back.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True  

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Картинка шапки'
    pic_slug.allow_tags = True   

  
              
        

        

    
    
