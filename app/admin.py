from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Contacts),
admin.site.register(Uploadproject),
admin.site.register(Personaldetail),



class PortfoliopageAdmin(admin.ModelAdmin):
    list_display = ('id','title','location')
admin.site.register(Portfoliopage, PortfoliopageAdmin),





