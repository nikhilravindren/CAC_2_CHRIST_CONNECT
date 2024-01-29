from django.contrib import admin
from .models import JobPortal,user_posts,post_comments,post_likes,user_follow,messages,user_Notification

# Register your models here.
admin.site.register(JobPortal)
admin.site.register(user_posts)
admin.site.register(post_comments)
admin.site.register(post_likes)
admin.site.register(user_follow)
admin.site.register(messages)
admin.site.register(user_Notification)