from django.contrib import admin

# Register your models here.
from .models import User, Lead, Agent, UserProfile

admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)