from django.contrib import admin
from .models import Project, Post, Img

class ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'img')

# Register your models here.
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Img, ImgAdmin)