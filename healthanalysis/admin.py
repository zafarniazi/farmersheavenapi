from django.contrib import admin
from healthanalysis.models import HealthAnalysis
from django.contrib.admin import ModelAdmin, register

# Register your models here.
# admin.site.register(HealthAnalysis)


@register(HealthAnalysis)
class HealthAnalysisAdmin(ModelAdmin):
    list_display = ['name', 'user',
                    'min_value', 'max_value', 'mean_value', 'time_from', 'time_to']
    list_filter = ['user', 'name', 'min_value',
                   'max_value', 'mean_value', 'time_from', 'time_to']
