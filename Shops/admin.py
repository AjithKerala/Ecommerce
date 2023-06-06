from django.contrib import admin

# Register your models here.
from .models import category
from .models import Productts
admin.site.register(category)
admin.site.register(Productts)