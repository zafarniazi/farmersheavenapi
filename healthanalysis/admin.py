from django.contrib import admin
from healthanalysis.models import HealthAnalysis
from django.contrib.admin import ModelAdmin, register

# Register your models here.
# admin.site.register(HealthAnalysis)


@register(HealthAnalysis)
class HealthAnalysisAdmin(ModelAdmin):
    list_display = ('name', 'path', 'user')
