from django.contrib import admin
from .models import user_profile,Notifications,admin_messages

admin.site.register(user_profile)
admin.site.register(Notifications)
admin.site.register(admin_messages)