from django.contrib import admin
from blog.models import Blog, Category

class CategoryAdmin(admin.ModelAdmin):
  list_display=["name"]
  readonly_fields=["slug"]
  search_fields=["name"]

class BlogAdmin(admin.ModelAdmin):
  list_display=["title", "imageFile", "isActive", "isHome", "category"]
  list_editable=["isActive", "isHome"]
  readonly_fields=["slug"]
  search_fields=["title"]
  list_filter=["isActive", "isHome", "category"]

# Register your models here.

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)