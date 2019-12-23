from django.contrib import admin
from videos.models import Category,Tags, Thumbnail, Videos

# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Thumbnail)
admin.site.register(Videos)