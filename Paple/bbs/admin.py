from django.contrib import admin
from bbs.models import Post, Question, Comment


admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Comment)