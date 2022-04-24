from django.contrib import admin
from .models import Users,Books,Orders

# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email']

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ['bookId','BookName','category']

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name','Book','orderId','IssueDate','returnDate']