from django.contrib import admin

# Register your models here.
from .models import Diseases, Gender

admin.site.register(Diseases)
admin.site.register(Gender)