from django.contrib import admin
from .models import New, CompanyImg


# Register your models here.



admin.site.register(CompanyImg)
admin.site.register(New)



admin.site.site_header = 'DMS'
admin.site.site_title = 'DMS'