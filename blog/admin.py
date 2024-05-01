from django.contrib import admin

from .models import Category, BlogPost



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']   
admin.site.register(Category, CategoryAdmin)



class BlogPostListAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'status']
    search_fields = ['title', 'text']
    list_filter = ['published_date']
admin.site.register(BlogPost, BlogPostListAdmin)    