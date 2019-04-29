from django.contrib import admin

# Register your models here.

from .models import Freelancer
from .models import Profesion

admin.site.register(Freelancer)
admin.site.register(Profesion)