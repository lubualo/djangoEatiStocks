from django.contrib import admin
from .models import Bourse, Stock, Investment

admin.site.register(Bourse)
admin.site.register(Stock)
admin.site.register(Investment)
