from django.contrib import admin
from .models import Category,Expense
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["title","category","amount","date","description"]

admin.site.register(Category)
admin.site.register(Expense,ExpenseAdmin)


    