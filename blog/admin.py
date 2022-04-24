from django.contrib import admin

from blog.models import Topic, Post, Comment

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)
