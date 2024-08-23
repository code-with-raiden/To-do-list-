from django.contrib import admin
from .models import To_do,History
# Register your models here.

class ToAdmin(admin.ModelAdmin):
    list_display = ['id','new_task','desc']
admin.site.register(To_do,ToAdmin)
admin.site.register(History)