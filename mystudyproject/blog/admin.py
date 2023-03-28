from django.contrib import admin
from .models import BlogArticles

# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title',)
    raw_id_fields = ('author',) #详情页，填入raw_id
    date_hierarchy = 'publish' #日期层级
admin.site.register(BlogArticles, BlogArticlesAdmin) #注册到管理后台，同时加入各类选项
