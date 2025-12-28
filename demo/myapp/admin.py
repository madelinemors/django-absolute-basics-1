from django.contrib import admin
from .models import TodoItem, WhatsAppItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(WhatsAppItem)
