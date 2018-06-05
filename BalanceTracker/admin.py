from django.contrib import admin
from .models import Transaction, SpendingSubCategory, SpendingCategory
# Register your models here.
admin.site.register(SpendingCategory)
admin.site.register(SpendingSubCategory)
admin.site.register(Transaction)
