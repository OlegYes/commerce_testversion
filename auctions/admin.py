from django.contrib import admin
from .models import User, Lots, Category, Seller_Lot
# Register your models here.

admin.site.register(User)
admin.site.register(Lots)
admin.site.register(Category)
admin.site.register(Seller_Lot)
