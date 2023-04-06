from django.contrib import admin
from .models import UserAdded, UserInfo

# Register your models here.
class UserAddedAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ('birth',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'company', 'aboutme', 'photo')

admin.site.register(UserAdded, UserAddedAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
