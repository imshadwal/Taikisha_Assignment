from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee_id', 'age']
    search_fields = ['name', 'employee_id']
    list_filter = ['age']
