from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Roll)
admin.site.register(Order)
admin.site.register(Type)
admin.site.register(Color)