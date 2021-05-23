from django.contrib import admin
from .models import Design,Comment
@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
  
  
admin.site.register(Comment)

