
from django.contrib.admin import ModelAdmin, register

from blog.models import blog
# Register your models here.
# admin.site.register(blog)


@register(blog)
class blogAdmin(ModelAdmin):
    list_display = ('title', 'content', 'user')
