from django.contrib import admin
from .models import CornerstoneUserProfile

class CornerstoneAdmin(admin.ModelAdmin):

    admin.site.register(CornerstoneUserProfile)
