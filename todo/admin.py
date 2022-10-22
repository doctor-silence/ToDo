from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):  #Добавляем дату создания
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)
