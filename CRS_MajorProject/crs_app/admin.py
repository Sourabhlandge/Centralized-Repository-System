from django.contrib import admin

# Register your models here.
from django.contrib import admin
from crs_app.models import *

# Register your models here.
@admin.register(EducationModel)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

@admin.register(HealthModel)
class HealthAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

@admin.register(AgricultureModel)
class AgricultureAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

@admin.register(ElectricityModel)
class ElectricityAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

@admin.register(BusinessModel)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

@admin.register(YouthModel)
class YouthAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}

@admin.register(GovernmentJobsModel)
class GovernmentJobsAdmin(admin.ModelAdmin):
    list_display = ['title','slug_field','body','publish','created','updated','status']
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug_field':('title',)}



