from django.contrib import admin
from .models import GeneralDepartment,Books,UserData,IssuedBooks
# Register your models here.
admin.site.register(GeneralDepartment)
admin.site.register(Books)
admin.site.register(UserData)
admin.site.register(IssuedBooks)



