from django.contrib import admin
from .models import User
from .tagsmodels import Tags
from .bannermodels import Banners
admin.site.register(User)
admin.site.register(Tags)
admin.site.register(Banners)

