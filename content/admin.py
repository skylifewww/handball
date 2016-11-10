from django.contrib import admin
from content.models import *
from content.fields import AdminImageWidget
from django.db import models




class Cat_playAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_editable = ['name']


class ArenaAdmin(admin.ModelAdmin):
    list_display = ['name', 'pic_slug', 'city', 'country']
    list_editable = ['name', 'city', 'country']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }  


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'pic_slug', 'city', 'country', 'gender']
    list_editable = ['name', 'city', 'country', 'gender']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }    

class PlayAdmin(admin.ModelAdmin):
    list_display = ['name', 'cat_play', 'result', 'is_home', 'date', 'pic_slug']
    
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }    

class PlayersAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'published', 'ordering', 'pic_slug']
    list_editable = ['name', 'published', 'ordering']
    
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }       


class MenuAdmin(admin.ModelAdmin):
    
    list_display = ['name']
    list_editable = ['name']


class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'menu', 'cat_play', 'slug', 'published', 'ordering']
    list_editable = ['slug', 'published', 'ordering']

    
class MetaAdmin(admin.ModelAdmin):
    list_display = ['meta_description', 'meta_keywords', 'meta_title', 'meta_author', 'pic_slug', 'published']
    list_editable = ['meta_description', 'meta_keywords', 'meta_title', 'meta_author', 'published']


class TopAdmin(admin.ModelAdmin):
    list_display = ['pic_slug', 'text_small', 'text_big', 'published']
    list_editable = ['text_small', 'text_big', 'published']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

class PhotosAdmin(admin.ModelAdmin):
    list_display = ['name', 'published', 'pic_slug']
    
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }   

# class  CategoryAdmin(admin.ModelAdmin):
#       list_display = ['name']        


# class SlideAdmin(admin.ModelAdmin):
#     list_display = ['name', 'pic_slug', 'category_article', 'published','ordering']
#     list_editable = ['published','ordering']
#     formfield_overrides = {
#         models.ImageField: {'widget': AdminImageWidget},
#     }

admin.site.register(Cat_play, Cat_playAdmin) 
admin.site.register(Photos, PhotosAdmin) 
admin.site.register(Arena, ArenaAdmin) 
admin.site.register(Team, TeamAdmin) 
admin.site.register(Play, PlayAdmin)   
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(Players, PlayersAdmin) 
# admin.site.register(Category, CategoryAdmin)

admin.site.register(Snipet)
admin.site.register(Top, TopAdmin)


