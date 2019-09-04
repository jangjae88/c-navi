from django.contrib import admin
from .models import Prouser, SearchResult, GotBlog

class ProuserAdmin(admin.ModelAdmin):
    list_display = ('user','password' ,'register_date')

class GotBlogAdmin(admin.ModelAdmin):
    list_display = ('search_result', 'title', 'content_url', 
    'original_name','original_url')

admin.site.register(Prouser, ProuserAdmin)
admin.site.register(SearchResult)
admin.site.register(GotBlog, GotBlogAdmin)

# Register your models here.
