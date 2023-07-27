from django.contrib import admin
from .models import award
class awardadmin(admin.ModelAdmin):
    list_display=['description','photo']
admin.site.register(award,awardadmin)
# Register your models here.
