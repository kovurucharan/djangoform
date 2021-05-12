from django.contrib import admin

# Register your models here.
from WebApp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["Name","Salary"]
admin.site.register(Employee,EmployeeAdmin)