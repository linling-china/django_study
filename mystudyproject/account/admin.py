from django.contrib import admin
from .models import UserAdded

# Register your models here.
class UserAddedAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('birth',)

admin.site.register(UserAdded, UserAddedAdmin)
