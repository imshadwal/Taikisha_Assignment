from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['get'])
    def chart_data(self, request):
        employees = self.get_queryset()
        data = [{'name': emp.name, 'age': emp.age} for emp in employees]
        return Response(data)
