from django.contrib import admin
from .models import ListItems


# Register your models here.
class ListItemsAdmin(admin.ModelAdmin):
    list_display = ('menu', 'path', 'name', 'url')


admin.site.register(ListItems, ListItemsAdmin)
