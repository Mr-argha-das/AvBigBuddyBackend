from django.contrib import admin
from .models import User
from .tagsmodels import Tags
admin.site.register(User)
admin.site.register(Tags)
