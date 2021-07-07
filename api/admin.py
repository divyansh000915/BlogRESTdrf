from django.contrib import admin

# Register your models here.
from api.models import Category, Comment, Post

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
