from django.contrib import admin
from contactus.models import Contactus
from django.contrib.admin import ModelAdmin, register

# Register your models here.


@register(Contactus)
class blogAdmin(ModelAdmin):
    list_display = ('name', 'email', 'message')
